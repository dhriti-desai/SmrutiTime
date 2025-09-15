from app import create_app
from extensions import db
import os

app = create_app()

with app.app_context():
    # Remove existing database
    if os.path.exists('database.db'):
        os.remove('database.db')
    if os.path.exists('instance/database.db'):
        os.remove('instance/database.db')
    
    # Create new tables
    db.create_all()
    print("Database reset successfully!")