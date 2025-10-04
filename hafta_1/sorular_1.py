class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileri_yazdir(self):
        print(f"Marka: {self.marka}, Model: {self.model}")

# Kullanım
araba1 = Araba("Mercedes", "C200")
araba1.bilgileri_yazdir()

#*********************************************************************************************************************************

class Dikdortgen:
    def __init__(self, yukseklik, genislik):
        self.yukseklik = yukseklik
        self.genislik = genislik

    def alan_hesap(self):
        return self.yukseklik * self.genislik

#Kullanım
dikdortgen = Dikdortgen(200, 400)
print(dikdortgen.alan_hesap())
alan = dikdortgen.alan_hesap()
print(alan)

#*********************************************************************************************************************************

class Square:
    def __init__(self, x):
        self.x = x

    def draw_square(self):
        for i in range(self.x):
            print("*" * self.x)

#Kullanım
square = Square(5)
square.draw_square()

#*********************************************************************************************************************************

class Calculator:
    def topla(self, x, y, z=None):
        if z is not None:
            return x + y + z
        else:
            return x + y

#Kullanım
hesap = Calculator()
sonuc = hesap.topla(5, 8)
print(sonuc)
sonuc2 = hesap.topla(2, 3, 97)
print(sonuc2)

#*********************************************************************************************************************************

class Merhaba:
    def merhaba_yaz(self):
        print("Merhaba")

#Kullanım
merhaba = Merhaba()
merhaba.merhaba_yaz()

#*********************************************************************************************************************************



















