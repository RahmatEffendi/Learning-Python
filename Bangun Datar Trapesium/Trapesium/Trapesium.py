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

#TRAPESIUM:
#  
#        luas : (sisi 1 + sisi 3) x t / 2
#        Keliling : sisi 1 + sisi 2 + sisi 3 + sisi 4

def keliling():
    sisi_1 = float(raw_input("Masukkan Nilai Sisi 1: "))
    sisi_2 = float(raw_input("Masukkan Nilai Sisi 2: "))
    sisi_3 = float(raw_input("Masukkan Nilai Sisi 3: "))
    sisi_4 = float(raw_input("Masukkan Nilai Sisi 4: "))

    # Masukkan ke dalam rumus
    keliling = sisi_1 + sisi_2 + sisi_3 + sisi_4
    #hasil
    print("Keliling Trapesium adalah: %d" %keliling)

def luas():
    sisi_1 = float(raw_input("Masukkan Nilai Sisi 1: "))
    sisi_3 = float(raw_input("Masukkan Nilai Sisi 3: "))
    tinggi = float(raw_input("Masukkan Nilai Tinggi: "))

    #masukkan ke dalam rumus
    luas = (sisi_1 + sisi_3) * tinggi / 2

    #hasil
    print("Luas Trapesium adalah: %d" %luas)

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





