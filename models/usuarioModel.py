from utils.db import db

class Institucion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    fecha_creacion = db.Column(db.Date, nullable=False)
    proyectos = db.relationship('Proyecto', backref='institucion', lazy=True)

    def __init__(self, nombre, descripcion, direccion, fecha_creacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.direccion = direccion
        self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'<Institucion {self.nombre}>'

class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_termino = db.Column(db.Date, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    institucion_id = db.Column(db.Integer, db.ForeignKey('institucion.id'), nullable=False)

    def __init__(self, nombre, descripcion, fecha_inicio, fecha_termino, usuario_id, institucion_id):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.usuario_id = usuario_id
        self.institucion_id = institucion_id

    def __repr__(self):
        return f'<Proyecto {self.nombre}>'

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    RUT = db.Column(db.String(15), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    proyectos = db.relationship('Proyecto', backref='usuario', lazy=True)

    def __init__(self, nombre, apellidos, RUT, fecha_nacimiento, cargo, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.RUT = RUT
        self.fecha_nacimiento = fecha_nacimiento
        self.cargo = cargo
        self.edad = edad

    def __repr__(self):
        return f'<Usuario {self.nombre} {self.apellidos}>'
# class UsuarioModel(db.Model):
    
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(100))
#     apellidos = db.Column(db.String(100))
#     rut = db.Column(db.String(13))
#     fecha_de_nacimiento = db.Column(db.Date())
#     cargo = db.Column(db.String(100))
#     edad = db.Column(db.Integer())
#     fullname = db.column_property(nombre + " " + apellidos)
#     proyectos = db.relationship('ProyectoModel', backref='usuario', uselist=False)

#     def __init__(self, nombre, apellidos, rut, fecha_de_nacimiento, cargo, edad):
#         self.nombre = nombre
#         self.apellidos = apellidos
#         self.rut = rut
#         self.fecha_de_nacimiento = fecha_de_nacimiento
#         self.cargo = cargo
#         self.edad = edad

#     def __repr__(self):
#         return f"[usuario {self.nombre} {self.apellidos}]"

# class InstitucionModel(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(100))
#     direccion = db.Column(db.String(100))
#     fecha_creacion = db.Column(db.DateTime())
#     proyectos = db.relationship(
#         "ProyectoModel", back_populates="instituciones"
#     )

#     def __init__(self, nombre, direccion, fecha_creacion):
#         self.nombre = nombre
#         self.direccion = direccion
#         self.fecha_creacion = fecha_creacion

#     def __repr__(self):
#         return f"<institución {self.nombre}>"

# class ProyectoModel(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(100))
#     descirpcion = db.Column(db.String(100))
#     fecha_inicio = db.Column(db.Date())
#     fecha_termino = db.Column(db.Date())
#     responsable = db.Column(db.Integer, db.ForeignKey('usuario_model.id'))
#     institucion_id = db.Column(db.Integer, db.ForeignKey('institucion_model.id'))
#     instituciones = db.relationship(
#         "InstitucionModel", back_populates="proyectos"
#     )

#     def __init__(self, nombre, descirpcion, fecha_inicio, fecha_termino, responsable,instituciones):
#         self.nombre = nombre
#         self.descirpcion = descirpcion
#         self.fecha_inicio = fecha_inicio
#         self.fecha_termino = fecha_termino
#         self.responsable = responsable
#         self.instituciones = instituciones

#     def __repr__(self):
#         return f"<proyecto {self.nombre}>"

