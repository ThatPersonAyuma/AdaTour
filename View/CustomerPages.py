from . import lib
import time

def AdminMenu():
    while True:
        lib.clear_terminal()
        print("===========================================")
        print("||           DashBoard Customer          ||")
        print("===========================================")
        print("1. Paket Wisata")
        print("2. Jadwal Keberangkatan")
        print("3. Keluar")
        print("========================================")
        pilihan = input("Masukan inputan (1-3): ")

        if pilihan == '1':
            PaketWisata()
        elif pilihan == '2':
            JadwalKeberangkatan()
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

def PaketWisata():
    while True:
        lib.clear_terminal()
        text += "============================================\n"
        text += "||              Paket Wisata              ||\n"
        text += "============================================\n"
        text += "1. Pilih Paket\n"
        text += "0. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (0 dan 1): ")

        if pilihan == '1':
            PilihPaket()
        elif pilihan == '0':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def PilihPaket():
    while True:
        lib.clear_terminal()
        text += "===============================================\n"
        text += "||              Pemilihan paket              ||\n"
        text += "===============================================\n"
        text += "1. Paket 1 {Destinasi}\n"
        text += "0. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (0-2): ")

        if pilihan == '1':
            paket1()
        elif pilihan == '0':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def paket1():
    while True:
        lib.clear_terminal()
        text += "===============================================\n"
        text += "||                  paket 1                  ||\n"
        text += "===============================================\n"
        text += "Destinasinya nanti akan ke {Destinasi}\n"
        text += "Kendaraan yang dipakai {kendaraan} kapasitas maksimal untuk {KapasitasKendaraan} orang\n"
        text += "Harga tarif untuk paket 1, sebesar {Tarif}\n"
        text += "1. Beli Tiket\n"
        text += "0. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (0 dan 1): ")

        if pilihan == '1':
            BeliTiket()
        elif pilihan == '0':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
        
def BeliTiket():
    while True:
        lib.clear_terminal()
        text += "================================================\n"
        text += "||                  Pembelian                  ||\n"
        text += "================================================\n"
        text += "Harga tarif yang harus dibayar adalah sebesar {Tarif}\n"
        text += "1. Bayar\n"
        text += "0. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (0 dan 1): ")

        if pilihan == '1':
            lib.clear_terminal()
            print("pembayaran berhasil! silahkan tunggu konfirmasi :D")
            time.sleep(2)
        elif pilihan == '0':
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
    
def JadwalKeberangkatan():
    while True:
        lib.clear_terminal()
        text += "========================================================\n"
        text += "||                Jadwal Keberangkatan                ||\n"
        text += "========================================================\n"
        # text += f"Anda akan berangkat pada tanggal adalah {Tanggal_Keberangkatan}\n"
        # text += f"Tour Guide anda nanti adalah {Nama_TourGuide}\n"
        # text += f"Status Jadwal {Status_kesiapan}\n"    #Siap atau Tidak
        text += "0. Keluar\n"
        text += "===========================================\n"
        print(text)
        pilihan = input("Masukan inputan (1-3): ")

        if pilihan == '1':
            UbahUsername()
        elif pilihan == '0':
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