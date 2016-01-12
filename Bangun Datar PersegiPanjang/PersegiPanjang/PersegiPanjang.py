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

#PERSEGI PANJANG:
#    Persegi memiliki sisi yang sama panjang, untuk rumus persegi antara lain:
#        luas : panjang x lebar
#        Keliling : (2 x p) + (2 x l) atau 2 x (p + l) 

def keliling():
    panjang = float(raw_input("Masukkan Nilai Panjang: "))
    lebar = float(raw_input("Masukkan Nilai Lebar: "))

    # Masukkan ke dalam rumus
    keliling = (2 * panjang) + (2 * lebar)
    #hasil
    print("Keliling Persegi Panjang adalah: %d" %keliling)

def luas():
    panjang = float(raw_input("Masukkan Nilai Panjang: "))
    lebar = float(raw_input("Masukkan Nilai Lebar: "))

    #masukkan ke dalam rumus
    luas = panjang * lebar

    #hasil
    print("Luas Persegi Panjang adalah: %d" %luas)

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





