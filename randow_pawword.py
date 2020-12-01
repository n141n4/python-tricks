import random

def shuffle(string):
    tempList = list(string)
    print(tempList)
    random.shuffle(tempList)
    return ''.join(tempList)

passWord = ""

for i in range(4):
    passWord = passWord + chr(random.randint(65, 90)) + chr(random.randint(48, 57))

password = shuffle(passWord)    
print(passWord)