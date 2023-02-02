from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ProyectoSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nombre",
            "fecha_inicio",
            "fecha_termino",
            "usuario_id",
            "institucion_id",
        )


proyecto_schema = ProyectoSchema()
proyectos_schema = ProyectoSchema(many=True)