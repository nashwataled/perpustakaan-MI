# Perpustakaan MI

Aplikasi perpustakaan berbasis Python untuk mengelola daftar buku dan peminjam. Proyek ini menyediakan fitur seperti melihat daftar buku, menambah atau menghapus buku, mencari buku, serta mengelola data peminjam.

## Struktur Proyek
- `main.py`: Berisi implementasi utama aplikasi, termasuk kelas `Buku`, `Peminjam`, dan `Menu`.
- `run.py`: Entry point untuk menjalankan aplikasi dengan memanfaatkan kelas `Menu` dari `main.py`.

## Fitur
1. **Manajemen Buku**
   - Melihat daftar buku yang tersedia.
   - Menambah buku baru ke daftar.
   - Menghapus buku dari daftar.
   - Mencari buku berdasarkan kata kunci.

2. **Manajemen Peminjam**
   - Melihat daftar peminjam buku.
   - Menambahkan data peminjam baru.
   - Menghapus data peminjam.

3. **Menu Utama**
   - Navigasi sederhana dengan berbagai opsi untuk mengakses fitur di atas.

## Cara Menjalankan
### Prasyarat
- Pastikan Python 3 sudah terinstal di komputer Anda.
- Sistem operasi Windows, karena ada penggunaan perintah `os.system("cls")` untuk membersihkan layar.

### Langkah Menjalankan
1. Clone atau download proyek ini.
2. Buka terminal atau command prompt.
3. Jalankan file `run.py` dengan perintah berikut:
   ```bash
   python run.py
4. Ikuti instruksi di layar untuk memilih menu dan mengakses fitur aplikasi.

## Contoh Penggunaan

Melihat Daftar Buku
Pilih menu 1.
Daftar buku akan ditampilkan dengan informasi judul, penulis, dan tahun terbit.

Mencari Buku
Pilih menu 2.
Masukkan kata kunci untuk mencari buku.
Jika ditemukan, informasi buku akan ditampilkan.

Menambah Buku
Pilih menu 3.
Masukkan detail buku seperti judul, penulis, dan tahun terbit.
Buku baru akan ditambahkan ke daftar.

## Pembagian Kontribusi
- **Nashwa Talitha Putri**: 
  - Mengembangkan **class Buku**, yang mencakup fitur untuk melihat, menambah, menghapus, dan mencari data buku.

- **Farhan Naufal**: 
  - Mengembangkan **class Peminjam**, yang mencakup fitur untuk melihat, menambah, dan menghapus data peminjam.

- **Cindy Novitri**: 
  - Mengembangkan **class Menu**, termasuk fungsi navigasi utama untuk menghubungkan semua fitur aplikasi.

- **Ilham Randi Kesuma**: 
  - Menyusun **presentasi (PPT)** untuk menjelaskan konsep aplikasi.
  - Memberikan **ide-ide kreatif** untuk desain aplikasi dan pengembangan fitur.




