#Öğrenci Kayıt Ekleme
liste = ["Sametcan Sari", "Mikail Yazar", "Mehmet Kaya"]
def ogrenci_ekleme():
  ad_soyad=input("Eklemek istediğiniz öğrencinin adi-soyadi: ")
  liste.append(ad_soyad)
  print(f"{ad_soyad} başarıyla listeye eklenmiştir.")
def ogrenci_cikarma():
  ad_soyad=input("Çıkarmak istediğiniz öğrencinin adı-soyadı: ")
  liste.remove(ad_soyad)
  print(f"{ad_soyad} başariyla listeden çikarilmiştir.")
def ogrencileri_ekleme():
  ögrenci_sayisi=int(input("Eklemek istediğiniz öğrenci sayisini giriniz: "))
  i=0
  while i<ögrenci_sayisi:
    ad_soyad=input(f"Eklemek istediğiniz {i+1}. öğrencinin adi-soyadı: ")
    liste.append(ad_soyad)
    i=i+1
  print("Öğrenciler başarıyla eklenmiştir.")
def liste_goruntuleme():
  print(liste)
def numara_gosterme():
  ad_soyad=input("Numarasini istediğiniz öğrencinin adi-soyadi: ")
  if (ad_soyad in liste):
    numara= liste.index(ad_soyad)
    print(f"Öğrencinin numarasi: {numara}")
  else:
    print("Öğrenci listede bulunmamaktadır.")
print("ÖĞRENCİ KAYIT SİSTEMİNE HOŞGELDİNİZ")
print("Kayit Sisteminde Yapilabilecek İşlemler")
print("1-Öğrenci Ekleme")
print("2-Öğrenci Çikarma")
print("3-Birden Fazla Öğrenci Ekleme")
print("4-Öğrenci Listesini Görüntüleme")
print("5-Öğrenci Numarasi Gösterme")
print("Not:Yapacağiniz İşlemler Bitince Çikmak İçin 6'ya basiniz.")
sayi=int(input("Yapacağiniz işlemin numarasini giriniz: "))
while sayi<6:
  if sayi==1:
    ogrenci_ekleme()
  elif sayi==2:
    ogrenci_cikarma()
  elif sayi==3:
    ogrencileri_ekleme()
  elif sayi==4:
    liste_goruntuleme()
  elif sayi==5:
    numara_gosterme()
else:
  print("Girdiğiniz numara hatalı. Tekrar giriniz.")