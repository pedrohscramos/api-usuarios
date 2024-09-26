from core.entities.user import User
from adapters.repositories.json_repository import JsonUserRepository


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, name, email, age):
        users = self.user_repository.get_all_users()

        if any(user['email'] == email for user in users):
            raise ValueError("Usuário já cadastrado.")

        new_user = User(
            id=len(users) + 1,
            name=name,
            email=email,
            age=age
        )

        self.user_repository.save_user(new_user)
        return new_user

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado.")
        return user

    def update_user(self, user_id, name=None, email=None, age=None):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado.")

        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if age:
            user['age'] = age

        self.user_repository.save_users(user)
        return user

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)