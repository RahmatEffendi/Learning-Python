#Bangun Ruang Limas
#Volume = 1/3 luas alas tinggi sisi
#Luas = luas alas + jumlah luas sisi tegak

def volume():
    luas_alas = float(input("Masukkan Luas Alas: "))
    tinggi = float(input("Masukkan Tinggi Limas: "))
    sisi = float(input("Masukkan Sisi Limas: "))

    volume = 1/3 * luas_alas * tinggi * sisi

    print ("Volume Limas adalah %d" %volume)

def luas():
    luas_alas = float(input("Masukkan Luas Alas: "))
    jumlah_sisi_tegak = float(input("Masukkan Jumlah Sisi Tegak: "))

    luas = luas_alas + jumlah_sisi_tegak

    print("Luas Limas adalah %d" %luas)

def menu():
    print("Masukkan Nomor dibawah untuk menggunakan aplikasi")
    print("1. Volume Limas")
    print("2. Luas Limas")
    masukan = int(input("Masukka No: "))
    return masukan

loop = 1
masuk = 0
while loop >= 1:
    masuk = menu()
    if masuk == 1:
        volume()
    elif masuk == 2:
        loop = 0
print('Semoga Menyenangkan')
