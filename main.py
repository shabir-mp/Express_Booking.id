import time, os, random

print("\033[31mKereta Jakarta Bandung - Whoosh 🚄\033[0m")
print()
print("Selamat Datang dalam KCIC WHOOSH INDONESIA")

time.sleep(3)
os.system("clear")
print("\033[34m🎫 Registration 🎫 \033[0m")
print()
kode = input("Masukkan Lokasi Kota Anda ")
while True:
  if kode == "Bandung" or kode == "bandung":
    print("Bandung")
    break
  elif kode == "Jakarta" or kode == "jakarta":
    print("Jakarta")
    break
  else:
    print("Kota tidak dikenal")
    kode = input("Masukkan Lokasi Anda : ")
    continue

print("   ")
nama = input("Masukkan nama penumpang ")
pswd = input("Masukkan NIK Anda ")

while pswd != "123456":
  print("NIK Salah/Tidak Terdaftar, mohon ulangi NIK")
  pswd = input("> ")
  print()

tujuanawal = input("Masukkan Stasiun keberangkatan ")
tujuanakhir = input("Masukkan Stasiun tujuan ")
jumlahtiket = int(input("Masukkan jumlah penumpang (Tidak Termasuk Anda) "))

penumpanglain = []
for i in range(jumlahtiket):
  penumpanglain.append(input("Input Penumpang : "))
print()
print("Data Penumpang Lengkap")
print(penumpanglain)


def kelas():
  print()
  print("Pilih Jenis Kelas:")
  print("""
  0. Ekonomi - 100.000/Orang
  1. Ekonomi Premium - 150.000/Orang
  2. Eksekutif - 200.000/Orang
  3. Bussiness Class - 300.000/Orang
  4. First Class - 1.000.000/Orang
  5. Compartment Suite - 800.000/Orang
  """)
  print()
kelas()
kls = int(input("Pilih Jenis Kelas"))

print("   ")
print("Jenis Keberangkatan")
print("1. Pulang Pergi")
print("2. Pergi")
keberangkatan = input("Pilih jenis keberangkatan: ")

if keberangkatan == "1":
  print("Pulang Pergi")
  tanggalbrkt = input("Masukkan tanggal keberangkatan ")
  tanggalplg = input("Masukkan tanggal pulang ")
  print("Data Terupdate")
  kelas()
  print("\033[32m")
  print("--------------------------")
  print("Rincian Pemesanan")
  print("Tiket Pemesanan a.n", nama)
  print("Dari Stasiun ", tujuanawal)
  print("Menuju ke Stasiun", tujuanakhir)
  print("akan berangkat pada tanggal", tanggalbrkt, "dan pulang pada tanggal",
        tanggalplg, "\033[0m")

elif keberangkatan == "2":
  print("Pergi")
  tanggalbrkt = input("Masukkan tanggal keberangkatan ")
  print("Data Terupdate")
  kelas()
  print("\033[32m")
  print("-------------------------")
  print("Rincian Pemesanan")
  print("Tiket Pemesanan a.n", nama)
  print("Dari Stasiun ", tujuanawal)
  print("Menuju ke Stasiun", tujuanakhir)
  print("Akan berangkat pada tanggal", tanggalbrkt)
  print("\033[0m")

else:
  print("Pilihan tidak tersedia, mohon ulangi data")

print()
print("-------------------------")
cash = input("~Lanjutkan Pembayaran ? (Y/N) ")
if cash == "Y":
  print("""
  Total transaksi sebesar Rp. 5.000.000,00
  Pembayaran transfer a.n Whoosh Indonesia
  No. Rek 097656854467846755
  """)
elif cash == "N":
  print("Silahkan Membayar di Kounter")
else:
  print("error")

print("    ")
print("---------------‐-------------")
print("Kode Pemesanan Anda: GA685JLP976")
print("-----------------------------")
print("Terimakasih atas kepercayaan anda menggunakan Jasa Kereta Indonesia")
print("Semoga selamat sampai tujuan")
print("     ")
cetak = input("Cetak Borading Pass ? (Y/N) ")
if cetak == "Y":
  kode = input("Masukkan Kode Pemesanan ")
  while kode != "GA685JLP976":
    print("Kode tidak ditemukan.")
    kode = input("Ulangi Kode: ")
    print()
  print("Tunggu Sebentar....")
else:
  print("Terimakasih atas kepercayaan anda menggunakan Jasa Kereta Indonesia ")

print()
print("1. HELP")
print("2. ERROR")
print("3. DTBSE")
input = input("Stasion Costumer Center ")
if input == "1":
  print("Please Wait. The officers will be here in a moment ")
elif input == "2":
  print("ERR CODE: 98557F6YG7")
elif input == "3":
  print("DTBSE CODE : 567NGY6TV")
