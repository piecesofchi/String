txt = 'Hello World'

# 1. Hitung jumlah karakternya
jumlah_karakter = len(txt)  # 11

# 2. Ambil karakter terakhir
karakter_terakhir = txt[-1]  # 'd'

# 3. Ambil karakter index ke-2 sampai index ke-4
karakter_index_2_4 = txt[2:5]  # 'llo'

# 4. Hilangkan spasi pada teks tersebut
teks_tanpa_spasi = txt.replace(" ", "")  # 'HelloWorld'

# 5. Ubah teks menjadi huruf besar
teks_huruf_besar = txt.upper()  # 'HELLO WORLD'

# 6. Ubah teks menjadi huruf kecil
teks_huruf_kecil = txt.lower()  # 'hello world'

# 7. Ganti karakter H dengan karakter J
teks_ganti_h_j = txt.replace("H", "J")  # 'Jello World'

# Hasil
jumlah_karakter, karakter_terakhir, karakter_index_2_4, teks_tanpa_spasi, teks_huruf_besar, teks_huruf_kecil, teks_ganti_h_j