import requests
import json
import os

def fetch_and_save_personas():
    try:
        response = requests.get("http://127.0.0.1:5000/personas")
        response.raise_for_status()
        
        personas = response.json()
        # todo me quedse aqui mañana sigo 

        if not os.path.exists('personas_json'):
            os.makedirs('personas_json')
        
        for persona in personas:

            filename = f"{persona['dm_name']}_{persona['dm_lastname']}.json"
            filepath = os.path.join('personas_json', filename)
            

            with open(filepath, 'w') as file:
                json.dump(persona, file, indent=4)
            
            print(f"Datos guardados en {filepath}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    except ValueError:
        print("Error: La respuesta no es un JSON válido.")
    except KeyError:
        print("Error: La estructura de datos no es la esperada.")

#metod main
if __name__ == "__main__":
    fetch_and_save_personas()