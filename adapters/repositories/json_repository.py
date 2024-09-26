import json
import os

USER_FILE = 'users.json'

class JsonUserRepository:
    def __init__(self):
        if not os.path.exists(USER_FILE):
            with open(USER_FILE, 'w') as f:
                json.dump([], f)

    def get_all_users(self):
        with open(USER_FILE, 'r') as f:
            return json.load(f)

    def get_user_by_id(self, user_id):
        users = self.get_all_users()
        return next((user for user in users if user['id'] == user_id), None)

    def save_user(self, user):
        users = self.get_all_users()
        users.append(user.to_dict())
        self._save_all_users(users)

    def delete_user(self, user_id):
        users = self.get_all_users()
        updated_users = [user for user in users if user['id'] != user_id]
        self._save_all_users(updated_users)

    def _save_all_users(self, users):
        with open(USER_FILE, 'w') as f:
            json.dump(users, f, indent=4)