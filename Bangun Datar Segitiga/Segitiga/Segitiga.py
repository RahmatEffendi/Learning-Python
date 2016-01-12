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

#SEGITIGA:
#   
#        luas : (alas x tinggi) / 2
#        Keliling : sisi 1 + sisi 2 + sisi 3

def keliling():
    
    sisi_1 = int(raw_input("Masukkan Nilai Sisi 1: "))
    sisi_2 = int(raw_input("Masukkan Nilai Sisi 2: "))
    sisi_3 = int(raw_input("Masukkan Nilai Sisi 3: "))

    # Masukkan ke dalam rumus
    keliling = sisi_1 + sisi_2 + sisi_3
    #hasil
    print("Keliling Segitiga adalah: %d" %keliling)

def luas():
    alas = int(raw_input("Masukkan Nilai Alas: "))
    tinggi = int(raw_input("Masukkan Nilai Tinggi: "))

    #masukkan ke dalam rumus
    luas = (alas * tinggi) / 2

    #hasil
    print("Luas Segitiga adalah: %d" %luas)

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





