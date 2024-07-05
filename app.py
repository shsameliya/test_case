# from flask import Flask, request, jsonify, make_response
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# # from model import User


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@127.0.0.1/pytest" 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# migrate = Migrate(app, db)

# # class User(db.Model):
# #     __tablename__ = 'users'

# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(80), unique=True, nullable=False)
# #     email = db.Column(db.String(120), unique=True, nullable=False)
# #     password = db.Column(db.String(120), unique=True, nullable=False)

# #     def json(self):
# #         return {'id': self.id,'username': self.username, 'email': self.email}


# # from app import views

# if __name__ == '__main__':
#     app.run(debug=True)


# app/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@127.0.0.1/pytest" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import views after app creation to avoid circular imports
# from app import views
# from app import views 
# from app import models

if __name__ == '__main__':
    app.run(debug=True)
