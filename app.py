from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

def load_personas():
    try:
        if not os.path.exists('personas.json'):
            raise FileNotFoundError("El archivo personas.json no fue encontrado.")
        
        with open('personas.json', 'r') as file:
            data = json.load(file)
        
        if not isinstance(data, list):
            raise ValueError("El archivo personas.json debe contener una lista de objetos.")
        
        return data

    except FileNotFoundError as e:
        return {"error": str(e)}, 404
    except json.JSONDecodeError:
        return {"error": "El archivo personas.json no contiene un JSON válido."}, 400
    except ValueError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": f"Error inesperado: {str(e)}"}, 500

@app.route('/personas', methods=['GET'])
def get_personas():
    result = load_personas()
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
