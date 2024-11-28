import os
import time

class Buku:
    def __init__(self):
        self.daftarbuku = [
            ("Matematika untuk SMA Kelas 10", "Tim Penyusun", 2021),
            ("Fisika Dasar untuk SMA Kelas 11", "Dr. Budi Santoso", 2020),
            ("Kimia untuk SMA Kelas 12", "Dr. Tri Widodo", 2019),
            ("Biologi untuk SMP Kelas 9", "Dr. Ratna Dewi", 2021),
            ("Bahasa Inggris untuk SMA Kelas 10", "Tim Penerbit", 2020),
            ("Sejarah Indonesia untuk SMA Kelas 11", "Ahmad Fauzan", 2018),
            ("Ekonomi untuk SMA Kelas 10", "Dr. Dian Kurnia", 2019),
            ("Sosiologi untuk SMA Kelas 12", "Dr. Indah Permatasari", 2020),
            ("Geografi untuk SMA Kelas 10", "Tim Geosmart", 2021),
            ("Pendidikan Agama Islam Kelas 9", "Ust. Muhammad Rasyid", 2020),
            ("Matematika untuk SMP Kelas 8", "Tim Penyusun", 2021),
            ("Ilmu Pengetahuan Alam untuk SMP Kelas 7", "Tim Penerbit", 2019),
            ("Bahasa Indonesia untuk SMA Kelas 12", "Dr. Andi Wijaya", 2020),
            ("Pendidikan Pancasila dan Kewarganegaraan untuk SMA", "Dr. Sari Lestari", 2021),
            ("Teknologi Informasi dan Komunikasi untuk SMA", "Ir. Eko Prasetyo", 2020),
            ("Kewirausahaan untuk SMA Kelas 11", "Dr. Sri Utami", 2020),
            ("Matematika Terapan untuk SMK", "Dr. Bambang Sugiarto", 2018),
            ("Fisika Modern untuk SMA", "Prof. Yuni Susanti", 2021),
            ("Bahasa Jepang Dasar untuk SMA", "Hiroshi Yamamoto", 2020),
            ("Seni Budaya untuk SMA Kelas 10", "Tim Seni Nusantara", 2019)
        ]

    def lihat_daftarbuku(self):
        os.system("cls")
        print("DAFTAR BUKU YANG TERSEDIA")
        print("=" * 50)
        if not self.daftarbuku:
            print("\n[Data tidak tersedia]")
        else:
            for i, (judul, penulis, tahun) in enumerate(self.daftarbuku, start=1):
                print(f"{i}. {judul} | {penulis} | {tahun}")
        input("\nTekan [ENTER] untuk kembali ke menu.")

    def cari_buku(self):
        os.system("cls")
        kata_kunci = input("\nMasukkan kata kunci untuk mencari buku: ").lower()
        found = False
        for data in self.daftarbuku:
            if kata_kunci in data[0].lower():  
                print(f"Buku ditemukan: {data[0]} | {data[1]} | {data[2]}")
                found = True
        if not found:
            print("Hasil pencarian tidak ditemukan.")
        input("\nTekan [ENTER] untuk kembali ke menu.")

    def tambah_buku(self):
        os.system("cls")
        print("TAMBAH BUKU")
        judul = input("Judul Buku : ")
        penulis = input("Penulis Buku : ")
        tahun = input("Tahun Terbit : ")
        self.daftarbuku.append((judul, penulis, tahun))
        print("[Data Buku Berhasil Ditambahkan]")
        input("\nTekan [ENTER] untuk kembali ke menu.")

    def hapus_buku(self):
        os.system("cls")
        judul = input("Masukkan judul buku yang ingin dihapus : ")
        self.daftarbuku = [data for data in self.daftarbuku if data[0].lower() != judul.lower()]
        print("\n[Data Buku Telah Terhapus]")
        input("\nTekan [ENTER] untuk kembali ke menu.")

class Peminjam:
    def _init_(self):
        self.daftarpeminjam = [
            "Rina Suryani - Buku: Matematika untuk SMA Kelas 10",
            "Andi Pratama - Buku: Fisika Dasar untuk SMA Kelas 11",
            "Siti Aminah - Buku: Kimia untuk SMA Kelas 12",
            "Budi Santoso - Buku: Biologi untuk SMP Kelas 9",
            "Ani Lestari - Buku: Sejarah Indonesia untuk SMA Kelas 11"
        ]

    def lihat_daftarpeminjam(self):
        os.system("cls")
        print("DAFTAR PEMINJAM BUKU")
        print("=" * 50)
        if not self.daftarpeminjam:
            print("\n[Data tidak tersedia]")
        else:
            for i, peminjam in enumerate(self.daftarpeminjam, start=1):
                print(f"{i}. {peminjam}")
        input("\nTekan [ENTER] untuk kembali ke menu.")

    def tambah_peminjam(self):
        os.system("cls")
        nama = input("Masukkan nama peminjam: ")
        self.daftarpeminjam.append(nama)
        print("[Data Peminjam Berhasil Ditambahkan]")
        input("\nTekan [ENTER] untuk kembali ke menu.")

    def hapus_peminjam(self):
        os.system("cls")
        nama = input("Masukkan nama peminjam yang ingin dihapus: ")
        self.daftarpeminjam = [peminjam for peminjam in self.daftarpeminjam if peminjam.lower() != nama.lower()]
        print("\n[Data Peminjam Telah Terhapus]")
        input("\nTekan [ENTER] untuk kembali ke menu.")

class Menu:
    def _init_(self):
        self.buku = Buku()
        self.peminjam = Peminjam()

    def tampilkan_menu(self):
        while True:
            os.system("cls")
            print(" " * 12, "PERPUSTAKAAN MI", " " * 12)
            print("Pilih daftar menu untuk mengakses Aplikasi :")
            print("=" * 50)
            print("[1] Lihat Daftar Buku")
            print("[2] Cari Buku")
            print("[3] Tambah Data Buku")
            print("[4] Hapus Data Buku")
            print("[5] Lihat Daftar Peminjam Buku")
            print("[6] Tambah Peminjam Buku")
            print("[7] Hapus Data Peminjam Buku")
            print("[8] Keluar dari Aplikasi")

            try:
                kode = int(input("\nMasukkan kode menu yang ingin diakses : "))
                self.pilih_menu(kode)
            except ValueError:
                print("Input harus berupa angka.")
                time.sleep(1)

    def pilih_menu(self, kode):
        if kode == 1:
            self.buku.lihat_daftarbuku()
        elif kode == 2:
            self.buku.cari_buku()
        elif kode == 3:
            self.buku.tambah_buku()
        elif kode == 4:
            self.buku.hapus_buku()
        elif kode == 5:
            self.peminjam.lihat_daftarpeminjam()
        elif kode == 6:
            self.peminjam.tambah_peminjam()
        elif kode == 7:
            self.peminjam.hapus_peminjam()
        elif kode == 8:
            print("Keluar dari Aplikasi...")
            time.sleep(1)
            exit()
        else:
            print("Kode yang Anda masukkan tidak valid.")
            input("\nTekan [ENTER] untuk kembali ke menu.")


    
