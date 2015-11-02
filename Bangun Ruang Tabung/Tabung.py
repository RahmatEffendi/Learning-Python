#Program ketika ini adalah berkaitan dengan dasar Tabung
#pada tabung terdapat nilai konstanta yang telah bernilai yaitu phi 
#phi bernilai 3,14 atau 22/7

#Untuk tabung rumus dasar nya antara lain:
#    Volume = luas alas x tinggi, atau luas lingkaran x t
#    Luas = luas alas + luas tutup + luas selimut, atau ( 2 x ? x r x r) + ? x d x t)

# creator by RahmatEffendi

def volume():
    #Masukkan inputaan
    luasAlas = float(raw_input("Masukkan nilai dari Luas Alas Tabung: "))
    tinggi = float(raw_input("Masukkan nilai dari Tinggi Tabung: "))

    #kalkulasikan dengan rumus
    volume = luasAlas * tinggi
    #Munculkan Hasilnya
    print("Hasil dari volume tabung adalah %d" %volume)

#jika luas yang diketahui adalah luas alas, luas tutup, dan luas selimut
def luassatu():
    #Masukkan inputaan
    luasAlas = float(raw_input("Masukkan nilai dari Luas Alas Tabung: "))
    luasTutup = float(raw_input("Masukkan nilai dari Luas Tutup Tabung: "))
    luasSelimut = float(raw_input("Masukkkan nilai dari Luas Selimut Tabung :"))

    #kalkulasikan dengan rumus
    luas = luasAlas + luasTutup + luasSelimut
    #Munculkan Hasilnya
    print("Hasil dari volume tabung adalah %d" %luas)

def luasdua():
    #Masukkan inputaan
    jari = float(raw_input("Masukkan nilai dari Ruas/Jari2: "))
    diameter = float(raw_input("Masukkan nilai dari Diameter: "))
    tinggi = float(raw_input("Masukkan nilai dari Tinggi Tabung: "))
    phi = float(raw_input("Masukkan nilai phi = 3.14: "))
    

    #kalkulasikan dengan rumus
    luas = (2 * phi * jari * jari) + (phi * diameter * tinggi)
    #Munculkan Hasilnya
    print("Hasil dari volume tabung adalah %d" %luas)

print ("Masukkan Pilihan Untuk Melakukan Pencarian Dasar Tabung")
print ("Pilihannya antara lain: ")
print ("1. Volume")
print ("2. Luas 1")
print ("3. Luas 2")
print ("")
#Masukkan pilihan
masukan = int(raw_input("Masukkan Pilihan: "))
if(masukan == 1):
    volume()
elif(masukan ==2):
    luassatu()
elif(masukan == 3):
    luasdua()
else:
    print("Have a nice day")
    
