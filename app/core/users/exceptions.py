class user_not_found_exception(Exception):
    def __init__(self, user_id):
        self.user_id = user_id
        self.message = f"User with ID {user_id} not found."
        super().__init__(self.message)

class user_creation_exception(Exception):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.message = f"User with name {name} and email {email} already exists or cannot be created."
        super().__init__(self.message)

class user_update_exception(Exception):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.message = f"User with name {name} and email {email} cannot be updated."
        super().__init__(self.message)

class user_deletion_exception(Exception):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.message = f"User with name {name} and email {email} cannot be deleted."
        super().__init__(self.message)