#ini merupakan program untuk bangun ruang kerucut
#Volume = 1/3 x ? x r x r x t
#Luas = luas alas + luas selimut

import math

def volume():
    jari_satu = float(input("Masukkan Jari Pertama: "))
    jari_dua = float(input("Masukkan Jari Kedua: "))
    tinggi = float(input("Masukkan Tinggi Kerucut: "))

    volume = 1/3 * math.pi * jari_satu * jari_dua * tinggi

    print ("Hasilnya adalah %d" %volume)

def luas():
    luas_alas = float(input("Masukkan Luas Alas: "))
    luas_selimut = float(input("Masukkan Luas Selimut: "))

    luas = luas_alas + luas_selimut

    print("Luas Kerucut adalah %d" %luas)

masukan = int(input("Masukkan no: "))
if masukan == 1:
    volume()
elif masukan == 2:
    luas()
else:
    print("program berhenti")
