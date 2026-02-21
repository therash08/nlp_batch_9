# class User:
    
#     def myfunc(self):
#         return "this is included in the class user"
    
# user1 = User()
# print(user1.myfunc())

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # Ekhane 'self' jog korte hobe
    def display(self):
        print(f"{self.name}, {self.email}, {self.password}")

    def __str__(self):
        return (f"{self.name} -> {self.email}")
    
user1 = User("rasidul", "therash@gmail.com", '12345')       
user1.display()

user2 = User("kamal", "kamal@gmail.com", 'fiufgug')
user2.display()

print(user1)