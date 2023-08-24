import random

karakterler= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

kullanici= int(input('Bir şifre uzunluğu giriniz'))

parola= ''

for i in range(kullanici):
   
    parola=parola+ random.choice(karakterler)

print(parola)