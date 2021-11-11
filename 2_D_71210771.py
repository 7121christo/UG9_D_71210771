print("Menghitung Uang Saku Anak-anak")

UA1=float(input("\t Uang saku anak pertama : "))
UA2=float(input("\t Uang saku anak kedua : "))
UA3=float(input("\t Uang saku anak ketiga : "))

def rataratauangsaku(UA1, UA2, UA3):
    rata = (UA1+UA2+UA3)/3
    return rata
rata=rataratauangsaku (UA1, UA2, UA3)
print("\t Rata-rata dari ", UA1, "+", UA2, "+", UA3, "adalah", rata)
