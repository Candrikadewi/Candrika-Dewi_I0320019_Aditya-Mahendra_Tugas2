#manampilkan informasi program
print("Luas Persegi Panjang")

#input nilai panjang
p = float(input("Masukkan panjang persegi panjang: "))

#input nilai lebar
l = float(input("Masukkan lebar persegi panjang: "))

#menghitung luas persegi panjang
Luas_persegi_panjang = p * l

#menampilkan hasil perhitungan
print("Luas Persegi Panjang:", Luas_persegi_panjang, "persegi")

#Menampilkan informasi program
print("Luas Lingkaran")

#Memasukkan nilai diameter
diameter = float(input("Masukkan nilai diameter: "))

#Menghitung luas lingkaran
luas_lingkaran = 0.25 * 3.14 * diameter * diameter

#Menampilkan hasil perhitungan ke layar
print("Luas Lingakaran:" , luas_lingkaran,"persegi")

#Menampilkan informasi program
print("Luas Kubus")

#Memasukkan nilai sisi kubus
sisi = float(input("Masukkan nilai sisi kubus: "))

#Menghitung luas kubus
luas_kubus = sisi ** 2

#Menampilkan hasil perhitungan ke layar
print("Luas Kubus:", luas_kubus, "persegi")

#Menampilkan informasi program
print("Konversi suhu Celcius ke Fahrenheit")

#Memasukkan suhu dalam Celcius
C = float(input("Masukkan nilai suhu(celcius): "))

#konversi suhu ke fahrenheit
F = ((9 /5 ) * C) + 32

#menampilkan hasil konversi ke layar
print("Celcius: ", C)
print("Fahrenheit: ", F)

#Menampilkan Informasi Program
print("Konversi suhu Reamur ke Kelvin")

#Memasukkan nilai Reamur
R = float(input("Masukkan nilai suhu (Reamur): "))

#Konversi ke Kelvin
K = (4 / 5 * R) + 273

#Menampilkan hasil perhitungan ke layar
print("Reamur:", R)
print("Kelvin:", K)
