user = {'name': 'rasidul'}
# print(user)
# print(len(user))

user['age'] = 23
print(user)
print(len(user))
user.update(status ='chowdhury')
print(user)

user.update({'city':'sylhet','job':'engineer'})
# print(user)
print(len(user))

user.update(name ='rash')
print(user)

del user["age"]
print(user) 