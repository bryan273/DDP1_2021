#mengimport nilai pi dari modul math
from math import pi

#menerima input dari user dalam bentuk float
radius = float(input("Masukkan radius lingkaran: "))

#menentukan formula luas area merah , kuning , dan ungu , dengan catatan r = radius
#luas merah didapatkan dengan mengurangi luas persegi dengan luas lingkaran ((2r)^2 - pi*(r^2))
#luas kuning didapatkan dengan menghitung luas lingkaran dikurangi luas segitiga (pi*(r^2) - (1/2*2r*r))
#luas ungu didapatkan dengan menghitung luas segitiga (1/2 * 2r * r)
luas_merah = 4*(radius**2) - pi*(radius**2)
luas_kuning = pi*(radius**2) - (radius**2)
luas_ungu = radius**2

#print luas daerah masing masing area , dengan membulatkan nilai menjadi 2 angka dibelakang koma
#dengan menggunakan formatting string
print("Luas daerah cat merah:","%.2f"%luas_merah)
print("Luas daerah cat kuning:","%.2f"%luas_kuning)
print("Luas daerah cat ungu:","%.2f"%luas_ungu)
