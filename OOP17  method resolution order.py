class A:
    def show(self):
        print("ini adalah show A")

class B:

    def show(self):
        print("ini adalah show B")

class C(B, A): #walaupun method nya sama yaitu show(), kita akan menginherit yg urutan sesuai penyebut di class C nya
    pass

objek = C()

#help(objek)
objek.show()
objek.show()


