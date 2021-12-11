import Signin
name = input('Name:')

print('Hello '+ name)
Signin.signin(name)

with open('Access_name.txt', 'w') as f:
    f.write(name)

