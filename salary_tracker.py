import csv
from datetime import datetime
#Program Salary Tracker
#Berfungsi untuk mencatat jam masuk dan pulang kerja, menghitung lama jam kerja, serta menghitung gaji berdasarkan jabatan dan lama jam kerja

def main(): #program utama
  print("==== Selamat Datang Di Program Presensi Karyawan PT Ngawi Sejahtera Makmur Sentosa ====")
  print("======================================================================================")
  database = ambil_data("data.csv")
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
            mulai_kerja(username, nama, jabatan_user)
            break
         elif indeks_menu == 2:
            selesai_kerja(username)
            break
         else:
            print("Masukkan kode menu yang benar (1/2)")

#subprogram
def ambil_data(filename):
  with open(filename, mode="r", encoding="utf-8-sig") as file:
    pembaca = csv.DictReader(file)
    return [row for row in pembaca]


def cek_waktu_saat_ini():
  return datetime.now()

def mulai_kerja(username, nama, jabatan):
   sekarang = cek_waktu_saat_ini()

   tanggal = sekarang.strftime("%Y-%m-%d")
   waktu_mulai = sekarang.strftime("%H:%M:%S")

   with open("data_waktu.csv", "r") as file:
      pembaca = csv.DictReader(file)

      for baris in pembaca:
         if baris["username"] == username and baris["tanggal"] == tanggal:
            print("Anda sudah melakukan presensi hari ini")
            return False

   with open("data_waktu.csv", "a", newline="") as file:
      penulis = csv.writer(file)
      penulis.writerow([nama, username, jabatan, tanggal, waktu_mulai, "", ""])

   print("Berhasil melakukan clock-in!")
   print("Waktu mulai:", waktu_mulai)
   return True

def selesai_kerja(username):
   sekarang = cek_waktu_saat_ini()

   tanggal = sekarang.strftime("%Y-%m-%d")
   waktu_selesai = sekarang.strftime("%H:%M:%S")

   with open("data_waktu.csv", "r") as file:
      pembaca = csv.DictReader(file)
      data = list(pembaca)

      for baris in data:
         if baris["username"] == username and baris["tanggal"] == tanggal:
            if baris["waktu_selesai"] != "":
              print("Anda sudah melakukan presensi hari ini")
              return False

            waktu_mulai = datetime.strptime(baris["waktu_mulai"], "%H:%M:%S")
            waktu_akhir = datetime.strptime(waktu_selesai, "%H:%M:%S")

            jam_kerja = (waktu_akhir - waktu_mulai).total_seconds() / 3600

            baris["waktu_selesai"] = waktu_selesai
            baris["jam_kerja"] = jam_kerja

            with open("data_waktu.csv", "w", newline="") as file:
                  penulis = csv.DictWriter(file, fieldnames=["nama", "username", "tanggal", "waktu_mulai", "waktu_selesai", "jam_kerja"])
                  penulis.writeheader()
                  penulis.writerows(data)

            print("Berhasil melakukan clock-out!")
            print("Waktu selesai:", waktu_selesai)
            print("Total jam kerja:", round(jam_kerja, 2), "jam")
            return True

   print("Anda belum melakukan clock-in hari ini!")
   return False

def cek_id(database):
  username = input("Masukkan user id anda: ")
  for data in database:
    if data["username"] == username:
      nama_user = data["nama"]
      indeks_user = int(data["nomor"])
      jabatan_user = data["jabatan"]
      return [True, indeks_user, username, nama_user, jabatan_user]
  print("Username tidak terdaftar!")
  return False

def cek_password(database, indeks):
  for kesempatan in range(3):
    password = input("Masukkan password: ")
    if password == database[indeks-1]["password"]:
      return True
    print("Password salah!")
  print("Anda sudah salah 3 kali! silahkan login ulang\nApabila Lupa, Hubungi admin untuk mengganti password")
  return False
   
main()

def edit_data():
  
def hapus_data():
  
def tambahkan_data():

def selesai_kerja():

def hitung_gaji():

def cek_gaji():
