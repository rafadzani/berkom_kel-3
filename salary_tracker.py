import csv
from datetime import datetime
#Program Salary Tracker
#Berfungsi untuk mencatat jam masuk dan pulang kerja, menghitung lama jam kerja, serta menghitung gaji berdasarkan jabatan dan lama jam kerja

def main() #program utama

#subprogram
def ambil_data()

def cek_waktu_saat_ini():
  return datetime.now()

def mulai_kerja():
  sekarang = cek_waktu_saat_ini()
  
  tanggal = sekarang.strftime("%Y-%m-%d")
  waktu_mulai = sekarang.strftime("%H:%M:%S
  
  with open("data_waktu.csv", "a", newline="") as file:
    penulis = csv.writer(file)
    penulis.writerow([username, jabatan, tanggal, waktu_mulai, "", ""])

  print("Berhasil melakukan clock-in!")
  print("Waktu mulai:", waktu_mulai)

def cek_id()

def cek_password()

def edit_data()

def hapus_data()

def tambahkan_data()

def selesai_kerja()

def hitung_gaji()

def cek_gaji()
