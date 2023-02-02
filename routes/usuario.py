from flask import Blueprint, request, jsonify
from models.usuarioModel import Usuario, Proyecto
from utils.db import db
from schemas.usuarioSchemas import usuario_schema, usuarios_schema
from datetime import datetime

usuarios = Blueprint('usuarios', __name__)


""" Json to create user"""
"""
    {
    "apellidos": "Carreños Navarros",
    "cargo": "ing. Informático",
    "edad": 25,
    "fecha_de_nacimiento": "1998-07-17",
    "id": 1,
    "nombre": "Bastian Ignacio",
    "rut": "199048"
    }
"""


@usuarios.route("/usuario", methods=["POST"])
def crear_usuario():
    print(request.json)
    nombre = request.json["nombre"]
    apellidos = request.json["apellidos"]
    edad = request.json["edad"]
    rut = request.json["rut"]
    cargo = request.json["cargo"]
    fecha_de_nacimiento = datetime.strptime(
        request.json["fecha_de_nacimiento"], "%Y-%m-%d"
    ).date()

    usuario = Usuario(nombre, apellidos, rut, fecha_de_nacimiento, cargo, edad)

    db.session.add(usuario)
    db.session.commit()
    return usuario_schema.jsonify(usuario)


@usuarios.route("/ver/usuarios", methods=["GET"])
def ver_usuarios():
    usuarios = Usuario.query.all()
    results = [
    {
        "id":           usuario.id,
        "rut":          usuario.RUT,
        "nombre":       usuario.nombre,
        "apellidos":    usuario.apellidos,
        "fecha_de_nacimiento": usuario.fecha_nacimiento,
        "cargo":        usuario.cargo,
        "edad":         usuario.edad
    } for usuario in usuarios]
    return results

@usuarios.route("/ver/usuario/<string:rut>/proyectos", methods=["GET"])
def ver_usuario_proyectos(rut):
    usuario = Usuario.query.filter( Usuario.RUT == rut).first()
    if usuario:
        proyectos = Proyecto.query.filter_by(usuario_id=usuario.id).all()
        results = [
            {
                "id": proyecto.id,
                "nombre": proyecto.nombre,
                "descripcion": proyecto.descripcion,
                "fecha_inicio": proyecto.fecha_inicio,
                "fecha_termino": proyecto.fecha_termino,
                "responsable": usuario.nombre
                + " "
                + usuario.apellidos,
            }
            for proyecto in proyectos
        ]

        return {"Rut": usuario.RUT, "Nombre": usuario.nombre,"apellidos": usuario.apellidos,"edad": usuario.edad, "cargo":usuario.cargo,    "proyectos": results}
    else:
        return {"error": "Usuario no encontrado"}, 404

@usuarios.route("/ver/usuario/<string:rut>", methods=["GET"])
def ver_usuario(rut):
    usuario = Usuario.query.filter( Usuario.RUT == rut).first()
    return usuario_schema.jsonify(usuario)


@usuarios.route("/actualizar/usuario/<int:id>", methods=["PUT"])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    usuario.nombre = request.json["nombre"]
    usuario.apellidos = request.json["apellidos"]
    usuario.rut = request.json["rut"]
    usuario.cargo = request.json["cargo"]
    usuario.edad = request.json["edad"]
    usuario.fecha_de_nacimiento = datetime.strptime(
        request.json["fecha_de_nacimiento"], "%Y-%m-%d"
    ).date()
    db.session.commit()
    return usuario_schema.jsonify(usuario)


@usuarios.route("/eliminar/usuario/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return usuario_schema.jsonify(usuario)