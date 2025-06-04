from . import lib
import time

def AdminMenu():
    while True:
        lib.clear_terminal()
        print("========================================")
        print("||           DashBoard Admin          ||")
        print("========================================")
        print("1. ")
        print("2. ")
        print("3. ")
        print("4. Keluar")
        print("========================================")
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            
        elif pilihan == '2':
            none()
        elif pilihan == '3':
            none()
        elif pilihan == '4':
            clear()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            clear()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def 

