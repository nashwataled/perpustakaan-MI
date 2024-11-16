import os
import time

class Buku:
    def __init__(self):
        self.daftarbuku = []

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
        self.daftarpeminjam = []

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
    


if __name__ == "__main__":
    perpustakaan = Perpustakaan()
    perpustakaan.tampilkan_menu()
