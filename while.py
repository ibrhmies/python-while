sayilar = [2,5,7,9]

#=>for döngüsünü bir collection için yani liste içindeki elemanları döndürmesi için kullanırız.
#-> 1- 100 => koşul=> while bir koşulla beraber döngü oluşturmak için while kullanırız

i = 0

while i<10:
    print('merhaba')
    i+=1            # i+=1 ile her seferinde i ye 1 eklenmesini sağlayarak 10 a kadar yazdırırız merhaba yı 
                    #fakat i yi her seferinde 1 arttırmak için gereken işlemi yazmazsak sonsuz döngü elde ederiz


username = ''

while not username:                                     # burda boş bir username tanımladık ve while döngüsüyle 
     username = input("Kullanıcı adınızı giriniz: ")    #username girilmediği sürece tekrar sormasını sağlayan bir dögü kurduk
    

print("Girdiğiniz kullanıcı adı: ",username)    


