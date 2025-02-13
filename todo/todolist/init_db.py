from todolist.main import app, db

# Drop existing database and create new tables
with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database recreated successfully.")

with app.app_context():
    db.create_all()
    print("Database initialized successfully.")
