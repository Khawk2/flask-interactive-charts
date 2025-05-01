from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/datos')
def obtener_datos():
    # Generamos datos aleatorios para el gráfico
    datos = {
        'labels': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        'valores': [random.randint(10, 100) for _ in range(5)]
    }
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True) 