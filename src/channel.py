class Channel:
    def __init__(self, name):
        self.name = name
        self.users = {}

    def add_user(self, user):
        if user.nickname not in self.users:
            self.users[user.nickname] = user

    def remove_user(self, user):
        if user.nickname in self.users:
            del self.users[user.nickname]

    def list_users(self):
        return list(self.users.keys())