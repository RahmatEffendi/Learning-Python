#Program kedua ini berkaitan dengan bangun ruang BALOK
#pada program sederhana ini akan mengkalkulasikan pencarian dasar-dasar dari balok
#mulai dari luas balok, keliling, volume dan juga diagonal ruang

#untuk rumus atau formulanya antara lain:
#    1. Luas Permukaan Balok = 2 x {(pxl) + (pxt) + (lxt)}
#    2. Diagonal Ruang = Akar dari (p kuadrat + l kuadrat + t kuadrat)
#    3. Keliling Balok = 4 x (p + l + t)
#    4. Volume Balok = p x l x t (sama dengan kubus, tapi semua rusuk kubus sama panjang).

#creator by RahmatEffendi
import math


#Menghitung Luas Balok
def luas():
    panjang = float(raw_input("Masukkan Panjang Balok: "))
    lebar = float(raw_input("Masukkan Lebar Balok: "))
    tinggi = float(raw_input("Masukkan TInggi Balok: "))

    #kalukulasikan pada rumus
    luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    print("Luas Balok adalah %d" %luas)

#def diagonal(): 
#    panjang = float(raw_input("Masukkan Panjang Balok: "))
#    lebar = float(raw_input("Masukkan Lebar Balok: "))
#    tinggi = float(raw_input("Masukkan TInggi Balok: "))

#    #kalukulasikan pada rumus
#    diagonal = float(math.sqrt(panjang**2 + lebar**2 + tinggi**2))
#    print("Luas Balok adalah %d" %diagonal)

#Keliling Balok
def keliling():
    panjang = float(raw_input("Masukkan Panjang Balok: "))
    lebar = float(raw_input("Masukkan Lebar Balok: "))
    tinggi = float(raw_input("Masukkan TInggi Balok: "))

    #kalukulasikan pada rumus
    keliling = 4 * (panjang + lebar + tinggi)
    print("Keliling Balok adalah %d" %keliling)

#Volume balok
def volume():
    panjang = float(raw_input("Masukkan Panjang Balok: "))
    lebar = float(raw_input("Masukkan Lebar Balok: "))
    tinggi = float(raw_input("Masukkan TInggi Balok: "))

    #kalukulasikan pada rumus
    volume = panjang * lebar * tinggi
    print("Volume Balok adalah %d" %volume)

#Masukkan Pilihan
masukkan = int(raw_input("Masukkan Pilihan: "))
if(masukkan == 1):
    luas()
elif(masukkan == 2):
    keliling()
elif(masukkan == 3):
     volume()
else:
    print("Hava anice day")