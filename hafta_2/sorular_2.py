class Human:
    def __init__(self, isim: str, yas: int, cinsiyet: str):
        self.isim = isim
        self.__yas = yas
        self.cinsiyet = cinsiyet

    def get_yas(self):
        return self.__yas

    def set_yas(self, yas):
        self.__yas = yas

    def bilgi_ver(self):
        print(self.isim, self.get_yas(), self.cinsiyet)

class Hoca(Human):
    def __init__(self, isim, yas, cinsiyet, brans: str):
        super().__init__(isim, yas, cinsiyet)
        self.brans = brans

    def konus(self):
        print("{} adlı hoca {} dersini anlatıyor".format(self.isim, self.brans))


class Ogrenci(Human):
    def __init__(self, isim, yas, cinsiyet, sinif: str, okul_no: int):
        super().__init__(isim, yas, cinsiyet)
        self.sinif = sinif
        self.__okul_no = okul_no

    def get_okul_no(self):
        return self.__okul_no

    def set_okul_no(self, okul_no):
        self.__okul_no = okul_no

    def katil(self):
        print("{} adlı öprenci {} sinifinda derse katılıyor.".format(self.isim, self.sinif))

    def konus(self):
        print("{} adlı öğrenci {} yaşında ve okul numarası: {}".format(self.isim, self.get_yas(), self.get_okul_no()))


human1 = Human("Mirza", 19, "erkek")
hoca1 = Hoca("Sinan", 23,"erkek", "Veri Bilimine Giriş")
ogrenci1 = Ogrenci("İsa", 20, "erkek", "BIL501", 321312321321)

print("*********************************************************************************")

human1.bilgi_ver()
hoca1.bilgi_ver()
ogrenci1.bilgi_ver()

print("*********************************************************************************")

hoca1.konus()

print("*********************************************************************************")

ogrenci1.katil()
ogrenci1.set_okul_no(1010101010)
ogrenci1.set_yas(39)
ogrenci1.konus()

print("*********************************************************************************")