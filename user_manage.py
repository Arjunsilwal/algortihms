"""We need to create a data structure which can store 100 million records
 and perform insertion, search, update and list operations efficiently."""


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(username = '{self.username}', name = '{self.name}', email = '{self.email}')"


Aakash = User('aakash', 'Aakash RaJ', 'aakash@example.com')
Biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
Hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
Jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
Siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
Sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
Vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [Aakash, Biraj, Hemanth, Jadhesh, Siddhant, Sonaksh, Vishal]

print(users)


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users
