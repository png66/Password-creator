import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length = int(input('Введите длину пароля')) 
password =''
if length >= 12:
    for i in range(length):
        password += random.choice(chars)
print(password) 
