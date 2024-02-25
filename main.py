import os
import time
import random

#subrutin untuk memesan tiket
def pesan():
  os.system("clear")
  print("\033[34m🎫 Registration 🎫 \033[0m")
  print()
  user_inpt = input("Masukkan Lokasi Kota Anda ").strip().lower()
  while True:
    if user_inpt == "bandung":
      print("Bandung")
      break
    elif user_inpt == "jakarta":
      print("Jakarta")
      break
    else:
      print("Kota tidak dikenal")
      inpt = input("Masukkan Lokasi Anda : ")
      continue

  print("   ")
  nama = input("Masukkan nama penumpang ")
  pswd = input("Masukkan NIK Anda ")

  while pswd != "123456":
    print("NIK Salah/Tidak Terdaftar, mohon ulangi NIK")
    pswd = input("> ")
    print()
  os.system("clear")
  tujuanawal = input("Masukkan Stasiun keberangkatan ")
  tujuanakhir = input("Masukkan Stasiun tujuan ")
  jumlahtiket = int(input("Masukkan jumlah penumpang (Tidak Termasuk Anda) "))

  penumpanglain = []
  for i in range(jumlahtiket):
    penumpanglain.append(input("Input Penumpang : "))
  print()
  print("Data Penumpang Lengkap")
  print(penumpanglain)
  os.system("clear")
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
  kls = int(input("Pilih Jenis Kelas "))
  os.system("clear")
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
    os.system("clear")
    print("\033[32m")
    print("--------------------------")
    print("-Rincian Pemesanan-\n")
    print("Tiket Pemesanan a.n", nama)
    print("Dari Stasiun ", tujuanawal)
    print("Menuju ke Stasiun", tujuanakhir)
    print("akan berangkat pada tanggal", tanggalbrkt,
          "dan pulang pada tanggal", tanggalplg, "\033[0m")

  elif keberangkatan == "2":
    print("Pergi")
    tanggalbrkt = input("Masukkan tanggal keberangkatan ")
    print("Data Terupdate")
    os.system("clear")
    print("\033[32m")
    print("-------------------------")
    print("-Rincian Pemesanan-\n")
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
    while kode != "GAAUL":
      print("Kode tidak ditemukan.")
      kode = input("Ulangi Kode: ")
      print()
    print("Tunggu Sebentar....")
  else:
    print(
        "Terimakasih atas kepercayaan anda menggunakan Jasa Kereta Indonesia ")

  print()
  while True:
    print("1. KELUAR")
    print("2. BANTUAN")
    user_input = input("> ")
    if user_input.strip() == "1":
      print("Tunggu Sebentar...")
      os.system("clear")
      intro()
      break
    elif user_input.strip() == "2":
      print("Tunggu Sebentar, Petugas akan Membantu Anda")
      exit = input("ENTER UNTUK KELUAR >")
      if exit == "":
        print("Tunggu Sebentar...")
        time.sleep(2)
        os.system("clear")
        intro()
        break
    else:
      print("ERROR, MOHON ULANGI KEMBALI")
      continue

#subrutin untuk melihat jadwal
def jadwal():
  os.system("clear")
  print("Jadwal Kereta :")

  print("""
  1. 17:30 | Argo Bromo Anggrek | 134 | Jakarta Gambir - Surabaya Pasar Turi
  2. 18:30 | Argo Parahyangan | 30 | Jakarta Gambir - Bandung
  3. 19:30 | Mutiara Selatan | 132 | Jakarta Gambir - Malang Kotalama
  4. 20:30 | Malabar | 129 | Bandung - Malang Kotalama
  5. 21:30 | Malabar | 130 | Malang Kotalama - Bandung

  6. 22:30 | Tawang Jaya | 133 | Semarang Tawang - Pasar Senen
  7. 23:30 | Senja Bengawan | 131 | Solo Jebres - Jakarta Pasar Senen
  8. 00:30 | Jayabaya | 135 | Malang Kotalama - Jakarta Pasar Senen
  9. 01:30 | Bengawan | 136 | Jakarta Pasar Senen - Solo Jebres
  10. 02:30 | Argo Wilis | 137 | Surabaya Gubeng - Bandung

  11. 03:30 | Pasundan | 138 | Surabaya Gubeng - Bandung Kiaracondong
  12. 04:30 | Turangga | 139 | Surabaya Gubeng - Bandung
  13. 05:30 | Logawa | 140 | Purwokerto - Jember
  14. 06:30 | Gaya Baru Malam Selatan | 141 | Surabaya Gubeng - Jakarta Pasar Senen

  15. 07:30 | Sawunggalih | 142 | Jakarta Pasar Senen - Kutoarjo
  16. 08:30 | Sritanjung | 143 | Bandung - Banyuwangi
  17. 09:30 | Kahuripan | 144 | Kiaracondong - Blitar
  18. 10:30 | Malabar | 145 | Malang Kotalama - Bandung

  19. 11:30 | Malabar | 146 | Bandung - Malang Kotalama
  20. 12:30 | Argo Parahyangan | 147 | Bandung - Jakarta Gambir
  21. 13:30 | Argo Bromo Anggrek | 148 | Surabaya Pasar Turi - Jakarta Gambir
  22. 14:30 | Mutiara Selatan | 149 | Malang Kotalama - Jakarta Gambir

  23. 15:30 | Tawang Jaya | 150 | Pasar Senen - Semarang Tawang
  24. 16:30 | Senja Bengawan | 151 | Jakarta Pasar Senen - Solo Jebres
  25. 22:30 | Jayabaya | 152 | Jakarta Pasar Senen - Malang Kotalama

  26. 23:30 | Bengawan | 153 | Solo Jebres - Jakarta Pasar Senen
  27. 00:30 | Argo Wilis | 154 | Bandung - Surabaya Gubeng
  28. 01:30 | Pasundan | 155 | Bandung Kiaracondong - Surabaya Gubeng
  29. 02:30 | Turangga | 156 | Bandung - Surabaya Gubeng

  30. 03:30 | Logawa | 157 | Jember - Purwokerto
  """)
  print()
  while True:
    print("1. KELUAR")
    print("2. BANTUAN")
    user_input = input("> ")
    if user_input.strip() == "1":
      print("Tunggu Sebentar...")
      os.system("clear")
      intro()
      break
    elif user_input.strip() == "2":
      print("Tunggu Sebentar, Petugas akan Membantu Anda")
      exit = input("ENTER UNTUK KELUAR >")
      if exit == "":
        print("Tunggu Sebentar...")
        time.sleep(2)
        os.system("clear")
        intro()
        break
    else:
      print("ERROR, MOHON ULANGI KEMBALI")
      continue

#subrutin railfood
def railfood():
  os.system("clear")
  kode = input("Kode Pemesanan Anda/Booking Code: ")
  time.sleep(2)
  os.system("clear")
  print("\033[34m🍽 Menu Railfood Kereta Api\033[0m")
  print("""
-Makanan/Food:
1. Nasi Goreng Special - Rp 25.000
2. Ayam Bakar Madu - Rp 30.000
3. Mie Goreng Seafood - Rp 28.000
4. Sate Padang - Rp 22.000
5. Rawon Daging - Rp 35.000
6. Sop Buntut - Rp 40.000
7. Burger Rendang - Rp 18.000
8. Martabak Telur - Rp 15.000
9. Nasi Uduk Komplit - Rp 20.000
10. Capcay Kuah - Rp 25.000
11. Es Campur - Rp 15.000
12. Pisang Goreng Keju - Rp 12.000
13. Bubur Sumsum - Rp 10.000
14. Roti Bakar Srikaya - Rp 8.000
15. Pudding Coklat - Rp 12.000
16. Kue Lapis Legit - Rp 18.000
17. Klepon Pandan - Rp 6.000
18. Tahu Tek - Rp 10.000
19.Lumpia Semarang - Rp 15.000
20. Es Teh Manis - Rp 5.000

-Minuman/Drink:
1. Kopi Tubruk - Rp 10.000
2. Teh Tarik - Rp 8.000
3. Es Jeruk Segar - Rp 7.000
4. Jus Alpukat - Rp 12.000
5. Kopi Susu Gula Aren - Rp 15.000
6. Lassi Mangga - Rp 10.000
7. Sirup Marjan - Rp 5.000
18. Air Kelapa Muda - Rp 8.000
19.Capuccino - Rp 12.000
20. Sjora - Rp 6.000
  """)
  menupesanan = []
  while True:
   pesanan = input("Pesan/Order > ")
   menupesanan.append(pesanan)
   print()
   print(menupesanan)
   print()
   exit = input("Tambah Pesanan/Add More ? (Y/N) ").lower().strip()
   if exit == "y":
     continue
   elif exit == "n":
     break
  print(f"Pesanan Anda/Your Order: {menupesanan}")
  time.sleep(5)
  os.system("clear")
  intro()

#subrutin porter
def porter():
  os.system("clear")
  print("Pemesanan Porter")
  porterinput = input("Masukkan Kode Pemesanan Anda: ")
  time.sleep(1)
  os.system("clear")
  print("Mencari Porter...")
  time.sleep(3)
  os.system("clear")
  porterlist = ["Agus Sugus", "Dadang Sutisna", "Aul Mengaul", "Danial Ibrahim", "Maulana Zahir"]
  porterpilihan = random.choice(porterlist)
  print(f"Kode Pemesanan : {porterinput}")
  print("Porter Anda: ", porterpilihan)
  print("--------------")
  print("TEKAN ENTER UNTUK KELUAR")
  inpt2 = input("> ")
  if inpt2 == "":
    time.sleep(2)
    os.system("clear")
    intro()

  
#subrutin kritik dan saran
def kritiksaran():
  os.system("clear")
  kersan = []
  print("Kritik dan Saran")
  print("Silahkan Masukkan Kritik dan Saran Untuk PT. KAI.")
  kritik = input("> Masukkan disini \n")
  kersan.append(kritik)
  print()
  print("Terimakasih atas Kritik dan Masukannya. Kami akan menerima kritik dan saran anda.")
  print()
  time.sleep(3)
  os.system("clear")
  intro()

#subrutin layar awal
def intro():
  print("\033[31mKereta Api Indonesia 🚄\033[0m")
  print()
  print("Selamat Datang di Stasiun Kereta Api Bandung - DAOP 2")
  print()
  print()
  
  halo = input("Tekan Enter Untuk Melanjutkan ")
  if halo == "":
    while True:
      os.system("clear")
      print(
          "Selamat Datang ! \n 1. Pesan Tiket \n 2. Jadwal Kereta \n 3. Rail Food \n 4. Pesan E-Porter \n 5. Kritik dan Saran \n 6. Bantuan "
      )
      halo = input("> ")
      if halo.strip() == "1":
        pesan()
        break
      elif halo.strip() == "2":
        jadwal()
        break
      elif halo.strip() == "3":
        print("Mohon Maaf, Fitur Ini Belum Tersedia.")
        time.sleep(2)
        continue
      elif halo.strip() == "4":
        porter()
        break
      elif halo.strip() == "5":
        kritiksaran()
        break
      elif halo.strip() == "6":
        print("Petugas Kamu Akan Tiba Sebentar Lagi Untuk Menolong Anda")
        time.sleep(5)
        os.system("clear")
        continue
      else:
        print("Mohon Ulangi Input")
        time.sleep(2)
        continue

#memulai kode
intro()
