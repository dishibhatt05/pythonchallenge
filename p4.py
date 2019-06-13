'''
take all input from user .

i)  check that all character are string
ii)  if all char are string then create user in your linux based OS
iii)  also create password for same user , password will
      password will be  ===>>     hello{username}
'''
import os


def checkDigit(name):
    return any(char.isdigit() for char in name )


name=input('Enter String :')
if not checkDigit(name):
    pas="hello"+name
    com="useradd -p $(openssl passwd -1 "+pas+") "+name
    os.system(com)

else:
    print("user Cannot be created")

