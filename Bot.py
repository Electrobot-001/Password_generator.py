import random
password=""
char="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
digits=int(input("Quante cifre deve avere la password?"))
for i in range(digits):
    password+=random.choice(char)
print(password)
