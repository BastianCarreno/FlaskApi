from flask import Blueprint, request, jsonify
from models.usuarioModel import Usuario, Institucion, Proyecto
from schemas.proyectoSchema import proyecto_schema, proyectos_schema
from utils.db import db
from datetime import datetime

proyecto = Blueprint("proyectos", __name__)

"""
    {
    "nombre": "Proyecto 3",
    "descripcion": "Descripción Institucion 3",
    "fecha_inicio": "2022-02-02",
    "fecha_termino": "2023-02-02",
    "usuario_id": 2,
    "institucion_id": 5
    }
"""

@proyecto.route("/crear/proyecto", methods=["POST"])
def crear_proyecto():
    data = request.get_json()

    nombre=data.get("nombre")
    descripcion=data.get("descripcion")
    fecha_inicio=data.get("fecha_inicio")
    fecha_termino=data.get("fecha_termino")
    usuario_id=data.get("usuario_id")
    institucion_id=data.get("institucion_id")

    # Validación de datos para la institucion
    if not nombre or not descripcion or not fecha_inicio or not fecha_termino or not usuario_id or not institucion_id:
        return (
            jsonify(
                {"error": "Faltan datos para crear la institución y los proyectos"}
            ),
            400,
        )

    # Validación de correcto formato de fecha
    try:
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_termino = datetime.strptime(fecha_termino, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "La fecha de creación no es válida"}), 400

    if not Usuario.query.get(usuario_id):
        return (
            jsonify(
                {"error": "Usuario no encontrado"}
            ),
            400,
        )

    if not Institucion.query.get(institucion_id):
        return (
            jsonify(
                {"error": "Institucion no encontrada"}
            ),
            400,
        )
    # institucion = Institucion(nombre=data["nombre"],direccion=data["direccion"],fecha_creacion=data["fecha_creacion"])
    proyecto = Proyecto(
        nombre=nombre,
        descripcion=descripcion,
        fecha_inicio=fecha_inicio,
        fecha_termino=fecha_termino,
        usuario_id=usuario_id,
        institucion_id=institucion_id,
    )
    db.session.add(proyecto)
    db.session.commit()
    return proyecto_schema.jsonify(proyecto)

@proyecto.route("/ver/proyectos", methods=["GET"])
def ver_proyectos():
    proyecto = Proyecto.query.all()
    return proyectos_schema.jsonify(proyecto)

@proyecto.route("/ver/proyectos/termino", methods=["GET"])
def ver_proyectos_termino():
    proyectos = Proyecto.query.all()
    result = []
    for proyecto in proyectos:
        dias = obtener_diferencia_dias(proyecto.fecha_termino)
        json = {
            "nombre": proyecto.nombre,
            "dias_termino": dias
        }
        result.append(json)

    return {"Proyectos": result}

def obtener_diferencia_dias(fecha):
    today = datetime.now().date()
    difference = (fecha - today).days
    return difference