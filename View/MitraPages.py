from . import lib
import time

def MitraMenu():
    while True:
        lib.clear_terminal()
        text += "============================================\n"
        text += "||             DashBoard Mitra            ||\n"
        text += "============================================\n"
        text += "1. kelola tarif\n"
        text += "2. Pesanan\n"
        text += "3. Pengaturan\n"
        text += "4. Keluar"
        text += "===========================================\n"
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            KelolaTarif()
        elif pilihan == '2':
            Pesanan()
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

def KelolaTarif():
    while True:
        lib.clear_terminal()
        text += "===============================================\n"
        text += "||                Kelola Tarif               ||\n"
        text += "===============================================\n"
        text += "1. ubah tarif\n"
        text += "2. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (1 dan 2): ")

        if pilihan == '1':
            UbahTarif()
        elif pilihan == '2':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def UbahTarif():
    while True:
        lib.clear_terminal()
        text += "====================================================\n"
        text += "||                  Ubah Tarif                    ||\n"
        text += "====================================================\n"
        #text += f" tarif yang anda beri sekarang adalah {Tarif_paket},\n"
        text += "====================================================\n"
        print(text)
        pilihan = input("Masukan nominal yang ingin anda masukkan: ")
        
    # if tarif in Harga_paket:
    #     lib.clear_terminal()
    #     print("Tarif tidak boleh sama")
    #     time.sleep(2)
    # else:
    #     lib.clear_terminal()
    #     print("Tarif berhasil diganti")
    #     time.sleep(2)

def Pesanan():
    while True:
        lib.clear_terminal()
        text += "===================================================\n"
        text += "||                  Menu Pesanan                 ||\n"
        text += "===================================================\n"
        text += "1. Daftar Customer yang memesan\n"
        text += "0. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (0-2) untuk keluar: ")
        
        if pilihan == '1':
            DaftarPemesanan()
        elif pilihan == '0':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def DaftarPemesanan():
    while True:
        lib.clear_terminal()
        text += "===============================================================\n"
        text += "||                       Daftar Pesanan                      ||\n"
        text += "===============================================================\n"
        #text += f"{Customer} telah memesan, pelanggan memesan pada\n
        #         Tanggal {Tanggal_pesanan} dengan kendaraan {Transport_Units} "
        #text += f"status Pembayaran {StatusPayment}\n"
        text += "0. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan(0) untuk keluar: ")

        if pilihan == '0':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)


def Pengaturan():
    while True:
        lib.clear_terminal()
        text += "============================================\n"
        text += "||               Pengaturan               ||\n"
        text += "============================================\n"
        # text += f" Hai {Username}! Semoga Harimu Baik :)\n"
        text += "============================================\n"
        text += "1. Ubah Username\n"
        text += "2. Ubah Password\n"
        text += "3. Hapus Akun\n"
        text += "4. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (1-3): ")

        if pilihan == '1':
            UbahUsername()
        elif pilihan == '2':
            UbahPassword()
        elif pilihan == '3':
            HapusAkun()
        elif pilihan == '4':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def UbahUsername():
    lib.clear_terminal()
    text += "===============================================\n"
    text += "||               Ubah Username               ||\n"
    text += "===============================================\n"
    print(text)
    input("Ubah Username: ")

    # if username in users:
    #     lib.clear_terminal()
    #     print("Username sudah ada")
    #     time.sleep(2)
    # else:
    #     lib.clear_terminal()
    #     print("Username berhasil diganti")
    #     time.sleep(2)

def UbahPassword():
    lib.clear_terminal()
    text += "===============================================\n"
    text += "||               Ubah Password               ||\n"
    text += "===============================================\n"
    print(text)
    input("Ubah Password: ")

    
    # if password == password:
    #     lib.clear_terminal()
    #     print("Password masih sama, silakan ganti yang baru")
    #     time.sleep(2)
    # else:
    #     lib.clear_terminal()
    #     print("Password berhasil diganti")
    #     time.sleep(2)


def HapusAkun():
    while True:
        lib.clear_terminal()
        text += "==========================================================\n"
        text += "||                     Hapus Akun                       ||\n"
        text += "==========================================================\n"
        # text += f" Hai {Username}! apakah kau yakin menghapus akun mu? :[\n"
        text += "==========================================================\n"
        text += "1. Ya\n"
        text += "2. Tidak\n"
        text += "==========================================================\n"
        print(text)
        pilihan = input("Masukan inputan (1 dan 2): ")

        if pilihan == '1':
            print("delete")
        elif pilihan == '2':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)