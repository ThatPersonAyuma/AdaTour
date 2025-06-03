from . import lib
import time

def AdminMenu():
    while True:
        lib.clear_terminal()
        print("===========================================")
        print("||           DashBoard Customer          ||")
        print("===========================================")
        print("1. ")
        print("2. Paket Wisata")
        print("3. Jadwal Keberangkatan")
        print("4. Keluar")
        print("========================================")
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            JadwalKeberangkatan()
        elif pilihan == '2':
            PaketWisata()
        elif pilihan == '3':
            Pengaturan()
        elif pilihan == '4':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def JadwalKeberangkatan():
    
def PaketWisata():

def Pengaturan():    

