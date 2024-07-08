from flask import Flask
from app.models import db
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///graphql.db'

db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

@app.route('/')
def index():
    return 'Hello World'
