from flask import Flask, render_template, request
import bayesiano
app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

  ###################################Definimos el route con el método POST
@app.route('/usuario',methods=['POST'])
def usuario():
    nombre = request.form['nombre']
    correo = request.form['correo']
    ocupacion = request.form['ocupacion']
    mayor = request.form['mayor']
    compras = request.form['compras']
    productos = request.form['productos']
    p_ocupacion = int (ocupacion)
    p_mayor = int (mayor)
    p_compras = int (compras)
    p_productos = int (productos)
    bayesiano.bayesiano(nombre,correo,p_ocupacion,p_mayor,p_compras,p_productos)
    return render_template("usuario.html")

 ###################################

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
