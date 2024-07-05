from flask_sqlalchemy import SQLAlchemy
from app_name import app


app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@127.0.0.1/pytest" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

