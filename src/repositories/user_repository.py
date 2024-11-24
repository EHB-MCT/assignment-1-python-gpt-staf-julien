from typing import List, Optional

class UserRepository:
    def __init__(self):
        # In a real app, this might connect to a database. We'll use an in-memory store.
        self.users = {
            1: {'name': 'Alice', 'email': 'alice@example.com'},
            2: {'name': 'Bob', 'email': 'bob@example.com'}
        }
        self.next_id = 3

    def get_user_by_id(self, user_id) -> Optional[dict]:
        """
        Get a user by their ID.

        Arguments:
            user_id (int): The ID of the user to retrieve.

        Returns:
           dict or None: A dictionary containing the user's data if found, otherwise None.
        """
        # In a real app, this would query a database. We'll use an in-memory store.
        
        user_data = self.users.get(user_id)
        if user_data:
            return {'id': user_id, **user_data}
        return None

    def get_all_users(self)-> List[dict]:
        """
        Get all users.

        Returns:
            list: A list of dictionaries containing the user's data.
        """
        # In a real app, this would query a database. We'll use an in-memory store.
        users_list = []
        for uid, data in self.users.items():
            user_dict = {'id': uid, **data}
            users_list.append(user_dict)
        return users_list
    
    def create_user(self, name, email) -> dict:
        """
        Create a new user.

        Arguments:
            name (str): The name of the user to create.
            email (str): The email address of the user to create.

        Returns:
            dict: A dictionary containing the newly created user's data.
        """
        # In a real app, this would insert into a database. We'll use an in-memory store.
        # Generate a new ID for the user.
        new_user_id = self.next_id
        # Add a new user to the in-memory store.
        new_user_id = self.next_id
        self.users[new_user_id] = {'name': name, 'email': email}
        self.next_id += 1
        return self.users[new_user_id]
    
    def update_user(self, user_id, name=None, email=None) -> bool:
        """
        Update an existing user.

        Arguments:
            user_id (int): The ID of the user to update.
            name (str, optional): The new name for the user. Defaults to None.
            email (str, optional): The new email address for the user. Defaults to None.

        Returns:
            bool: True if the user was updated successfully, False otherwise.
        """
        # Update an existing user in the in-memory store.
        if user_id not in self.users:
            return False
        if name is not None:
            self.users[user_id]['name'] = name
            if email is not None:
                self.users[user_id]['email'] = email
                return True
    
    def delete_user(self, user_id) -> bool:
        """
        Delete an existing user.

        Arguments:
            user_id (int): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted successfully, False otherwise.
        """
        # Delete an existing user from the in-memory store.
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
