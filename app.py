from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from utils.db import db

from routes.usuario import usuarios
from routes.institucion import institucion
from routes.proyectos import proyecto


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:admin12345@localhost:5432/prueba"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(usuarios)
app.register_blueprint(institucion)
app.register_blueprint(proyecto)

# Marshmallow(app)
# migrate = Migrate(app)



# class InstitucionModel(db.Model):
#     __tablename__ = "instituciones"

#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(100))
#     direccion = db.Column(db.String(100))
#     fecha_creacion = db.Column(db.DateTime(), default=today.strftime("%d/%m/%Y"))
#     proyectos = db.relationship(
#         "ProyectoModel", backref="institucion", lazy=False, cascade="all, delete-orphan"
#     )

#     def __init__(self, nombre, direccion, fecha_creacion):
#         self.nombre = nombre
#         self.direccion = direccion
#         self.fecha_creacion = fecha_creacion

#     def __repr__(self):
#         return f"<institución {self.nombre}>"


# # Modelo de Proyecto
# class ProyectoModel(db.Model):
#     __tablename__ = "proyectos"

#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(100))
#     descirpcion = db.Column(db.String(100))
#     fecha_inicio = db.Column(db.Date())
#     fecha_termino = db.Column(db.Date())
#     responsable = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
#     institucion_id = db.Column(
#         db.Integer, db.ForeignKey("instituciones.id"), nullable=False
#     )

#     def __init__(self, nombre, descirpcion, fecha_inicio, fecha_termino, responsable):
#         self.nombre = nombre
#         self.descirpcion = descirpcion
#         self.fecha_inicio = fecha_inicio
#         self.fecha_termino = fecha_termino
#         self.responsable = responsable

#     def __repr__(self):
#         return f"<proyecto {self.nombre}>"

# Creación de Schemas Usuario

