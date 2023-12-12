# PascalCase camelCase snake_case
class User:
    #pass
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following += 1 
        
        
user_1 = User("001","desdemona",)
user_2 = User("002","alodi",)
user_1.follow(user_2)
print(user_1.following)
