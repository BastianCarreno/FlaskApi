from flask_marshmallow import Marshmallow

ma = Marshmallow()

class InstitucionSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nombre",
            "direccion",
            "descripcion",
            "fecha_creacion",
        )


institucion_schema = InstitucionSchema()
instituciones_schema = InstitucionSchema(many=True)