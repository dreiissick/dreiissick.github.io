from app import app, db

# Create the tables in the database
with app.app_context():
    db.create_all()

print("Database and tables created successfully.")
