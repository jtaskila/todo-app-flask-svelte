from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

db_config = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///todoapp.sqlite3',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}
