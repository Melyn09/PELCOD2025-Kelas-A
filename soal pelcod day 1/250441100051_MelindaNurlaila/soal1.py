print("==soal 1 Menghitung Total Waktu Menonton==")

# Durasi satu episode dalam menit
durasi_per_episode = int(input("Masukkan durasi satu episode (menit):"))

# Total jumlah episode
total_episode = int(input("Masukkan Jumlah Episode: "))


# Hitung total durasi dalam menit
total_menit = durasi_per_episode * total_episode

# Konversi menit ke jam dan menit dan detik
jam = total_menit // 60
menit = total_menit % 60

# Tampilkan Hasil
print("\nkamu menonton selama:")
print(f"{jam} jam {menit} menit")

print("="*100)

print("==soal 2 menghitung sisa uang setelah membeli ikan==")

# Input harga ikan
harga_cupang = int(input("Masukkan harga cupang (Rp):"))
harga_Koi = int(input("Masukkan harga koi (Rp):"))

# Input jumlah ikan yang dibeli
jumlah_cupang = int(input("Masukkan jumlah cupang yang dibeli:"))
jumlah_koi = int(input("Masukkan jumlah koi yang dibeli:"))

# Input total uang yang dibawa
total_uang = int(input("Masukkan total uang yang kamu bawa (Rp)"))

# Hitung total belanja
total_belanja = (harga_cupang*jumlah_cupang) + (harga_Koi*jumlah_koi)

# Cek apakah uang yang kamu bawa cukup
if total_belanja > total_uang :
    print("\nUang kamu tidak cukup.")
    print(f"Total belanja: Rp {total_belanja:,}")
    print(f"Sedangkan Uang kamu: Rp {total_uang:,}")
else:
    sisa_uang = total_uang - total_belanja
    print(f"\nTotal belanja: Rp {total_belanja:,}")
    print(f"Sisa uang kamu: Rp {sisa_uang:,}")

print("="*100)

print("==Soal 3 Menghitung perhitungan BBM==")

# input dari pengguna
jarak = float(input("Masukkan total jarak perjalanan (KM):"))
konsumsi = float(input("Masukkan konsumsi BBM sepeda motor (KM per liter):"))
kapasitas_tangki = float(input("Masukkan kapasitas tangki sepeda motor (Liter):"))
harga_bensin = float(input("Masukkan harga bensin per liter (Rp):"))

# Total bensin yang dibutuhkan
total_bensin = jarak/konsumsi

# Cek apakah dapat diskon
if total_bensin > 3 :
    harga_bensin_diskon = harga_bensin - 500
else:
    harga_bensin_diskon = harga_bensin

# Hitung total biaya bensin
total_biaya = total_bensin*harga_bensin_diskon

# Hitung berapa kali harus mengisi bensin (asumsi tangki penuh setiap kali isi)
jumlah_isi = total_bensin/kapasitas_tangki

# Pembulatan keatas karna tidak bisa isi sebagian
import math
jumlah_isi = math.ceil(jumlah_isi)

# Tampilkan hasil
print(f"nTotal bensin yang dibutuhkan: {total_bensin:.2f}Liter")
print(f"harga bensin per liter setelah diskon (jika ada): Rp {harga_bensin_diskon}")
print(f"Total biaya bensin: Rp {total_biaya:.2f}")
print(f"Perkiraan jumlah kali mengisi bensin: {jumlah_isi}kali")