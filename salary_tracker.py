import csv
from datetime import datetime
#Program Salary Tracker
#Berfungsi untuk mencatat jam masuk dan pulang kerja, menghitung lama jam kerja, serta menghitung gaji berdasarkan jabatan dan lama jam kerja

def main(): #program utama
  database = ambil_data("data.csv")
  

#subprogram
def ambil_data(filename):
  database = []
  with open(filename) as file:
    pembaca = csv.DictReader(file)
    database = [row for row in pembaca]
  return[database]

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

def cek_id(database):
  username = input("Masukkan username: ")

  for i in range(len(database)):
       if username == database[i][1]:
          return i
       
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
