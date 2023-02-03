from flask import Flask, request, jsonify
from utils.db import db

from routes.usuario import usuarios
from routes.institucion import institucion
from routes.proyectos import proyecto


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:admin12345@localhost:5432/api_flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(usuarios)
app.register_blueprint(institucion)
app.register_blueprint(proyecto)