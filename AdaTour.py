import os
import time

from Controllers import *
from Models import *
from View import auth
import json



users = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def FirstStepMenu():
    while True:
        clear()
        text = "===============================================\n"
        text+="||                 Menu Awal                 ||\n"
        text+="===============================================\n"
        text+="1. Login\n"
        text+="2. Registtext+=bila anda belum mempunyai aku\n"
        text+="3. Keluar\n"
        text+="==============================================="
        print(text)
        pilihan = input("Masukan inputan (1-3): ")

        if pilihan == '1':
            login()
        elif pilihan == '2':
            MenuRegistrasi()
        elif pilihan == '3':
            clear()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            clear()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def login():
    clear()
    print("==============================================")
    print("||                Menu Login                ||")
    print("==============================================")
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    if username in users and users[username] == password:
        clear()
        print("==============================================")
        print(f"||  Selamat datang di AdaTour, {username}!  ||")
        print("==============================================")
        time.sleep(2)
        clear()
        DashBoard()
    else:
        clear()
        print("Login gagal. Username atau password salah.")
        time.sleep(2)

def MenuRegistrasi():
    while True:
        clear()
        print("===============================================")
        print("||              Menu Registrasi              ||")
        print("===============================================")
        print("1. Register untuk pelanggan")
        print("2. Register untuk Tourguide")
        print("3. Log in (bila anda sudah mempunyai akun)")
        print("4. Keluar")
        print("===============================================")
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            RegistrasiCustomer()
        elif pilihan == '2':
            RegistrasiTourGuide()
        elif pilihan == '3':
            FirstStepMenu()
        elif pilihan == '4':
            clear()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            clear()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def RegistrasiCustomer():
    clear()
    print("========================================")
    print("||        Registrasi Pelanggan        ||")
    print("========================================")
    username = input("Buat username: ")

    if username in users:
        clear()
        print("Username sudah ada")
        time.sleep(2)
    else:
        password = input("Buat password: ")
        users[username] = password

        clear()
        print("Registrasi berhasil. Silakan login.")
        time.sleep(2)

def RegistrasiTourGuide():
    clear()
    print("=========================================")
    print("||         Registrasi TourGuide        ||")
    print("=========================================")
    username = input("Buat username: ")

    if username in users:
        clear()
        print("Username sudah ada")
        time.sleep(2)
    else:
        password = input("Buat password: ")
        users[username] = password
        clear()
        print("Registrasi berhasil. Silakan login.")
        time.sleep(2)

def DashBoard():
    clear()
    while True:
        text = "========================================\n"
        text+="||              DashBoard             ||\n"
        text+="========================================\n"
        print("1. ")
        print("2. ")
        print("3. ")
        print("4. Keluar")
        print("========================================")
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            none()
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

def none():
    print("isi dulu lee")

# FirstStepMenu()
# lib.CreateUserTable()
# # wisatawan.create_wisatawan(name="Bayu", email="123abc")
wisatawan.read_wisatawan()