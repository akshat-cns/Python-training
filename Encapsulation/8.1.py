class UserAccount:

    def __init__(self, username, password):
        self.username = username
        self.__password = self.__hash_password(password)

    def __hash_password(self, password):
        # the logic for password hashing goes here
        return password

    def verify_password(self, password):
        return self.__hash_password(password) == self.__password

    def change_password(self, old_password, new_password):
        if not self.verify_password(old_password):
            print("Old password is incorrect.")
        if len(new_password) < 6:
            raise ValueError("New password must be at least 6 characters long.")
        self.__password = self.__hash_password(new_password)
        print("Password has been successfully updated.")

    def get_username(self):
        return self.username
