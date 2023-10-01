from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import mongodb as dbase
from articulo import Articulo

db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    products = db['final2']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)

#Method Post
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    id = request.form['id']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']

    if id and nombre and descripcion:
        product = Articulo(id, nombre, descripcion)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'id' : id,
            'nombre' : nombre,
            'descripcion' : descripcion
        })
        return redirect(url_for('home'))
    else:
        return notFound()


if __name__ == '__main__':
    app.run(debug=True, port=4000)