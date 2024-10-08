class UserService:
    def __init__(self):
        # In a real app, this might connect to a database. We'll use an in-memory store.
        self.users = {
            1: {'name': 'Alice', 'email': 'alice@example.com'},
            2: {'name': 'Bob', 'email': 'bob@example.com'}
        }
        self.next_id = 3

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
    
    def create_user(self, name, email):
        # Add a new user to the in-memory store.
        new_user_id = self.next_id
        self.users[new_user_id] = {'name': name, 'email': email}
        self.next_id += 1
        return self.users[new_user_id]
    
    def update_user(self, user_id, name=None, email=None):
        # Update an existing user in the in-memory store.
        if user_id not in self.users:
            return False
        if name is not None:
            self.users[user_id]['name'] = name
            if email is not None:
                self.users[user_id]['email'] = email
                return True
    
    def delete_user(self, user_id):
        # Delete an existing user from the in-memory store.
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
