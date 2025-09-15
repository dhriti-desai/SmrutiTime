from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date

from extensions import db
from models import User, JournalEntry, Smruti
from forms import LoginForm, RegisterForm

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ✅ Routes
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/journal', methods=['GET', 'POST'])
    def journal():
        from flask import session
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        today = date.today()
        entry_text = ''
        
        existing_entry = None  # Simplified for now
        
        if existing_entry:
            entry_text = existing_entry.content
        
        if request.method == 'POST':
            content = request.form.get('journal-entry')
            print(f"Journal entry saved: {content[:50] if content else 'Empty'}...")
            flash('Journal entry saved!', 'success')
            return redirect(url_for('journal'))
        
        return render_template('journal.html', today=today, entry=entry_text)

    @app.route('/journal/history')
    def journal_history():
        from flask import session
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        entries = []  # Simplified for now
        return render_template('journal_history.html', entries=entries)

    @app.route('/smruti', methods=['GET', 'POST'])
    def smruti():
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            author_name = request.form.get('author_name', 'Anonymous')
            
            new_smruti = Smruti(
                title=title,
                content=content,
                author_name=author_name
            )
            db.session.add(new_smruti)
            db.session.commit()
            flash('Your Smruti has been shared!', 'success')
            return redirect(url_for('smruti'))
        
        try:
            smrutis = Smruti.query.order_by(Smruti.created_at.desc()).all()
        except:
            smrutis = []
        return render_template('smruti.html', smrutis=smrutis)



    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            from flask import session
            session['logged_in'] = True
            session['user_email'] = email
            session['user_name'] = email.split('@')[0].title()
            return redirect(url_for('journal'))
        
        return render_template('login.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            
            from flask import session
            session['logged_in'] = True
            session['user_email'] = email
            session['user_name'] = f"{first_name} {last_name}"
            flash('Account created! Welcome to Smruti Time!', 'success')
            return redirect(url_for('journal'))
        return render_template('signup.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You have been logged out.', category='info')
        return redirect(url_for('home'))

    print("Registered Routes:")
    print(app.url_map)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully")
        except Exception as e:
            print(f"Database error: {e}")
    app.run(debug=True)

