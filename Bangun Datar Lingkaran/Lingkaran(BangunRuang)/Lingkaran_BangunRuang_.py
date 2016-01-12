#Program Bangun Datar
#Program ini merupakan aplikasi dari pembelajaran yang sedang saya pelajari
#yaitu bahasa pemprograman python. Dan jika ada kesalahan logika atau algoritma dari program yang saya buat
#maka sekiranya meng-emailkan ke saya di rahmat480@gmail.com

#Tanggal 1/10/2016 7:24 AM WIB
#Atjeh, Indonesia
#Author Rahmat Effendi

#Program Bangun datar ini akan mencakup beberapa bangun datar, 
#dan kalkulasi yang dilakukan adalah perihal pencarian Keliling, Luas, dan Sisi.
#Bangun datar yang akan diaplikasikan adalah:
#    - Persegi
#    - Persegi Panjang
#    - Jajargenjang
#    - Trapesium
#    - Belah Ketupat
#    - Layang - layang
#    - Segitiga, dan
#    - Lingkaran

#LINGKARANG:
#   
#        luas : phi x r^2
#        Keliling : phi x diameter atau 2 x phi x r
#        Diameter : 2 x jari-jari

import math

def diameter():
    jari_jari = float(raw_input("Masukkan Nilai Jari-Jari: "))

    #masukkan rumus
    diameter = 2 * jari_jari
    #hasil
    print "Diameternya adalah %d: " %diameter

def keliling():
    
    diameter = float(raw_input("Masukkan Nilai Diameter: "))

    # Masukkan ke dalam rumus
    keliling = math.pi * diameter
    #hasil
    print("Keliling lingkaran adalah: %d" %keliling)

def luas():
    jari_jari = float(raw_input("Masukkan Nilai Jari-Jari: "))

    #masukkan ke dalam rumus
    luas = math.pi * jari_jari**2

    #hasil
    print("Luas Lingkaran adalah: %d" %luas)

print"MENU PILIHAN"
print"============"
print"1. Keliling"
print"2. Luas"
print"3. Diameter"
print""
print"============"
print""

masukkan = int(raw_input("masukkan menu: "))
if masukkan == 1:
    keliling()
elif masukkan == 2:
    luas()
elif masukkan == 3:
    diameter()
else:
    print("Terima Kasih")





