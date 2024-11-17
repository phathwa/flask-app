from app import create_app
from app.extensions import db
app = create_app()

with app.app_context():
    db.create_all()  # This will create all the tables defined in your models

if __name__ == "__main__":
    app.run(debug=True, port=5001)
