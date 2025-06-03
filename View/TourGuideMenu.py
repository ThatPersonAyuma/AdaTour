from . import lib
import time

def TourguideMenu():
    while True:
        lib.clear_terminal()
        text += "============================================\n"
        text += "||           DashBoard TourGuide          ||\n"
        text += "============================================\n"
        text += "1. Jadwal Kerja\n"
        text += "2. Pengaturan\n"
        text += "3. Keluar\n"
        text += "===========================================\n"
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            JadwalKerja()
        elif pilihan == '2':
            Pengaturan()
        elif pilihan == '3':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def JadwalKerja():
    while True:
        lib.clear_terminal()
        text += "============================================\n"
        text += "||              Jadwal Kerja              ||\n"
        text += "============================================\n"
        text += "1. Jadwal wisata\n"
        text += "2. Tanggal ketersediaan\n"
        text += "3. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (1-3): ")

        if pilihan == '1':
            JadwalKerja()
        elif pilihan == '2':
            TanggalKetersediaan()
        elif pilihan == '3':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def JadwalWisata():
    while True:
        lib.clear_terminal()
        text += "=============================================\n"
        text += "||              Jadwal Wisata              ||\n"
        text += "=============================================\n"
        #text += f" Anda akan berangkat pada tanggal {jadwal_keberangkatan}\n"
        #text += f" Mitra yang Digunakan {Nama_Mitra}\n"
        #text += f" Lokasi yang akan anda kunjungi bersama pelanggan {Lokasi_Wisata}\n"
        text += "0. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (0) untuk keluar: ")
        
        if pilihan == '0':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def TanggalKetersediaan():
    while True:
        lib.clear_terminal()
        text += "===================================================\n"
        text += "||              Jadwal Ketersediaan              ||\n"
        text += "===================================================\n"
        # text += f" Jadwal Aktif anda {Jadwal_Aktif}"  # {20-12-2025 - 20-04-2026}
        text += "1. Ubah Jadwal\n"
        text += "0. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (0) untuk keluar: ")
        
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