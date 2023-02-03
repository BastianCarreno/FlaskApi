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