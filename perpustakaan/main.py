import os
import time

class Perpustakaan:
    def __init__(self):
        self.daftarbuku = []  # Format: [(judul, penulis, tahun)]
        self.daftarpeminjam = []  # Format: [(nama, judul, tanggal)]

    def tampilkan_menu(self):
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


        kode = int(input("\nMasukkan kode menu yang ingin diakses : "))
        self.pilih_menu(kode)

    def pilih_menu(self, kode):
        if kode == 1:
            self.lihat_daftarbuku()
        elif kode == 2:
            self.cari_buku()
        elif kode == 3:
            self.tambah_buku()
        elif kode == 4:
            self.hapus_buku()
        elif kode == 5:
            self.lihat_daftarpeminjam()
        elif kode == 6:
            self.tambah_peminjam()
        elif kode == 7:
            self.hapus_peminjam()
        elif kode == 8:
            print("Keluar dari Aplikasi...")
            time.sleep(1)
            exit()
        else:
            print("Kode yang Anda masukkan tidak valid.")
            input("\nTekan [ENTER] untuk kembali ke menu.")
            self.tampilkan_menu()

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
        self.tampilkan_menu()

    def cari_buku(self):
        os.system("cls")
        judul = input("\nMasukan judul buku yang ingin dicari: ")
        found = False
        for data in self.daftarbuku:
            if data[0].lower() == judul.lower():
                print(f"Buku ditemukan: {data[0]} | {data[1]} | {data[2]}")
                found = True
                break
        if not found:
            print("Hasil pencarian tidak ditemukan.")
        input("\nTekan [ENTER] untuk kembali ke menu.")
        self.tampilkan_menu()

    def tambah_buku(self):
        os.system("cls")
        print("TAMBAH BUKU")
        judul = input("Judul Buku : ")
        penulis = input("Penulis Buku : ")
        tahun = input("Tahun Terbit : ")
        self.daftarbuku.append((judul, penulis, tahun))
        print("[Data Buku Berhasil Ditambahkan]")
        input("\nTekan [ENTER] untuk kembali ke menu.")
        self.tampilkan_menu()

    def hapus_buku(self):
        os.system("cls")
        judul = input("Masukkan judul buku yang ingin dihapus : ")
        self.daftarbuku = [data for data in self.daftarbuku if data[0].lower() != judul.lower()]
        print("\n[Data Buku Telah Terhapus]")
        input("\nTekan [ENTER] untuk kembali ke menu.")
        self.tampilkan_menu()

   def lihat_daftarpeminjam(self):
        os.system("cls")
        print("DAFTAR PEMINJAM BUKU")
        print("=" * 50)
        if not self.daftarpeminjam:
            print("\n[Data tidak tersedia]")
        else:
            for i, (nama, judul, tanggal) in enumerate(self.daftarpeminjam, start=1):
                print(f"{i}. {nama} | {judul} | {tanggal}")
        input("\nTekan [ENTER] untuk kembali ke menu.")
        self.tampilkan_menu()

    def tambah_peminjam(self):
        os.system("cls")
        print("TAMBAH PEMINJAM BUKU")
        nama = input("Nama Peminjam : ")
        judul = input("Judul Buku : ")
        tanggal = input("Tanggal Peminjaman : ")
        self.daftarpeminjam.append((nama, judul, tanggal))
        print("[Data Peminjam Berhasil Ditambahkan]")
        input("\nTekan [ENTER] untuk kembali ke menu.")
        self.tampilkan_menu()

    def hapus_peminjam(self):
        os.system("cls")
        nama = input("Masukkan Nama Peminjam yang Ingin Dihapus : ")
        self.daftarpeminjam = [data for data in self.daftarpeminjam if data[0].lower() != nama.lower()]
        print("\n[Data Peminjam Telah Terhapus]")
        input("\nTekan [ENTER] untuk kembali ke menu.")
        self.tampilkan_menu()

    


if __name__ == "__main__":
    perpustakaan = Perpustakaan()
    perpustakaan.tampilkan_menu()
