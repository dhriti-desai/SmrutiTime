from app import create_app
from extensions import db
from models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Create a test user
    test_email = "test@test.com"
    test_password = "123456"
    
    # Check if user already exists
    existing_user = User.query.filter_by(email=test_email).first()
    if existing_user:
        print("Test user already exists!")
    else:
        hashed_pw = generate_password_hash(test_password)
        test_user = User(email=test_email, password=hashed_pw)
        db.session.add(test_user)
        db.session.commit()
        print(f"Test user created: {test_email} / {test_password}")