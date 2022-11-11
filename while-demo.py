sayilar = [4,6,9,10,35,57,89,125,244]

#1-> sayilar listesini while döngüsü ile yazdırınız.


#çözüm1
i= 0
while i < len(sayilar):
    print(sayilar[i])
    i+=1


#çözüm2
a = 0
b = len(sayilar)
while a < b :
    print(sayilar[a])
    a+=1

#2-> başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

baslangicDegeri = int(input("Başlangıç değerini giriniz: "))
bitisDegeri = int(input("Bitiş değerini giriniz: "))

i = baslangicDegeri

while i<bitisDegeri:
    i+=1
    if (i % 2 == 1):
        print(i)

#3-> 1 -100 arasındaki sayıları azalan şekilde yazdırın.

i = 100

while i > 1:
    i-=1
    print(i)
    

#4-> kullanıcıdan alacağınız 5 değeri sıralı şekilde yazdırın

sayilar = []
i = 0

while i < 5:
    x = int(input("Lütfen sayıyı giriniz: "))
    sayilar.append(x)
    i+=1
    sayilar.sort()
    print(sayilar)
    


