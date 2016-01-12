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

#BELAH KETUPAT:
#   
#        luas : (diagonal 1 * diagonal 2) / 2
#        Keliling : 4 x sisi 

def keliling():
    sisi = int(raw_input("Masukkan Nilai Sisi: "))

    # Masukkan ke dalam rumus
    keliling = 4 * sisi
    #hasil
    print("Keliling Belah Ketupat adalah: %d" %keliling)

def luas():
    diagonal_1 = int(raw_input("Masukkan Nilai Sisi Diagonal 1: "))
    diagonal_2 = int(raw_input("Masukkan Nilai Sisi Diagonal 2: "))

    #masukkan ke dalam rumus
    luas = (diagonal_1 * diagonal_2) / 2

    #hasil
    print("Luas Belah Ketupat adalah: %d" %luas)

print"MENU PILIHAN"
print"============"
print"1. Keliling"
print"2. Luas"
print"3. Keluar"
print"============"
print""

masukkan = int(raw_input("masukkan menu: "))
if masukkan == 1:
    keliling()
elif masukkan == 2:
    luas()
else:
    print("Terima Kasih")





