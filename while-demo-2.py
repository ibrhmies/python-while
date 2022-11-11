# kullanıcıdan urun bilgilerini alıp dictionary tipinde listede saklayın
# ürün adedini kullanıcıdan alın ürün bilgileri (isim, fiyat)




i = 0
urunAdedi = int(input("Ürün adedini giriniz: "))

urunler = []


while i< urunAdedi:
    urunAdi = input("Ürün adını girniz: ")
    fiyat = int(input("ürün fiyatını giriniz: "))
    urunler.append({
        'name':urunAdi,'price':fiyat             
})
    i+=1
    print(urunler)
    

#-> dictionary tipinde bir liste oluşturacaksak döngüde 
# değerlerin o listeye girmesinde append komutunda {} le keyleri tanımlıyoruz  
# eğer birden fazla urun tanımlanıyorsa ürün bilgileri döngü içinde olmalı



