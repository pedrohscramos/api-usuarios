# Flask User API

Essa API permite o cadastro, listagem, atualização e exclusão de usuários, salvando os dados em um arquivo JSON local.

## Como executar

1. Clone este repositório
`git clone https://github.com/pedrohscramos/api-usuarios.git`

2. Instale as dependências:
`pip install -r requirements.txt`

3. Execute o servidor Flask:
`python app.py`

4. Acesse a API em `http://localhost:5000`

## Endpoints

### 1.Criar Usuário

- **POST** `/users`
- **Body (JSON)**:

```json
{
 "name": "John Doe",
 "email": "johndoe@example.com",
 "age": 30
}
```

### 2. Listar Usuários

- **GET** `/users`

### 3. Obter Usuário pelo ID

- **GET** `/users/<user_id>`

### 4. Atualizar Usuário

- **PUT** `/users/<user_id>`
- **Body** (JSON)**:

```json
{
  "name": "John Updated",
  "email": "newemail@example.com",
  "age": 31
}
```

### 5. Deletar Usuário

- **DELETE** `/users/<user_id>`
