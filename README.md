
'''python
def validasi_pendaftaran(nama, nomor_telepon, email):
    errors = []
    
    # Validasi nama (hanya huruf dan spasi)
    if not nama.replace(" ", "").isalpha():
        errors.append("Nama lengkap harus hanya berisi huruf.")
    
    # Validasi nomor telepon (hanya angka)
    if not nomor_telepon.isdigit():
        errors.append("Nomor telepon harus hanya berisi angka.")
    
    # Validasi email (harus mengandung @ dan .)
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        errors.append("Email harus mengandung karakter '@' dan '.'.")
    
    # Output hasil validasi
    if errors:
        print("Terdapat kesalahan:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Data pendaftaran valid.")

    # Contoh input pengguna
    nama = input("Masukkan nama lengkap: ")
    nomor_telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    
    # Panggil fungsi validasi
    validasi_pendaftaran(nama, nomor_telepon, email)


1. Validasi Nama
   Untuk memastikan hanya huruf dan spasi yang diperbolehkan, gunakan replace(" ", "").isalpha()
2. Pengesahan Nomor Telepon
   Menggunakan isdigit() untuk memastikan bahwa hanya angka yang diizinkan
3. Verifikasi email
   Untuk memastikan format email yang valid (mengandung @ dan. dengan posisi yang sesuai), gunakan ekspresi reguler re.match().
4. Keputusan Validasi
   -Program mencetak daftar kesalahan jika terjadi kesalahan.
   -Program mencetak pesan "Data pendaftaran valid" jika semua validasi berhasil.
