class UserService:
    def __init__(self):
        # In a real app, this might connect to a database. We'll use an in-memory store.
        self.users = {
            1: {'name': 'Alice', 'email': 'alice@example.com'},
            2: {'name': 'Bob', 'email': 'bob@example.com'}
        }

    def get_user_by_id(self, user_id):
        user_data = self.users.get(user_id)
        if user_data:
            return {'id': user_id, **user_data}
        return None

    def get_all_users(self):
        users_list = []
        for uid, data in self.users.items():
            user_dict = {'id': uid, **data}
            users_list.append(user_dict)
        return users_list
