import csv
from datetime import datetime
#Program Salary Tracker
#Berfungsi untuk mencatat jam masuk dan pulang kerja, menghitung lama jam kerja, serta menghitung gaji berdasarkan jabatan dan lama jam kerja

def main(): #program utama
  database = ambil_data("data.csv")
  while True:
    lanjut_ke_pin = False #keadaan dasar
    lanjut_ke_absen = False #keadaan dasar

  while lanjut_ke_pin == False:
    data_utama_user = cek_id(database)
    if data_utama_user != False:
      lanjut_ke_pin = data_utama_user[0]
      indeks_user = data_utama_user[1]
      nama_user = data_utama_user[2]
      jabatan_user = data_utama_user[3]
  

#subprogram
def ambil_data(filename):
  with open(filename, mode="r", encoding="utf-8-sig") as file:
  pembaca = csv.DictReader(file)
  return [row for row in pembaca]

def cek_waktu_saat_ini():
  return datetime.now()

def mulai_kerja(username, nama):
   sekarang = cek_waktu_saat_ini

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
      penulis.writerow([nama, username, tanggal, waktu_mulai, "", ""])

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
      indeks_user =data["nomor"]
      jabatan_user = data["jabatan"]
      return [True, indeks_user, nama_user, jabatan_user]
  print("Username tidak terdaftar!")
  return False

def cek_password(database, indeks):
  for kesempatan in range(3):
       password = input("Masukkan password: ")
  
       if password == database[indeks][2]:
          return True
  
       print("Password salah!")

  print("Anda sudah salah 3 kali!")
  return False

def edit_data():
  

def hapus_data():
  

def tambahkan_data():

def selesai_kerja():

def hitung_gaji():

def cek_gaji():
