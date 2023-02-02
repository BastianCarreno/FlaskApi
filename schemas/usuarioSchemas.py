from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "RUT",
            "nombre",
            "apellidos",
            "fecha_de_nacimiento",
            "cargo",
            "edad",
        )


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)