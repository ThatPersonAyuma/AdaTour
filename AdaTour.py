from View import AdminPages, lib
import time
from Controllers import *
from ModelsControll import *
from View import auth
import json

def FirstStepMenu(): 
    while True:
        lib.clear_terminal()
        text ="===============================================\n"
        text+="||                 Menu Awal                 ||\n"
        text+="===============================================\n"
        text+="1. Login\n"
        text+="2. Registrasi (bila anda belum mempunyai aku)\n"
        text+="3. Keluar\n"
        text+="==============================================="
        print(text)
        pilihan = input("Masukan inputan (1-3): ")

        if pilihan == '1':
            login()
        elif pilihan == '2':
            MenuRegistrasi()
        elif pilihan == '3':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def login():
    while True:
        lib.clear_terminal()
        text = "==============================================\n"
        text += "||                Menu Login                ||\n"
        text += "=============================================="
        print(text)
        username = input("Masukan username: ")
        password = input("Masukan password: ")
        authResult = user.User.user_auth(username=username, password=password)
        if (len(authResult) == 1):
            match authResult[0].jenis_role :
                case "Administrator":
                    print("Welcome Admin")
                    input()
                    AdminPages.AdminDasboard(authResult[0])
                case "Pemandu":
                    print("Welcome Pemandu")
                    input()
                    # DashBoardWisatawan()
                case "Wisatawan":
                    print("Welcome Wisatawan")
                    input()
                    # DashBoardWisatawan()
                case _:
                    raise "Jenis Role Tidak Diketahui silakan cek database"    
        else:
            lib.clear_terminal()
            print("Login gagal. Username atau password salah.")
            time.sleep(2)

    # if username in users and users[username] == password:
    # lib.clear_terminal()
    # text = "==============================================\n"
    # text += f"||  Selamat datang di AdaTour, {username}!  ||\n"
    # text += "=============================================="
    # print(text)
    # time.sleep(2)
    # lib.clear_terminal()
    # # DashBoard()
    # DashBoardAdmin()
    

def MenuRegistrasi():
    while True:
        lib.clear_terminal()
        text = "===============================================\n"
        text += "||              Menu Registrasi              ||\n"
        text += "===============================================\n"
        text += "1. Register untuk pelanggan\n"
        text += "2. Log in (bila anda sudah mempunyai akun)\n"
        text += "3. Keluar\n"
        text += "==============================================="
        print(text)
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            RegistrasiCustomer()
        elif pilihan == '2':
            RegistrasiTourGuide()
        elif pilihan == '3':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def RegistrasiCustomer():
    lib.clear_terminal()
    text = "========================================\n"
    text += "||        Registrasi Pelanggan        ||\n"
    text += "========================================"
    print(text)
    username = input("Buat username: ")

    if user.User.IsUserExist(username):
        lib.clear_terminal()
        print("Username sudah ada")
        time.sleep(2)
    else:
        role: any# Bikin logika buat cari role di sini
        password = input("Buat password: ")

        # Buat user masukin data dulu, Id_Role nanti ajah
        # Habis buat langsung login ajah
        # user.User.create(
        #     id_role = ,
        #     username = ,
        #     password = ,
        #     nama_lengkap = ,
        #     kontak = ,
        #     alamat = 
        # )
        lib.clear_terminal()
        print("Registrasi berhasil. Silakan login.")
        time.sleep(2)

def RegistrasiTourGuide():
    lib.clear_terminal()
    text = "=========================================\n"
    text += "||         Registrasi TourGuide        ||\n"
    text += "========================================="
    print(text)
    username = input("Buat username: ")

    if username in users:
        lib.clear_terminal()
        print("Username sudah ada")
        time.sleep(2)
    else:
        password = input("Buat password: ")
        users[username] = password
        lib.clear_terminal()
        print("Registrasi berhasil. Silakan login.")
        time.sleep(2)

# def DashBoardAdmin():
#     lib.clear_terminal()
#     while True:
#         text = "========================================\n"
#         text+="||              DashBoard             ||\n"
#         text+="========================================\n"
#         print("1. Kelola Paket")
#         print("2. Kelola Akun")
#         print("3. Kelola Mitra")
#         print("4. Keluar")
#         print("========================================")
#         pilihan = input("Masukan inputan (1-4): ")

#         if pilihan == '1':
#             none()
#         elif pilihan == '2':
#             none()
#         elif pilihan == '3':
#             none()
#         elif pilihan == '4':
#             lib.clear_terminal()
#             print("Terima kasih!")
#             time.sleep(2)
#             break
#         else:
#             lib.clear_terminal()
#             print("Pilihan tidak valid. Coba lagi.")
#             time.sleep(2)



def none():
    pass
    print("isi dulu lee")

FirstStepMenu()
# lib.CreateUserTable()
# # wisatawan.create_wisatawan(name="Bayu", email="123abc")
