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
        print("[7] Hapus Data Peminjam Buku")
        print("[8] Keluar dari Aplikasi")

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

   

    


if __name__ == "__main__":
    perpustakaan = Perpustakaan()
    perpustakaan.tampilkan_menu()
