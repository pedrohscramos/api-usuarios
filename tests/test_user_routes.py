import unittest
import json
from app import app

class TestUserRoutes(unittest.TestCase):

    def setUp(self):
        # Configuração inicial antes de cada teste
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_users(self):
        # Testa a rota de listagem de todos os usuários (GET /users/)
        response = self.app.get('/users/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_create_user(self):
        # Testa a criação de um novo usuário (POST /users/)
        new_user = {
            'name': 'João Silva',
            'email': 'joao@example.com',
            'age': 25
        }
        response = self.app.post('/users/', data=json.dumps(new_user),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], new_user['name'])
        self.assertEqual(data['email'], new_user['email'])
        self.assertEqual(data['age'], new_user['age'])

    def test_get_user_by_id(self):
        # Testa obter um usuário específico (GET /users/<user_id>)
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['id'], 1)

    def test_update_user(self):
        # Testa a atualização de um usuário (PUT /users/<user_id>)
        updated_user = {
            'name': 'João Silva Updated',
            'email': 'joao_updated@example.com',
            'age': 30
        }
        response = self.app.put('/users/1', data=json.dumps(updated_user),content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], updated_user['name'])
        self.assertEqual(data['email'], updated_user['email'])
        self.assertEqual(data['age'], updated_user['age'])

    def test_delete_user(self):
        # Testa a deleção de um usuário (DELETE /users/<user_id>)
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)

    def test_get_nonexistent_user(self):
        # Testa obter um usuário inexistente
        response = self.app.get('/users/999')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Usuário não encontrado')

    def test_create_user_invalid_data(self):
        # Testa a criação de um usuário com dados inválidos
        new_user = {
            'name': '',
            'email': 'joaoexample.com',  # Email inválido
            'age': -1                    # Idade inválida
        }
        response = self.app.post('/users/', data=json.dumps(new_user),content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('message', data)


if __name__ == '__main__':
    unittest.main()
