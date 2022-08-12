from crypt import methods
from dataclasses import fields
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sqlalchemy

app = Flask(__name__)

#Configuracion de la conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567890@localhost:3306/BD_REST_TEST'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

#Crea la tabla
class Productos(db.Model):
    id_producto          = db.Column(db.Integer, primary_key=True)
    nombre_producto      = db.Column(db.String(100))
    descripcion_producto = db.Column(db.String(100))

    def __init__(self, nombre, descripcion):
        self.nombre_producto      = nombre
        self.descripcion_producto = descripcion

db.create_all()

#Esquema
class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id_producto','nombre_producto','descripcion_producto')

#Respuesta unitaria
producto_schema = ProductoSchema()

#Respuesta multiple
productos_schema = ProductoSchema(many=True)

@app.route('/find',methods=['GET'])
def findProducto():
    all_productos =  Productos.query.all()
    result = productos_schema.dump(all_productos)
    return jsonify(result)



#HOME REST SERVICE
@app.route('/',methods=['GET'])
def index():
    return jsonify({'mensaje' : 'Bienvenido a mi primer servicio REST'})

if __name__ == "__main__":
    app.run(debug=True)
