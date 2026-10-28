import csv
from datetime import datetime
#Program Salary Tracker
#Berfungsi untuk mencatat jam masuk dan pulang kerja, menghitung lama jam kerja, serta menghitung gaji berdasarkan jabatan dan lama jam kerja

def main(): #program utama
  print("==== Selamat Datang Di Program Presensi Karyawan PT Ngawi Sejahtera Makmur Sentosa ====")
  print("======================================================================================")
  database = ambil_data("data.csv")
  database_waktu = ambil_data("data_waktu.csv")
  while True:
    lanjut_ke_pin = False #keadaan dasar
    lanjut_ke_absen = False #keadaan dasar

    while lanjut_ke_pin == False:
      data_utama_user = cek_id(database)
      if data_utama_user != False:
         lanjut_ke_pin = data_utama_user[0]
         indeks_user = data_utama_user[1]
         username = data_utama_user[2]
         nama = data_utama_user[3]
         jabatan_user = data_utama_user[4]

    while lanjut_ke_absen == False:
       lanjut_ke_absen = cek_password(database, indeks_user)

    if lanjut_ke_absen == True:
       print("Login berhasil!\n")

    if nama == "Admin":
       indeks_menu = int(input("Selamat datang di menu Admin, apa yang ingin anda lakukan?\n1. Edit data karyawan\n2. Hapus data karyawan\n3. Tambahkan karyawan baru\n4. Cek gaji\nPilih menu: "))

    else:
      print(f"Selamat datang {nama}, apa yang ingin anda lakukan?\n1. Presensi mulai kerja\n2. Presensi selesai kerja")

      while True:
         indeks_menu = int(input("Pilih menu: "))
         if indeks_menu == 1:
            if mulai_kerja(database_waktu, username, nama, jabatan_user):
               simpan_data("data_waktu.csv", database_waktu)
            break
         elif indeks_menu == 2:
            if selesai_kerja(database_waktu, username):
               simpan_data("data_waktu.csv", database_waktu)
            break
         else:
            print("Masukkan kode menu yang benar (1/2)")

#subprogram
def ambil_data(filename):
  with open(filename, mode="r", encoding="utf-8-sig") as file:
    pembaca = csv.DictReader(file)
    return [row for row in pembaca]

def tambah_data(database):

def simpan_data(filename, database):
   with open(filename, "w", newline="") as file:
      penulis = csv.DictWriter(file, fieldnames=database[0].keys())
      penulis.writeheader()
      penulis.writerows(database)

def cek_waktu_saat_ini():
  return datetime.now()

def mulai_kerja(database_waktu, username, nama, jabatan):
   sekarang = cek_waktu_saat_ini()

   tanggal = sekarang.strftime("%Y-%m-%d")
   waktu_mulai = sekarang.strftime("%H:%M:%S")

   for baris in database_waktu:
      if baris["username"] == username and baris["tanggal"] == tanggal:
         print("Anda sudah melakukan presensi hari ini")
         return False

   for i in range(len(database_waktu)):
      if database_waktu[i]["username"] == "":
         database_waktu[i] = {
            "nama": nama,
            "username": username,
            "jabatan": jabatan,
            "tanggal": tanggal,
            "waktu_mulai": waktu_mulai,
            "waktu_selesai": "",
            "jam_kerja": ""
         }

         print("Berhasil melakukan clock-in!")
         print("Waktu mulai:", waktu_mulai)
         return True

   print("Database presensi sudah penuh!")
   return False

def selesai_kerja(database_waktu, username):
   sekarang = cek_waktu_saat_ini()

   tanggal = sekarang.strftime("%Y-%m-%d")
   waktu_selesai = sekarang.strftime("%H:%M:%S")

   for baris in database_waktu:
      if baris["username"] == username and baris["tanggal"] == tanggal:

         if baris["waktu_selesai"] != "":
            print("Anda sudah melakukan presensi selesai kerja hari ini")
            return False

         waktu_mulai = datetime.strptime(baris["waktu_mulai"], "%H:%M:%S")
         waktu_akhir = datetime.strptime(waktu_selesai, "%H:%M:%S")

         jam_kerja = (waktu_akhir - waktu_mulai).total_seconds() / 3600

         baris["waktu_selesai"] = waktu_selesai
         baris["jam_kerja"] = round(jam_kerja, 2)

         print("Berhasil melakukan clock-out!")
         print("Waktu selesai:", waktu_selesai)
         print("Total jam kerja:", round(jam_kerja, 2), "jam")
         return True

   print("Anda belum melakukan clock-in hari ini!")
   return False

def cek_id(database):
  username = input("Masukkan user id anda: ")
  for i in range(len(database)):
    if database[i]["username"] == username and username != "":
      nama_user = database[i]["nama"]
      jabatan_user = database[i]["jabatan"]
      return [True, i, username, nama_user, jabatan_user]
  print("Username tidak terdaftar!")
  return False

def cek_password(database, indeks):
  for kesempatan in range(3):
    password = input("Masukkan password: ")
    if password == database[indeks]["password"]:
      return True
    print("Password salah!")
  print("Anda sudah salah 3 kali! silahkan login ulang\nApabila Lupa, Hubungi admin untuk mengganti password")
  return False

main()

def edit_data():
  
def hapus_data():

def hitung_gaji():

def cek_gaji():
