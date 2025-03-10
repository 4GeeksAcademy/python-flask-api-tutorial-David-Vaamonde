# Importar Flask y añadir el método jsonify a la importacion
from flask import Flask, jsonify, request
app = Flask(__name__)

# Ejemplo JSON
# Variable some_data
some_data = {"name": "David", "lastname": "Vaamonde"}

# Añadimos /myroute
@app.route('/myroute', methods=['GET'])
def hello():
    # Puedes convertir esa variable en una cadena json en la siguiente linea
    json_text = jsonify(some_data)

    # Y luego puedes devolverlo al fron-end en el cuerpo de la respuesta en la siguiente linea
    return json_text


# Variable todos
todos = [
    {"label": "My first task", "done": False}
]

# Método GET
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)

    return json_text


# Metodo POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(dict(request_body))
    return jsonify(todos)

# Metodo DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    del todos[position]
    return jsonify(todos)

# Estas dos línes simepre deben estar al final de tu archivo app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

