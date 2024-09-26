from flask import Flask
from flask_restx import Api
from adapters.controllers.user_controller import user_ns

app = Flask(__name__)

# Cria a instância da API do Flask-RESTX
api = Api(app, version='1.0', title='User API', description='API para cadastro de usuários usando Flask e JSON', doc='/docs')

# Registra o namespace dos usuários
api.add_namespace(user_ns, path='/users')

if __name__ == '__main__':
    app.run(debug=True)
