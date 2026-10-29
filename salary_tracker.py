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
      data_utama_user = cek_user(database)
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
       if indeks_menu == 1:
          change_user_id = input("Masukkan id user yang ingin diedit: ")
       elif indeks_menu == 2:
          delete_user = input("Masukkan id user yang ingin dihapus: ")
       elif indeks_menu == 3:
          new_user_id = input("Masukkan id user yang ingin ditambahkan : ")
          new_user_name = input("Masukkan nama karyawan yang ingin ditambahkan : ")
          new_user_jabatan = input("Masukkan jabatan karyawan yang ingin ditambahkan : ")
          new_user_password = input("Buat password untuk akun ini: ")
                    

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
               hitung_gaji(database_waktu, database, username)
               simpan_data("data_waktu.csv", database_waktu)
               simpan_data("data.csv", database)
            break
         else:
            print("Masukkan kode menu yang benar (1/2)")
           
    lanjut_looping = input("Apa ada hal lain yang bisa dibantu?\n1. Ada\n2. Tidak Ada \nPilih menu: ")
    while lanjut_looping != "1" and lanjut_looping != "2":
       lanjut_looping = input("Masukkan kode yang benar!\nApa ada hal lain yang bisa dibantu?\n1. Ada\n2. Tidak Ada\nPilih menu: ")

    if lanjut_looping == "1":
       continue
    elif lanjut_looping == "2":
       print("Terima kasih telah menggunakan layanan ini :D")
       break

#subprogram
def ambil_data(filename):
  with open(filename, mode="r", encoding="utf-8-sig") as file:
    pembaca = csv.DictReader(file)
    return [row for row in pembaca]

def simpan_data(filename, database):
   with open(filename, "w", newline="") as file:
      penulis = csv.DictWriter(file, fieldnames=database[0].keys())
      penulis.writeheader()
      penulis.writerows(database)

def tambah_data(database):
   for i in range(len(database)):
      if database[i]["nomor"] == "":
         nomor = i + 1

         nama =  input("Masukkan nama karyawan: ")
         username = input("Masukkan username: ")

         for data in database:
            if data["username"] == username:
               print("Username sudah terdaftar!")
               return False

         password = input("Masukkan password: ")
         jabatan = input("Masukkan jabatan: ")
         gaji = input("Masukkan gaji: ")

         database[i] = {
            "nomor": str(nomor),
            "nama": nama,
            "username": username,
            "password": password,
            "jabatan": jabatan,
            "gaji": gaji
         }

         print("Karyawan berhasil ditambahkan!")

def edit_data(database):
   username = input("Masukkan username karyawan yang ingin diedit: ")

   for i in range(len(database)):
      if database[i]["username"] == username and username != "":
         print("Nama:", database[i]["nama"])
         print("Username:", database[i]["username"])
         print("Jabatan:", database[i]["jabatan"])
         print("Gaji:", database[i]["gaji"])

         print("\n1. Edit nama\n2. Edit username\n3. Edit password\n4. Edit jabatan\n5. Edit gaji")

         pilihan = input("Pilih data yang ingin diedit: ")

         if pilihan == "1":
            database[i["nama"]] = input("Masukkan nama baru: ")

         elif pilihan == "2":
            username_baru = input("Masukkan username baru: ")

            for j in range(len(database)):
               if database[j]["username"] == username_baru:
                  print("Username sudah terdaftar!")
                  return False

            database[i]["username"] = username_baru

         elif pilihan == "3":
            database[i]["password"] = input("Masukkan password baru: ")

         elif pilihan == "4":
            database[i]["jabatan"] = input("Masukkan jabatan baru: ")

         elif pilihan == "5":
            database[i]["gaji"] = input("Masukkan gaji baru: ")
         
         else:
            print("Pilihan tidak valid!")
            return False

         print("Data karyawan berhasil diperbarui!")
         return True
   
   print("Username tidak ditemukan!")
   return False

def hapus_data(database):
   username = input("Masukkan username karyawan yang ingin dihapus: ")

   for i in range(len(database)):
      if database[i]["username"] == username and username != "":
         print("Nama:", database[i]["nama"])
         print("Jabatan:", database[i]["jabatan"])

         konfirmasi = input("Yakin ingin menghapus karyawan ini? (y/n): ")

         if konfirmasi == "y":
            for j in range(i, len(database) - 1):
               database[j] = database[j + 1]

            database[len(database) - 1] = {
               "nomor": "",
               "nama": "",
               "username": "",
               "password": "",
               "jabatan": "",
               "gaji": ""
            }

            for j in range(len(database)):
               if database[j]["nama"] != "":
                  database[j]["nomor"] = str(j + 1)
            
            print("Data karyawan berhasil dihapus!")
            return True

         else:
            print("Penghapusan dibatalkan!")
            return False

   print("Username tidak ditemukan!")
   return False

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
         waktu_mulai = baris["waktu_mulai"]
         if baris["waktu_selesai"] != "":
            print("Anda sudah melakukan presensi selesai kerja hari ini")
            return False
         
         jam_kerja = hitung_jam_kerja (waktu_mulai, waktu_selesai)
         
         baris["waktu_selesai"] = waktu_selesai
         baris["jam_kerja"] = round(jam_kerja, 2)

         print("Berhasil melakukan clock-out!")
         print("Waktu selesai:", waktu_selesai)
         print("Total jam kerja:", round(jam_kerja, 2), "jam")
         return True

   print("Anda belum melakukan clock-in hari ini!")
   return False

def cek_user(database):
  username = input("Masukkan username anda: ")
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

def hitung_jam_kerja(waktu_mulai, waktu_selesai):
   # Menghitung jam kerja dari format "HH:MM"
   # KAMUS LOKAL
   # waktu_mulai, waktu_selesai : str

   waktu_mulai = datetime.strptime(waktu_mulai, "%H:%M:%S")
   waktu_akhir = datetime.strptime(waktu_selesai, "%H:%M:%S")
   menit = (waktu_akhir - waktu_mulai).total_seconds() / 60   # detik menjadi menit
   if menit < 0:                          # jika shift lewat tengah malam
           menit += 24 * 60 
   return menit / 60                   # menit menjadi jam

def hitung_gaji(database_waktu, database, username):
   # Menentukan gaji berdasarkan jabatan dan mengalikan total jam kerja dengan tarif per jam
   # KAMUS LOKAL
   # database : list of list, username : str, tarif_per_jam : int/float
   tarif_per_jam = 0
   for baris in database_waktu:
      if baris["jabatan"] == "General Manager":
         tarif_per_jam = 50000
      elif baris ["jabatan"] == "Manager":
         tarif_per_jam = 40000
      elif baris["jabatan"] == "Supervisor":
         tarif_per_jam = 30000
      elif baris["jabatan"] == "Staff":
         tarif_per_jam = 20000
      elif baris["jabatan"] == "Magang":
         tarif_per_jam = 10000
   total_jam = 0
   for baris in database_waktu:
        if baris["username"] == username:
            total_jam += float(baris["jam_kerja"])     # row[6] = jam_kerja
   gaji = total_jam * tarif_per_jam

   for baris in database:
      if baris["username"] == username:
         baris["gaji"] = str(int(baris["gaji"])+ gaji)
main()

def edit_data():
  return 0

def tambah_data():
  return 0
def hapus_data():
  return 0
