class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

data = [{"name": "rash", "age" : 23 }, {"name": "abdullah", "age": 24}]

user_objects = [User(**item) for item in data]

print(user_objects)