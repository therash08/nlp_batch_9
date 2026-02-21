class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def display(self):
        print(f"user name : {self.name} email : {self.email}")


class Admin (User):
    def __init__(self, access_level,name, email, password):
        super().__init__(name,email,password)
        self.access_level = access_level


    def info(self):
        print(f"{self.name} {self.email} {self.access_level}")


admin1 = Admin("High", "rash", "therash@gmail.com", "2234nf4k")
admin1.info()