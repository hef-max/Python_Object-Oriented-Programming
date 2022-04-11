class Mangga:

    #magic method
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

    def __repr__(self):
        return "debug - Mangga : {} dengan jumlah : {} dan harganya : {}".format(self.nama, self.jumlah, self.harga)

    def __str__(self):
        return "Mangga : {} dengan jumlah : {} dan harganya : {}".format(self.nama, self.jumlah, self.harga)

    #biasa digunakan dengan aritmatika
    def __add__(self, object):
        return "jumlah buah yang dibeli : {} dengan harga : {}k".format(self.jumlah + object.jumlah, self.harga + object.harga)

    @property
    def __dict__(self):
        return "object ini mempunyai nama, jumlah dan harga"





belanja = Mangga("arumanis", 5, 15)
belanja2 = Mangga("manalagi", 10, 20)

print(repr(belanja))
print(belanja2)
print(belanja + belanja2)
print(belanja.__dict__)