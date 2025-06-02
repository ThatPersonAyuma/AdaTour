from . import lib

def home_page():
    warning:str=""
    while(1):
        lib.clear_terminal()
        strings = "\n".join(lib.center("ADA TOUR", "SOLUSI TERBAIK UNTUK WISATA"))+"\n"
        strings += "\nSilahkan Pilih Aksi Berikutnya:\n1. Masuk\n2.Registrasi"
        print(strings)
        print(warning, end="")
        userChoice = input("Ketik angka saja ('0' untuk keluar): ")
        if userChoice=='0' or userChoice=='1' or userChoice=='2':
            return userChoice
        else:
            warning = lib.string_clr_Red("Inputan Tidak Valid") +"\n"