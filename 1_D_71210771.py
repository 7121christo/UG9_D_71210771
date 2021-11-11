print("Menghitung Luas Layang-layang")

d1=float(input("\t Masukkan d1: "))
d2=float(input("\t Masukkan d2: "))

def luaslayanglayang(d1, d2):
    luas = (d1*d2)/2
    return luas
luas=luaslayanglayang (d1, d2)
print("\t Luas Layang-layang = ", luas, "cm")
