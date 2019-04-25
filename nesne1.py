"""class Calisan():
    print("Yeni bir class oluşturuldu")
    unvan="Personel"
    mesai="9-18"
    def __init__(self): #Sürekli değişen özellikleri bu fonk. içerisine yazarız
        print("Yeni bir calisan olusturuldu")
        self.yetenekler=[]
        self.maas=1600
        self.gunsayisi=0
    def çalış(self):
    self.gunsayisi+=1
    ahmet= Calisan()
        ahmet.yetenekler.append("Python biliyor")
        ahmet.maas=1700
        print("selam")
        print(ahmet.maas)"""""


class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))
