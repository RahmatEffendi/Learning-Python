#Program pertama ini adalah program yang berkaitan dengan dasar dari pada KUBUS
#kubus memiliki sisi-sisi yang sama panjang
#program sederhana kali ini akan menghitung dasar-dasar kubus antara lain:
#    - Luas kubus 
#            untuk luas kubus rumus nya adalah 
#               6 x sisi x sisi atau 6 x S X S

#    - Keliling kubus
#            untuk keliling kubus rumusnya adalah
#                12 x sisi atau 12 x S

#    - Volume kubus
#            untuk volume kubus rumusnya adalah
#                sisi x sisi x sisi atau S x S x S

#Pencarian untuk luas kubus
def luas():
    sisi = float(raw_input("Masukkan Salah Satu sisi dari kubus: "))
    #Hitung Luas nya
    luas = 6 * sisi * sisi
    print("Luas dari Kubus adalah %d" %luas)

def keliling():
    sisi = float(raw_input("Masukkan salah satu sisi dari kubus: "))
    #hitung keliling kubusnya
    keliling = 12 * sisi
    print("Keliling dari kubus adalah %d" %keliling)

def volume():
    sisi = float(raw_input("Masukkan salah satu sisi dari kubus: "))
    #hitung volume kubus
    volume = sisi * sisi * sisi
    print("Volume kubusnya adalah %d" %volume)


print ("Masukkan Pilihan Untuk Melakukan Pencarian Dasar Kubus ")
print ("Pilihannya antara lain: ")
print ("1. Luas Kubus")
print ("2. Keliling Kubus")
print ("3. Volume Kubus")
print ("")

masukkan = int(raw_input("Masukkan Pilihan: "))
if (masukkan == 1):
    luas()
elif (masukkan == 2):
    keliling()
elif(masukkan == 3):
    volume()
else:
    print("Masukkan Yang Anda Pilih Salah!")