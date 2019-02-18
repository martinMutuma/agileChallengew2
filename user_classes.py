class User:
    user = [
        {"user_id": 1, "username": "Markize", "password": "Mark106", "role": "Normal User" "logged_in": False},
        {"user_id": 2,"username": "Peshy", "password": "Peshy101", "role": "moderator", "logged_in": False},
        {"user_id": 3,"username": "Martin", "password": "Martin101", "role": "Admin" "logged_in": False}
           ]
    
    def __init__(self, name, password, role, logged_in):
        self.name = name
        self.password = password
        self.role = role

    def edit_comment(self, comment):
        if comment.author.name == self.name:
            return True
        else:
            return False
      
    def delete_comment(self, comment):
        return False
     
class Moderator(User):
    def __init__(self, name):
        super().__init__(name)

    def delete_comment(self, comment):
        return True

class Admin(Moderator):
    def __init__(self, name):
        super().__init__(name)

    def delete_comment(self, comment):
        return True

    def edits_comment(self, comment):
        return True