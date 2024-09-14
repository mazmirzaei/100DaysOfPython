class User:
    """ The attributes are the things that the object has and the methods
    are the things that the object does."""
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Maziyar")
user_2 = User("002", "Tannaz")

user_1.follow(user_2)

print(user_1.user_id, user_1.user_name, user_1.followers, user_1.following)
print(user_2.user_id, user_2.user_name, user_2.followers, user_2.following)
