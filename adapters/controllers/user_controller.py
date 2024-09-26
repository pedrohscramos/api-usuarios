from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from core.services.user_service import UserService
from adapters.repositories.json_repository import JsonUserRepository

# Cria um namespace para o controller de usuários
user_ns = Namespace('users', description='Operações relacionadas aos usuários')

user_service = UserService(JsonUserRepository())

# Define o modelo de entrada/saída de dados para o Swagger
user_model = user_ns.model('User', {
    'id': fields.Integer(readOnly=True, description='Identificador único do usuário'),
    'name': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Email do usuário'),
    'age': fields.Integer(required=True, description='Idade do usuário')
})

# Rota para criar um novo usuário
@user_ns.route('/')
class UserList(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_list_with(user_model)
    def get(self):
        '''Lista todos os usuários'''
        return user_service.get_all_users(), 200

    @user_ns.doc('create_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        '''Cria um novo usuário'''
        data = request.get_json()
        try:
            new_user = user_service.create_user(
                name=data['name'],
                email=data['email'],
                age=data['age']
            )
            return new_user.to_dict(), 201
        except ValueError as e:
            return {'message': str(e)}, 400

# Rota para operações com usuários específicos
@user_ns.route('/<int:user_id>')
@user_ns.response(404, 'Usuário não encontrado')
@user_ns.param('user_id', 'O identificador único do usuário')
class User(Resource):
    @user_ns.doc('get_user')
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        '''Obtém um usuário específico'''
        try:
            user = user_service.get_user_by_id(user_id)
            return user, 200
        except ValueError as e:
            return {'message': str(e)}, 404

    @user_ns.doc('delete_user')
    @user_ns.response(204, 'Usuário deletado')
    def delete(self, user_id):
        '''Deleta um usuário'''
        try:
            user_service.delete_user(user_id)
            return '', 204
        except ValueError as e:
            return {'message': str(e)}, 404

    @user_ns.doc('update_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        '''Atualiza um usuário'''
        data = request.get_json()
        try:
            updated_user = user_service.update_user(
                user_id=user_id,
                name=data.get('name'),
                email=data.get('email'),
                age=data.get('age')
            )
            return updated_user, 200
        except ValueError as e:
            return {'message': str(e)}, 404
