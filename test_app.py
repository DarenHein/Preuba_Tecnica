import unittest
import os
import json
from app import app, load_personas

class TestApp(unittest.TestCase):

    def test_load_personas_success(self):
        with open('personas.json', 'w') as file:
            file.write('[{"dm_name": "John", "dm_lastname": "Doe"}]')
        
        result = load_personas()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['dm_name'], 'John')
        self.assertEqual(result[0]['dm_lastname'], 'Doe')

        os.remove('personas.json')

    def test_load_personas_file_not_found(self):
        if os.path.exists('personas.json'):
            os.remove('personas.json')

        result = load_personas()
        self.assertEqual(result[0]['error'], "El archivo personas.json no fue encontrado.")
        self.assertEqual(result[1], 404)

    def test_load_personas_invalid_json(self):
        with open('personas.json', 'w') as file:
            file.write('not a json')

        result = load_personas()
        self.assertEqual(result[0]['error'], "El archivo personas.json no contiene un JSON válido.")
        self.assertEqual(result[1], 400)

        os.remove('personas.json')

    def test_load_personas_invalid_format(self):
        with open('personas.json', 'w') as file:
            file.write('{"not": "a list"}')

        result = load_personas()
        self.assertEqual(result[0]['error'], "El archivo personas.json debe contener una lista de objetos.")
        self.assertEqual(result[1], 400)

        os.remove('personas.json')
    #todo solo falta terminat el tes de chcear si abre bien el json
    def test_get_personas(self):
        with open('personas.json', 'w') as file:
            file.write('[{"dm_name": "Alice", "dm_lastname": "Smith"}]')
        
        with app.test_client() as client:
            response = client.get('/personas')
            self.assertEqual(response.status_code, 200)
            personas = json.loads(response.data)
            self.assertEqual(len(personas), 1)
            self.assertEqual(personas[0]['dm_name'], 'Alice')
            self.assertEqual(personas[0]['dm_lastname'], 'Smith')

        os.remove('personas.json')

if __name__ == "__main__":
    unittest.main()
