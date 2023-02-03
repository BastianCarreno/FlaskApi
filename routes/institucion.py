from flask import Blueprint, request, jsonify
from models.usuarioModel import Usuario, Institucion, Proyecto
from schemas.institucionSchema import institucion_schema, instituciones_schema
from utils.db import db
from datetime import datetime

institucion = Blueprint("instituciones", __name__)

"""         JSon de ejemplo para la creacion de una institucion, proyectos relacionados y responsable de los proyectos
{
    "nombre": "Institucion 1",
    "direccion":"psje. titanic 2769",
    "fecha_creacion": "2023-02-02",
    "proyectos":[
        {
            "nombre": "Proyecto 1",
            "descirpcion": "Descripción Proyecto 1",
            "fecha_inicio": "2022-07-17",
            "fecha_termino": "2023-07-17",
            "responsable": 
                    {
                        "apellidos": "Carreños Navarros",
                        "cargo": "ing. Informático",
                        "edad": 25,
                        "fecha_de_nacimiento": "1998-07-17",
                        "id": 1,
                        "nombre": "Bastian Ignacio",
                        "rut": "199048"
                    }
        },{
            "nombre": "Proyecto 2",
            "descirpcion": "Descripción Proyecto 2",
            "fecha_inicio": "2022-07-17",
            "fecha_termino": "2023-07-17",
            "responsable": 
                    {
                        "apellidos": "Carreños Navarros",
                        "cargo": "ing. Informático",
                        "edad": 25,
                        "fecha_de_nacimiento": "1998-07-17",
                        "nombre": "Bastian Ignacio",
                        "rut": "199048"
                    }
        }
    ]
}
"""


# Creacion de Institucion con "X" proyectos y con sus respectivos responsables
@institucion.route("/crear/institucion/proyecto/usario", methods=["POST"])
def crear_institucion_proyectos_usuario():
    data = request.get_json()

    nombre = data.get("nombre")
    direccion = data.get("direccion")
    fecha_creacion = data.get("fecha_creacion")
    descripcion = data.get("descripcion")
    proyectos = data.get("proyectos")

    # Validación de datos para la institucion
    if (
        not nombre
        or not direccion
        or not fecha_creacion
        or not proyectos
        or not descripcion
    ):
        return (
            jsonify(
                {"error": "Faltan datos para crear la institución y los proyectos"}
            ),
            400,
        )

    # Validación formato de fecha
    try:
        fecha_creacion = datetime.strptime(fecha_creacion, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "La fecha de creación no es válida"}), 400

    institucion = Institucion(
        nombre=nombre,
        direccion=direccion,
        fecha_creacion=fecha_creacion,
        descripcion=descripcion,
    )

    proyectos = []
    for proyecto_data in data["proyectos"]:

        #Validamos si el Usuario a crear ya existe en la base de datos
        usuario = Usuario.query.filter(
            Usuario.nombre == proyecto_data["responsable"]["nombre"],
            Usuario.apellidos == proyecto_data["responsable"]["apellidos"],
            Usuario.edad == proyecto_data["responsable"]["edad"],
            Usuario.fecha_nacimiento
            == proyecto_data["responsable"]["fecha_de_nacimiento"],
            Usuario.cargo == proyecto_data["responsable"]["cargo"],
            Usuario.RUT == proyecto_data["responsable"]["rut"],
        ).first()

        # Si no se Enccuentra en la base de datos procedemos a crear el usuario
        if usuario == None:
            usuario = Usuario(
                nombre=proyecto_data["responsable"]["nombre"],
                apellidos=proyecto_data["responsable"]["apellidos"],
                edad=proyecto_data["responsable"]["edad"],
                fecha_nacimiento=proyecto_data["responsable"]["fecha_de_nacimiento"],
                cargo=proyecto_data["responsable"]["cargo"],
                RUT=proyecto_data["responsable"]["rut"],
            )
            db.session.add(usuario)
            db.session.commit()
        proyecto = Proyecto(
            nombre=proyecto_data["nombre"],
            descripcion=proyecto_data["descirpcion"],
            fecha_inicio=proyecto_data["fecha_inicio"],
            fecha_termino=proyecto_data["fecha_termino"],
            usuario_id=usuario.id,
            institucion_id=institucion.id,
        )
        proyectos.append(proyecto)

    institucion.proyectos = proyectos

    db.session.add(institucion)
    db.session.add_all(proyectos)
    db.session.commit()

    return {"Estado": "Exito"}


"""
    {
    "nombre": "Institución 1",
    "descripcion": "Descripcion de la Institución 1",
    "direccion": "Santiago Maipú",
    "fecha_creacion":"2020-09-12" 
    }
"""
# Creacion de Institucion
@institucion.route("/crear/institucion", methods=["POST"])
def crear_institucion():
    data = request.get_json()

    nombre = data.get("nombre")
    direccion = data.get("direccion")
    fecha_creacion = data.get("fecha_creacion")
    descripcion = data.get("descripcion")

    # Validación de datos para la institucion
    if not nombre or not direccion or not fecha_creacion or not descripcion:
        return (
            jsonify(
                {"error": "Faltan datos para crear la institución"}
            ),
            400,
        )

    # Validación de correcto formato de fecha
    try:
        fecha_creacion = datetime.strptime(fecha_creacion, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "La fecha de creación no es válida"}), 400

    # institucion = Institucion(nombre=data["nombre"],direccion=data["direccion"],fecha_creacion=data["fecha_creacion"])
    institucion = Institucion(
        nombre=nombre,
        direccion=direccion,
        fecha_creacion=fecha_creacion,
        descripcion=descripcion,
    )
    db.session.add(institucion)
    db.session.commit()
    return institucion_schema.jsonify(institucion)


# Listar todas las Instituciones
@institucion.route("/ver/instituciones", methods=["GET"])
def ver_instituciones():
    institucion = Institucion.query.all()
    return instituciones_schema.jsonify(institucion)



# Listar todas las Instituciones
@institucion.route("/ver/instituciones/maps", methods=["GET"])
def ver_instituciones_maps():
    instituciones = Institucion.query.all()
    results = [
            {
                "nombre": institucion.nombre,
                "abreviacion": institucion.nombre[:3],
                "descripcion": institucion.descripcion,
                "direccion": "https://www.google.com/maps/search/"+institucion.direccion.replace(" ", "+"),
                "fecha_creacion": institucion.fecha_creacion,
                "id": institucion.id,
            }
            for institucion in instituciones
        ]
    return {"Instituciones": results}


# Listar todos los proyectos de una institucion por la id
@institucion.route("/institucion/<int:institucion_id>/proyectos", methods=["GET"])
def ver_proyectos_institucion(institucion_id):
    institucion = Institucion.query.get(institucion_id)
    if institucion:
        proyectos = Proyecto.query.filter_by(institucion_id=institucion_id).all()
        results = [
            {
                "id": proyecto.id,
                "nombre": proyecto.nombre,
                "descripcion": proyecto.descripcion,
                "fecha_inicio": proyecto.fecha_inicio,
                "fecha_termino": proyecto.fecha_termino,
                "responsable": Usuario.query.get(proyecto.usuario_id).nombre
                + " "
                + Usuario.query.get(proyecto.usuario_id).apellidos,
            }
            for proyecto in proyectos
        ]

        return {"Instiucion": institucion.nombre,"direccion": institucion.direccion,"Descripcion": institucion.descripcion,"Fecha_creacion": institucion.fecha_creacion,   "proyectos": results}
    else:
        return {"error": "Institución no encontrada"}, 404


# Actualizar una institucion por la id
@institucion.route("/institucion/<int:institucion_id>/actualizar", methods=["PUT"])
def actualizar_institucion(institucion_id):
    institucion = Institucion.query.get(institucion_id)
    if institucion:
        data = request.get_json()
        nombre = data.get("nombre")
        direccion = data.get("direccion")
        fecha_creacion = data.get("fecha_creacion")
        descripcion = data.get("descripcion")

        if not nombre or not direccion or not fecha_creacion or not descripcion:
            return (
                jsonify(
                    {"error": "Faltan datos para crear la institución y los proyectos"}
                ),
                400,
            )

        try:
            fecha_creacion = datetime.strptime(fecha_creacion, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "La fecha de creación no es válida"}), 400
        institucion.nombre=nombre
        institucion.direccion=direccion
        institucion.fecha_creacion=fecha_creacion
        institucion.descripcion=descripcion

        db.session.commit()
        return institucion_schema.jsonify(institucion)


# Eliminar una institucion por la id
@institucion.route("/institucion/<int:institucion_id>/eliminar", methods=["DELETE"])
def eliminar_institucion(institucion_id):
    usuario = Institucion.query.get_or_404(institucion_id)
    db.session.delete(usuario)
    db.session.commit()
    return institucion_schema.jsonify(usuario)