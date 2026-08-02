
import random
import string
uzunluk = int(input("Şifre uzunluğunu girin: "))
tane = int(input("Kaç tane şifre istiyorsunuz: ")) 

for j in range(tane):
    for i in range(uzunluk):
        print(random.choice(string.ascii_letters + string.digits + string.punctuation), end="")
    print()
    print("şifre oluşturuldu.")