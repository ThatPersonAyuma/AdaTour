from . import lib
import time
from Controllers import *
from Models import *
from View import auth
import json

# Start Region of CONSTANT DATA
CONNECTION_STRING: str
try:
    with open('appsettings.json', 'r') as f:
        config = json.load(f)
        CONNECTION_STRING = config["ConnectionStrings"]["DefaultConnection"]
except:
    raise "Check appsettings.json"

users = {}

def FirstStepMenu():
    while True:
        lib.clear_terminal()
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
        text += "=============================================="
        text += "||                Menu Login                ||"
        text += "=============================================="
        print(text)
        username = input("Masukan username: ")
        password = input("Masukan password: ")

        if username in users and users[username] == password:
            lib.clear_terminal()
            text += "=============================================="
            text += f"||  Selamat datang di AdaTour, {username}!  ||"
            text += "=============================================="
            print(text)
            time.sleep(2)
            lib.clear_terminal()
            lib.DashBoard()
        else:
            lib.clear_terminal()
            print("Login gagal. Username atau password salah.")
            time.sleep(2)

def MenuRegistrasi():
    while True:
        lib.clear_terminal()
        text += "==============================================="
        text += "||              Menu Registrasi              ||"
        text += "==============================================="
        text += "1. Register untuk pelanggan"
        text += "2. Register untuk Tourguide"
        text += "3. Log in (bila anda sudah mempunyai akun)"
        text += "4. Keluar"
        text += "==============================================="
        print(text)
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            RegistrasiCustomer()
        elif pilihan == '2':
            RegistrasiTourGuide()
        elif pilihan == '3':
            FirstStepMenu()
        elif pilihan == '4':
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
    text += "========================================"
    text += "||        Registrasi Pelanggan        ||"
    text += "========================================"
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

def RegistrasiTourGuide():
    lib.clear_terminal()
    text += "========================================="
    text += "||         Registrasi TourGuide        ||"
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
