import os
import pwinput
import time
from prettytable import PrettyTable

# Dictionary
barang = {
    "1001":{
        "nama" : "Laptop",
        "keluaran" : "2025"
    },
    "1002":{
            "nama" : "Tablet",
            "keluaran" : "2025"
    },
    "1003":{
            "nama" : "Handphone",
            "keluaran" : "2025"
    },
}
dipinjam = {}
tidak_tersedia = {}
users = {
    "admin":{
        "nama": "Admin",
        "pass": "1234",
        "izin": "admin"
    },
    "user":{
        "nama": "user",
        "pass": "user",
        "izin": "user"
    }

}

# Jika sebuah definisi sudah selesai, maka def ini akan dipanggil
def freeze():
    input("\nKlik Enter untuk kembali ke menu...")
    os.system("cls" if os.name == "nt" else "clear")

# Tabel barang
def view(viewbarang, judul):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ["ID", "Tipe Barang", "Keluaran"]
    for ids, datas in viewbarang.items():
        tabel.add_row([ids, datas["nama"], datas["keluaran"]])
    print(tabel)

# Nambah/Hapus barang
def nambahhapus():
    print("Opsi:")
    print("1: Tambah")
    print("2: hapus")
    edit = input("Pilihan Opsi: ")
    if edit == "2":
        view(barang, "Barang") 
        modifydel = input("Masukkan ID barang yang mau dihapus: ")
        if modifydel in barang:
            data = barang.pop(modifydel)
            print(f"Barang {data['nama']} telah dihapus")
        else:
            print("Barang tidak ditemukan")
    elif edit == "1":
        view(barang, "Barang")
        insert = input("Masukkan ID barang baru: ")
        if insert in barang or insert in dipinjam or insert in tidak_tersedia:
            print("ID sudah dipakai")
            return
        name = input("Nama barang: ")
        releases = input("Tahun keluaran: ")
        barang[insert] = {"nama": name, "keluaran": releases}
        print(f"Barang {name} telah ditambah")
    else:
        print("Tidak Valid")

# Mengubah status barang tidak tersedia/tersedia
def tidaktersedia():
    view(barang, "Barang Tersedia")  
    view(tidak_tersedia, "Barang Tidak Tersedia")  
    select = input("Masukkan kode barang yang ingin diubah statusnya: ")

    if select in barang:
        tidak_tersedia[select] = barang.pop(select)
        print(f"Barang {tidak_tersedia[select]['nama']} telah dibuat tidak tersedia")
    elif select in tidak_tersedia:
        barang[select] = tidak_tersedia.pop(select)
        print(f"Barang {barang[select]['nama']} telah dibuat tersedia")
    else:
        print("Barang tidak ditemukan")

# Memminjam barang
def pinjam():
    view(barang, "Barang Tersedia") 
    select = input("Pilih barang yang ingin dipinjam sesuai ID: ")
    
    if select in barang:
        dipinjam[select] = barang.pop(select)
        print(f"Barang {dipinjam[select]['nama']} telah dipinjam")
    else:
        print("Barang tidak ditemukan, dipinjam, atau tidak tersedia")

# Mengembalikan barang
def kembalikan():
    view(dipinjam, "Barang yang sedang dipinjam")
    select = input("Pilih barang yang ingin dikembalikan sesuai ID: ")
    if select in dipinjam:
        barang[select] = dipinjam.pop(select)
        print(f"Barang {barang[select]['nama']} telah dikembalikan")
    else:
        print("Barang tidak ditemukan")

# Managemen user
def manageusers():
        print("Opsi manajmen user: ")
        print("1. Melihat")
        print("2. Menambah")
        print("3. Menghapus")
        opsi = input("Pilih: ")
        if opsi == "1":
            os.system("cls" if os.name == "nt" else "clear")
            tabeluser = PrettyTable()
            tabeluser.title = "LIST USER"
            tabeluser.field_names = ["Username", "Nama", "Akses Izin"]
            for usn, data in users.items():
                tabeluser.add_row([usn, data["nama"], data["izin"]])
            print(tabeluser)
        elif opsi == "3":
            usn = input("Masukkan user yang ingin dihapus: ")
            if usn == "admin":
                print("Akun admin tidak boleh dihapus")
                return
            elif usn in users:
                users.pop(usn)
                print(f"Username {usn} telah dihapus")
            else:
                print("Tidak valid")
        elif opsi == "2":
            usn = input("Masukkan username: ")
            if usn in users:
                print("Username sudah dipakai")
                return
            elif usn == "exit":
                print("Username tidak boleh 'exit'")
                return
            name = input("Nama: ")
            passw = pwinput.pwinput("Password: ")
            perm = input("Izin (admin/user): ")
            if perm not in ("admin", "user"):
                print("Tidak Valid")
                return
            users[usn] = {"nama": name, "pass": passw, "izin": perm}
            print(f"User {usn} telah ditambah") 
        else:
            print("Pilihan tidak valid")         

# Menu Admin
def menuadmin():
    while True:
        print("============ MENU ADMIN ============")
        print("1. Status Barang")
        print("2. Tambah/Hapus Barang")
        print("3. Ubah Status Ketersediaan")
        print("4. Manajemen User")
        print("0. Logout")
        insert = input("Pilihan menu: ")

        if insert == "1":
            view(barang, "Barang Tersedia")
            view(tidak_tersedia, "Barang Tidak Tersedia")
            view(dipinjam, "Barang yang sedang dipinjam")
        elif insert == "2":
            nambahhapus()
        elif insert == "3":
            tidaktersedia()
        elif insert == "4":
            manageusers()
        elif insert == "0":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("Pilihan Invalid")
        freeze()

# Menu user
def menuuser():
    while True:
        print("============ MENU USER ============")
        print("1. Lihat Barang")
        print("2. Pinjam Barang")
        print("3. Mengembalikan barang")
        print("0. Logout")
        insert = input("Pilihan menu: ")
        if insert == "1":
            view(barang, "Barang Tersedia")
            view(tidak_tersedia, "Barang Tidak Tersedia")
            view(dipinjam, "Barang yang dipinjam")
        elif insert == "2":
            pinjam()
        elif insert == "3":
            kembalikan()
        elif insert == "0":
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("Pilihan Invalid")
        freeze()
        
# Logika login
def main():
    while True:
        usn = input("Masukkan Username (ketik 'exit' untuk exit): ")
        if usn == "exit":
                print("Terimakasih")
                break
        passw = pwinput.pwinput("Masukkan Password: ")

        if usn in users and users[usn]["pass"] == passw:
            print(f"Selamat datang, {users[usn]['nama']}.")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")

            if users[usn]["izin"] == "admin":
                menuadmin()
            else:
                menuuser()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Username/Password Salah")
            
        

main()
