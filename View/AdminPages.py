from ModelsControll import user, paket_wisata, roles
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
            KelolaPaketPage()
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
        text+="4. Hapus Paket\n"
        text+="5. Keluar\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")
        match pilihan:
            case '1':
                LihatPaketWisata()
                pass
            case '2':
                TambahPaketWisata()
                return None
            case '3':
                UpdatePaketWisataPage()
                pass
            case '4':
                HapusPaketWisata()
            case _:
                lib.clear_terminal()
                print("Pilihan tidak valid. Coba lagi.")
                time.sleep(2)

def LihatPaketWisata():
    paketWisatas: list[paket_wisata.PaketWisata] = paket_wisata.PaketWisata.read_all()
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||        Daftar Paket Wisata         ||\n"
        text+= "========================================\n"
        for index, pW in enumerate(paketWisatas):
            text+= f"{index+1}. {pW.nama}\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan sesuai angka untuk melihat detail atau '0' untuk kembali: ")
        if (pilihan.isdigit()):
            pilihan = int(pilihan)
            if (pilihan == 0):
                lib.clear_terminal()
                print("Terima kasih!")
                time.sleep(2)
                return None
            elif (pilihan >= 0 and pilihan <= len(paketWisatas)):
                PaketDetailPages(paketWisatas[pilihan-1])
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
                
def PaketDetailPages(paketWisata: paket_wisata.PaketWisata):
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||        Detail Paket Wisata         ||\n"
        text+= "========================================\n"
        text+=f"Nama\t : {paketWisata.nama}\nId Paket : {paketWisata.id_paket}\nDeskripsi: {paketWisata.deskripsi}\nDurasi\t : {paketWisata.durasi_hari}\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan '0' untuk kembali: ")  
        if (pilihan == '0'):
            return None              

def TambahPaketWisata():
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||        Tambah Paket Wisata         ||\n"
        text+= "========================================"
        print(text)
        # Requirement nama (chr 30), deskripsi (text), durashi (int)
        Nama = input("Nama Paket: ")
        if Nama != "" and len(Nama) <= 30:
            print(f"Nama Paket: {Nama}")
        else:
            continue
        deskripsi = input("Deskripsi Paket Wisata: ")
        while(1):
            durasi = input("Durasi Paket Wisata: ")
            if (durasi.isdigit):
                break
            else:
                print("Harus Berupa Nagka Saja")
        paket_wisata.PaketWisata.create(
            nama=Nama,
            deskripsi=deskripsi,
            durasi_hari=durasi
        ); return None
        
def HapusPaketWisata():
    paketWisatas: list[paket_wisata.PaketWisata] = paket_wisata.PaketWisata.read_all()
    listOfID: list[int] = [pW.id_paket for pW in paketWisatas]
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||         Hapus Paket Wisata         ||\n"
        text+= "========================================\n"
        for index, pW in enumerate(paketWisatas):
            text+= f"{index+1}. Nama: {pW.nama}\n, ID: {pW.id_paket}\n"
        text+= "========================================"
        print(text)
        id_picked = input("Masukan inputan id_paket: ")
        if (id_picked.isdigit()):
            id_picked = int(id_picked)
            if (id_picked in listOfID):
                paket_wisata.PaketWisata.delete(id_paket=id_picked)
                return
            else:
                lib.clear_terminal()
                print("ID tidak ada. Coba lagi.")
                time.sleep(2)
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
            
def UpdatePaketWisataPage():
    paketWisatas: list[paket_wisata.PaketWisata] = paket_wisata.PaketWisata.read_all()
    listOfID: list[int] = [pW.id_paket for pW in paketWisatas]
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||         Hapus Paket Wisata         ||\n"
        text+= "========================================\n"
        for index, pW in enumerate(paketWisatas):
            text+= f"{index+1}. Nama: {pW.nama}\n, ID: {pW.id_paket}\n"
        text+= "========================================"
        print(text)
        id_picked = input("Masukan inputan id_paket: ")
        if (id_picked.isdigit()):
            id_picked = int(id_picked)
            if (id_picked in listOfID):
                
                return
            else:
                lib.clear_terminal()
                print("ID tidak ada. Coba lagi.")
                time.sleep(2)
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def UpdatePaketWisataLogic(id_paket: int):
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||         Update Paket Wisata        ||\n"
        text+= "========================================\n"
        text+= "1. Rubah Akomodasi\n"
        text+= "2. Ruah Transportasi\n"
        text+= "3. Rubah Destinasi Wisata\n"
        text+= "========================================"
        print(text)
        pilihan = input("Masukan inputan id_paket: ")
        match pilihan:
            case '1':
                LihatPaketWisata()
                pass
            case '2':
                TambahPaketWisata()
                return None
            case '3':
                UpdatePaketWisataPage()
                pass
            case '4':
                HapusPaketWisata()
            case _:
                lib.clear_terminal()
                print("Pilihan tidak valid. Coba lagi.")
                time.sleep(2)

def EditAkomodasi():
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||          Update Akomodais          ||\n"
        text+= "========================================\n"
        text+= "1. Lihat Akomodais\n"
        text+= "2. Tambah Akomodais\n"
        text+= "3. Hapus Akomodais\n"
        text+= "========================================"
        print(text)
        pilihan = input("Masukan inputan id_paket: ")
        match pilihan:
            case '1':
                LihatAkomodasiWisata()
                pass
            case '2':
                TambahAkomodasiWisata()
                return None
            case '3':
                HapusAkomodasiWisata()
                pass
            case _:
                lib.clear_terminal()
                print("Pilihan tidak valid. Coba lagi.")
                time.sleep(2)

def KelolaAkun():
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||             Kelola Akun            ||\n"
        text+="========================================\n"
        text+="1. Kelola Akun Administrator\n"
        text+="2. Kelola Akun Pemandu\n"
        text+="3. Kelola Akun Wisatawan\n"
        text+="4. Kelola Akun Mitra\n"
        text+="5. Keluar\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            KelolaAkunAdminPage()
        elif pilihan == '2':
            KelolaAkunPemanduPage()
        elif pilihan == '3':
            KelolaAkunWisatawanPage()
        elif pilihan == '4':
            KelolaAkunMitraPage()
        elif pilihan == '5':
            
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
            
def KelolaAkunAdminPage():
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||      Kelola Akun Administrator     ||\n"
        text+="========================================\n"
        text+="1. Tambah Akun Administrator\n"
        text+="2. Rubah Akun Administrator\n"
        text+="3. Hapus Akun Administrator\n"
        text+="4. Keluar\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            TambahAkunAdminPage()
        elif pilihan == '2':
            RubahAkunAdminPage()
        elif pilihan == '3':
            HapusAkunAdminPage()
        elif pilihan == '4':
            
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
            
def TambahAkunAdminPage():
    pass
    
def HapusAkunAdminPage():
    admins: list[user.User] = user.User.read_administrator_all()
    listOfID: list[int] = [a.id_user for a in admins]
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||      Hapus Akun Administrator      ||\n"
        text+= "========================================\n"
        for index, a in enumerate(admins):
            text+= f"{index+1}. Nama: {a.username}\n, ID: {a.id_user}\n"
        text+= "========================================"
        print(text)
        id_picked = input("Masukan inputan id_paket: ")
        if (id_picked.isdigit()):
            id_picked = int(id_picked)
            if (id_picked in listOfID):
                user.User.delete(id_user=id_picked)
                return
            else:
                lib.clear_terminal()
                print("ID tidak ada. Coba lagi.")
                time.sleep(2)
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
        
def KelolaAkunPemanduPage():
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||         Kelola Akun Pemandu        ||\n"
        text+="========================================\n"
        text+="1. Tambah Akun Pemandu  \n"
        text+="2. Rubah Akun Pemandu  \n"
        text+="3. Hapus Akun Pemandu  \n"
        text+="4. Keluar\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")
        if pilihan == '1':
            TambahAkunPemanduPage()
        elif pilihan == '2':
            RubahAkunPemanduPage()
        elif pilihan == '3':
            HapusAkunPemanduPage()
        elif pilihan == '4':
            
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)

def TambahAkunPemanduPage():
    lib.clear_terminal()
    text =  "========================================\n"
    text += "||         Registrasi Pemandu         ||\n"
    text += "========================================"
    print(text)
    username = input("Buat username: ")

    if user.User.IsUserExist(username):
        lib.clear_terminal()
        print("Username sudah ada")
        time.sleep(2)
    else:
        role_id = roles.get_role_id(role_name="")#any# Bikin logika buat cari role di sini
        password = input("Buat password: ")
        nama_lengkap = input("Tambah Nama lengkap: ")
        kontak = input ("Tambah kontak: ")
        alamat = input("Tambah Alamat: ")
        # Buat user masukin data dulu, Id_Role nanti ajah
        # Habis buat langsung login ajah
        user.User.create(
            id_role = role_id,
            username = username,
            password = password,
            nama_lengkap = nama_lengkap,
            kontak = kontak,
            alamat = alamat 
        )
        lib.clear_terminal()
        print("Registrasi berhasil!!!")
        time.sleep(2)
    
def HapusAkunPemanduPage():
    pemandus: list[user.User] = user.User.read_pemandu_all()
    listOfID: list[int] = [a.id_user for a in pemandus]
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||      Hapus Akun Administrator      ||\n"
        text+= "========================================\n"
        for index, a in enumerate(pemandus):
            text+= f"{index+1}. Nama: {a.username}\n, ID: {a.id_user}\n"
        text+= "========================================"
        print(text)
        id_picked = input("Masukan inputan id_paket: ")
        if (id_picked.isdigit()):
            id_picked = int(id_picked)
            if (id_picked in listOfID):
                user.User.delete(id_user=id_picked)
                return
            else:
                lib.clear_terminal()
                print("ID tidak ada. Coba lagi.")
                time.sleep(2)
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
    
def KelolaAkunWisatawanPage():
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||        Kelola Akun Wisatawan       ||\n"
        text+="========================================\n"
        text+="1. Hapus Akun Wisatawan  \n"
        text+="2. Keluar\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            HapusAkunWisatawanPage()
        elif pilihan == '2':
            
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
            
def HapusAkunWisatawanPage():
    pemandus: list[user.User] = user.User.read_wisatawan_all()
    listOfID: list[int] = [a.id_user for a in pemandus]
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||      Hapus Akun Administrator      ||\n"
        text+= "========================================\n"
        for index, a in enumerate(pemandus):
            text+= f"{index+1}. Nama: {a.username}\n, ID: {a.id_user}\n"
        text+= "========================================"
        print(text)
        id_picked = input("Masukan inputan id_paket: ")
        if (id_picked.isdigit()):
            id_picked = int(id_picked)
            if (id_picked in listOfID):
                user.User.delete(id_user=id_picked)
                return
            else:
                lib.clear_terminal()
                print("ID tidak ada. Coba lagi.")
                time.sleep(2)
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
            
def KelolaAkunMitraPage():
    while True:
        lib.clear_terminal()
        text = "========================================\n"
        text+= "||          Kelola Akun Mitra         ||\n"
        text+="========================================\n"
        text+="1. Lihat Akun Mitra\n"
        text+="2. Tambah Akun Mitra\n"
        text+="3. Rubah Akun Mitra\n"
        text+="4. Hapus Akun Mitra\n"
        text+="5. Keluar\n"
        text+="========================================"
        print(text)
        pilihan = input("Masukan inputan (1-4): ")

        if pilihan == '1':
            LihatMitraWisata() # Done
        elif pilihan == '2':
            pass
        elif pilihan == '3':
            pass
        elif pilihan == '4':
            pass
        elif pilihan == '5':
            
            lib.clear_terminal()
            print("Terima kasih!")
            time.sleep(2)
            break
        else:
            lib.clear_terminal()
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(2)
def LihatMitraWisata():
    mitraWisataAkom: list[paket_wisata.AkomodasiOfPaket] = paket_wisata.get_akomodasi_paket()
    mitraWisataTrans: list[paket_wisata.TransportasiOfPaket] = paket_wisata.get_transport_paket()
    mitraWisataDest: list[paket_wisata.DestinasiOfPaket] = paket_wisata.get_destination_paket()
    while True:
        lib.clear_terminal()
        count = 0
        text = "========================================\n"
        text+= "||         Lihat Mitra Paket          ||\n"
        text+= "========================================\n"
        for mitra in mitraWisataAkom:
            count+=1
            text+= f"{count}. Nama: {mitra.nama}, Tipe: {mitra.tipe}, Rate: {mitra.bintang} ID: {mitra.id_akomodasi}\n"
        for mitra in mitraWisataTrans:
            count+=1
            text+= f"{count}. Nama: {mitra.nama_transportasi}, Jenis: {mitra.jenis}, ID: {mitra.id_transportasi}\n"
        for mitra in mitraWisataDest:
            count+=1
            text+= f"{count}. Nama: {mitra.nama_destinasi}, Lokasi: {mitra.lokasi}, ID: {mitra.id_destinasi}\n"
        text+= "========================================"
        print(text)
        pilihan = input("Masukan inputan '0' untuk kembali: ")
        if (pilihan == '0'):
            return None