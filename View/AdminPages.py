from ModelsControll import user, paket_wisata
from . import lib
import time

# Region Of Constanct Data
ADMIN: user.User
# End Of Constanct Data

def AdminChange(admin: user.User):
    global ADMIN
    ADMIN = admin

def AdminDasboard(admin: user.User):
    AdminChange(admin)
    lib.clear_terminal()
    text = "==============================================\n"
    text += f"||  Selamat datang di AdaTour, {ADMIN.username}!  ||\n"
    text += "=============================================="
    print(text)
    time.sleep(2)
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||              DashBoard             ||\n"
        text+="========================================\n"
        text+="1. Kelola Paket\n"
        text+="2. Kelola Akun\n"
        text+="3. Kelola Mitra\n"
        text+="4. Keluar\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            pass
        elif pilihan == '2':
            pass
        elif pilihan == '3':
            pass
        elif pilihan == '4':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def KelolaPaketPage():
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||        Kelola Paket Wisata         ||\n"
        text+= "========================================\n"
        text+="1. Lihat Paket\n"
        text+="2. Tambah Paket\n"
        text+="3. Rubah Paket\n"
        text+="4. Hapus Mitra\n"
        text+="5. Keluar\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")
        match pilihan:
            case '1':
                
                pass
            case '2':

                pass
            case '3':

                pass
            case '4':
                lib.clear_terminal()
                print("Terima kasih!")
                time.sleep(2)
                break
            case _:
                lib.clear_terminal()
                print("Pilihan tidak valid. Coba lagi.")
                time.sleep(2)

def LihatPaketWisata():
    pajetWisatas: list[paket_wisata.PaketWisata] = paket_wisata.PaketWisata.read_all()
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||        Daftar Paket Wisata         ||\n"
        text+= "========================================\n"
        text+="1. Lihat Paket\n"
        text+="2. Tambah Paket\n"
        text+="3. Rubah Paket\n"
        text+="4. Hapus Mitra\n"
        text+="5. Keluar\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")
        match pilihan:
            case '1':
                
                pass
            case '2':

                pass
            case '3':

                pass
            case '4':
                lib.clear_terminal()
                print("Terima kasih!")
                time.sleep(2)
                break
            case _:
                lib.clear_terminal()
                print("Pilihan tidak valid. Coba lagi.")
                time.sleep(2)
                
def TambahPaketWisata():
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||        Tambah Paket Wisata         ||\n"
        text+= "========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")
        match pilihan:
            case '1':
                
                pass
            case '2':

                pass
            case '3':

                pass
            case '4':
                lib.clear_terminal()
                print("Terima kasih!")
                time.sleep(2)
                break
            case _:
                lib.clear_terminal()
                print("Pilihan tidak valid. Coba lagi.")
                time.sleep(2)