import csv
from datetime import datetime
#Program Salary Tracker
#Berfungsi untuk mencatat jam masuk dan pulang kerja, menghitung lama jam kerja, serta menghitung gaji berdasarkan jabatan dan lama jam kerja

def main(): #Program Utama
    # Menjalankan tampilan utama Salary Tracker
    # KAMUS LOKAL
    # database, database_waktu : list of dict; data_utama_user : list atau bool; indeks_user : int; indeks_menu, lanjut_looping, username, nama, jabatan_user : str
    print("==== Selamat Datang Di Program Presensi Karyawan PT Ngawi Sejahtera Makmur Sentosa ====")
    print("=======================================================================================")

    database = ambil_data("data.csv")
    database_waktu = ambil_data("data_waktu.csv")

    while True:
        while True:
            data_utama_user = cek_user(database)

            if data_utama_user != False:
                indeks_user = data_utama_user[1]
                username = data_utama_user[2]
                nama = data_utama_user[3]
                jabatan_user = data_utama_user[4]

                if cek_password(database, indeks_user):
                    print("Login berhasil!\n")
                    break

        if nama == "Admin":
            while True:
                print("=======================================================================================")
                print("Selamat datang di menu Admin, apa yang ingin anda lakukan?")
                print("1. Edit data karyawan")
                print("2. Hapus data karyawan")
                print("3. Tambahkan karyawan baru")
                print("4. Cek gaji")

                indeks_menu = input("Pilih menu: ")

                if indeks_menu == "1":
                    print("=======================================================================================")
                    print("Selamat datang di menu pengeditan data karyawan")
                    edit_data(database, database_waktu)
                    simpan_data("data.csv", database)
                    simpan_data("data_waktu.csv", database_waktu)
                    break

                elif indeks_menu == "2":
                    print("=======================================================================================")
                    print("Selamat datang di menu penghapusan data karyawan")
                    hapus_data(database)
                    simpan_data("data.csv", database)
                    break

                elif indeks_menu == "3":
                    print("=======================================================================================")
                    print("Selamat datang di menu penambahan data karyawan")
                    tambah_data(database)
                    simpan_data("data.csv", database)
                    break

                elif indeks_menu == "4":
                    print("=======================================================================================")
                    print("Selamat datang di menu pengecekan gaji karyawan")
                    cek_gaji(database)
                    break

                else:
                    print("Masukkan kode menu yang benar (1/2/3/4)")

        else:
            print("=======================================================================================")
            print(f"Selamat datang {nama}, apa yang ingin anda lakukan?")
            print("1. Presensi mulai kerja")
            print("2. Presensi selesai kerja")

            while True:
                indeks_menu = input("Pilih menu: ")

                if indeks_menu == "1":
                    if mulai_kerja(database_waktu, username, nama, jabatan_user):
                        simpan_data("data_waktu.csv", database_waktu)
                    break

                elif indeks_menu == "2":
                    presensi = selesai_kerja(database_waktu, username)

                    if presensi != False:
                        if hitung_gaji(presensi, database, username):
                           simpan_data("data_waktu.csv", database_waktu)
                           simpan_data("data.csv", database)
                    break

                else:
                    print("Masukkan kode menu yang benar (1/2)")

        print("=======================================================================================")
        lanjut_looping = input("Apa ada hal lain yang bisa dibantu?\n1. Ada\n2. Tidak Ada\nPilih menu: ")

        while lanjut_looping != "1" and lanjut_looping != "2":
            lanjut_looping = input("Masukkan kode yang benar!\nApa ada hal lain yang bisa dibantu?\n1. Ada\n2. Tidak Ada\nPilih menu: ")

        if lanjut_looping == "1":
            continue
        elif lanjut_looping == "2":
            print("Terima kasih telah menggunakan layanan ini :D")
            break

#subprogram
def ambil_data(filename):
  # Membaca file CSV dan mengambil datanya
  # KAMUS LOKAL
  # filename : str; pembaca : DictReader
  with open(filename, mode="r", encoding="utf-8-sig") as file:
    pembaca = csv.DictReader(file)
    return [row for row in pembaca]

def simpan_data(filename, database):
   # Menyimpan perubahan yang dilakukan terhadap database
   # KAMUS LOKAL
   # filename : str; database : list of dict; penulis : DictWriter
   if len(database) == 0:
      print("Database kosong, tidak ada data yang disimpan!")
      return False

   with open(filename, "w", newline="") as file:
      penulis = csv.DictWriter(file, fieldnames=database[0].keys())
      penulis.writeheader()
      penulis.writerows(database)

   return True

def cek_user(database):
  # Meminta input username lalu mencocokkannya dengan database
  # KAMUS LOKAL
  # database : list of dict; username, nama_user, jabatan_user : str; i : int
  username = input("Masukkan username anda: ")
  for i in range(len(database)):
    if database[i]["username"] == username and username != "":
      nama_user = database[i]["nama"]
      jabatan_user = database[i]["jabatan"]
      return [True, i, username, nama_user, jabatan_user]
  print("Username tidak terdaftar!")
  return False

def cek_password(database, indeks):
  # Meminta input password lalu mencocokkannya dengan database
  # KAMUS LOKAL
  # database : list of dict; indeks, kesempatan : int; password : str
  for kesempatan in range(3):   # User diberi 3 kali percobaan/kesempatan
    password = input("Masukkan password: ")
    if password == database[indeks]["password"]:
      return True
    print("Password salah!")
  print("Anda sudah salah 3 kali! silahkan login ulang\nApabila Lupa, Hubungi admin untuk mengganti password")
  return False

def tambah_data(database):
   # Menambah data karyawan baru dalam database
   # KAMUS LOKAL
   # database : list of dict; nama, username, password, jabatan, gaji, pilihan : str; i, nomor : int; sudah_ada : bool
   for i in range(len(database)):
      if database[i]["nomor"] == "":
         nomor = i + 1

         nama =  input("Masukkan nama karyawan: ")
         while nama == "":
            nama = input("Nama tidak boleh kosong! Masukkan nama: ")

         username = input("Masukkan username: ")
         while True:
            if username == "":
               print("Username tidak boleh kosong!")
            else:
               sudah_ada = False
               for data in database:
                  if data["username"] == username:
                     sudah_ada = True
                     break

               if sudah_ada == False:
                  break

               print("Username sudah terdaftar!")

            username = input("Masukkan username baru: ")

         password = input("Masukkan password: ")
         while password == "":
            password = input("Password tidak boleh kosong! Masukkan password: ")

         print("1. General Manager\n2. Manager\n3. Supervisor\n4. Staff\n5. Magang")
         pilihan = input("Pilih jabatan: ")

         while pilihan not in ["1", "2", "3", "4", "5"]:
            pilihan = input("Pilihan tidak valid! Pilih jabatan (1-5): ")

         if pilihan == "1":
            jabatan = "General Manager"
         elif pilihan == "2":
            jabatan = "Manager"
         elif pilihan == "3":
            jabatan = "Supervisor"
         elif pilihan == "4":
            jabatan = "Staff"
         else:
            jabatan = "Magang"

         gaji = input("Masukkan gaji awal: ")
         while not gaji.isdigit():
            gaji = input("Gaji harus berupa angka! Masukkan gaji awal: ")

         database[i] = {
            "nomor": str(nomor),
            "nama": nama,
            "username": username,
            "password": password,
            "jabatan": jabatan,
            "gaji": gaji
         }

         print("Karyawan berhasil ditambahkan!")
         return True
   print("Database karyawan sudah penuh!")
   return False

def edit_data(database, database_waktu):
   # Mengedit/mengubah profil data karyawan yang sudah ada di dalam database
   # KAMUS LOKAL
   # database, database_waktu : list of dict; username, pilihan, nama_baru, username_baru, password_baru, jabatan_baru, gaji_baru : str; sudah_ada : bool
   username = input("Masukkan username karyawan yang ingin diedit: ")

   for i in range(len(database)):
      if database[i]["username"] == username and username != "":
         print("Nama:", database[i]["nama"])
         print("Username:", database[i]["username"])
         print("Jabatan:", database[i]["jabatan"])
         print("Gaji:", database[i]["gaji"])

         print("\n1. Edit nama\n2. Edit username\n3. Edit password\n4. Edit jabatan\n5. Edit gaji")
         pilihan = input("Pilih data yang ingin diedit: ")

         if pilihan == "1":   # Edit nama
            nama_baru = input("Masukkan nama baru: ")
            while nama_baru == "":
               nama_baru = input("Nama tidak boleh kosong! Masukkan nama baru: ")
            database[i]["nama"] = nama_baru

         elif pilihan == "2":   # Edit username
            while True:
               username_baru = input("Masukkan username baru: ")

               if username_baru == "":
                  print("Username tidak boleh kosong!")
                  continue

               sudah_ada = False
               for j in range(len(database)):
                  if j != i and database[j]["username"] == username_baru:
                     sudah_ada = True
                     break

               if sudah_ada == False:
                  for baris in database_waktu:
                     if baris["username"] == username:
                        baris["username"] = username_baru

                  database[i]["username"] = username_baru
                  break

               print("Username sudah terdaftar!")

         elif pilihan == "3":   # Edit password
            password_baru = input("Masukkan password baru: ")
            while password_baru == "":
               password_baru = input("Password tidak boleh kosong! Masukkan password baru: ")
            database[i]["password"] = password_baru

         elif pilihan == "4":   # Edit jabatan
            print("1. General Manager\n2. Manager\n3. Supervisor\n4. Staff\n5. Magang")
            jabatan_baru = input("Pilih jabatan baru: ")

            while jabatan_baru not in ["1", "2", "3", "4", "5"]:
               jabatan_baru = input("Pilihan tidak valid! Pilih jabatan (1-5): ")

            if jabatan_baru == "1":
               database[i]["jabatan"] = "General Manager"
            elif jabatan_baru == "2":
               database[i]["jabatan"] = "Manager"
            elif jabatan_baru == "3":
               database[i]["jabatan"] = "Supervisor"
            elif jabatan_baru == "4":
               database[i]["jabatan"] = "Staff"
            else:
               database[i]["jabatan"] = "Magang"

         elif pilihan == "5":   # Edit gaji
            gaji_baru = input("Masukkan gaji baru: ")
            while not gaji_baru.isdigit():
               gaji_baru = input("Gaji harus berupa angka! Masukkan gaji baru: ")
            database[i]["gaji"] = gaji_baru

         else:
            print("Pilihan tidak valid!")
            return False

         print("Data karyawan berhasil diperbarui!")
         return True

   print("Username tidak ditemukan!")
   return False

def hapus_data(database):
   # Meminta input username lalu menghapus data karyawan dari database
   # KAMUS LOKAL
   # database : list of dict; username, konfirmasi : str; i, j : int
   username = input("Masukkan username karyawan yang ingin dihapus: ")

   for i in range(len(database)):
      if database[i]["username"] == username and username != "":
         print("Nama:", database[i]["nama"])
         print("Jabatan:", database[i]["jabatan"])

         konfirmasi = input("Yakin ingin menghapus karyawan ini? (y/n): ")

         if konfirmasi == "y":
            for j in range(i, len(database) - 1):
               database[j] = database[j + 1]

            database[len(database) - 1] = {   # Mengosongkan slot terakhir setelah data digeser
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

def cek_gaji(database):
   # Meminta input username lalu mengambil data total gaji karyawan tersebut
   # KAMUS LOKAL
   # database : list of dict; username : str; i : int
   username = input("Masukkan username karyawan yang gajinya ingin di cek: ")

   for i in range(len(database)):
      if database[i]["username"] == username and username != "":
         print(database[i]["nama"], "memiliki total gaji senilai: ", end="")
         cetak_rupiah(int(database[i]["gaji"]))
         return True
   print("Username tidak ditemukan!")
   return False

def cetak_rupiah(gaji):
   # Menampilkan nominal gaji dalam format rupiah dengan pemisah ribuan
   # KAMUS LOKAL
   # gaji, panjang, i : int; nominal : str
   nominal = str(gaji)
   panjang = len(nominal)

   for i in range(panjang):
      if i == 0:
         print(f"Rp{nominal[i]}", end="")
      elif (panjang - i) % 3 == 0:
         print(f".{nominal[i]}", end="")
      else:
         print(nominal[i], end="")

   print()

def cek_waktu_saat_ini():
  # Mengambil tanggal dan jam saat ini dari sistem komputer
  # KAMUS LOKAL : (tidak ada)
  return datetime.now()

def mulai_kerja(database_waktu, username, nama, jabatan):
   # Menjalankan fungsi presensi mulai kerja dengan mencatat waktu mulai ke dalam database_waktu
   # KAMUS LOKAL
   # database_waktu : list of dict; username, nama, jabatan, tanggal, waktu_mulai : str; sekarang : datetime; i : int
   sekarang = cek_waktu_saat_ini()

   tanggal = sekarang.strftime("%Y-%m-%d")
   waktu_mulai = sekarang.strftime("%H:%M:%S")

   for baris in database_waktu:
      if baris["username"] == username and baris["tanggal"] == tanggal:   # Mengecek apakah user sudah presensi pada hari tersebut
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
   # Menjalankan fungsi presensi selesai kerja dengan mencatat waktu selesai dan menampilkan total jam kerja
   # KAMUS LOKAL
   # database_waktu : list of dict; username, waktu_mulai, waktu_selesai : str; sekarang : datetime; jam_kerja : float
   sekarang = cek_waktu_saat_ini()
   waktu_selesai = sekarang.strftime("%H:%M:%S")

   for baris in database_waktu:
      if baris["username"] == username and baris["waktu_selesai"] == "" and baris["waktu_mulai"] != "":
         waktu_mulai = baris["waktu_mulai"]
         jam_kerja = hitung_jam_kerja (waktu_mulai, waktu_selesai)
         
         baris["waktu_selesai"] = waktu_selesai
         baris["jam_kerja"] = round(jam_kerja, 2)

         print("Berhasil melakukan clock-out!")
         print("Waktu selesai:", waktu_selesai)
         print("Total jam kerja:", round(jam_kerja, 2), "jam")
         return baris

   for baris in database_waktu:
      if baris["username"] == username and baris["waktu_selesai"] != "":
         print("Anda sudah melakukan clock-out!")
         return False

   print("Anda belum melakukan clock-in!")
   return False


def hitung_jam_kerja(waktu_mulai, waktu_selesai):
   # Menghitung jam kerja dari format "HH:MM:SS"
   # KAMUS LOKAL
   # waktu_mulai, waktu_selesai : str (parameter); waktu_mulai, waktu_akhir : datetime (setelah konversi); menit : float
   # Menghitung jam kerja dari format "HH:MM"
   # KAMUS LOKAL
   # waktu_mulai, waktu_selesai : str

   waktu_mulai = datetime.strptime(waktu_mulai, "%H:%M:%S")
   waktu_akhir = datetime.strptime(waktu_selesai, "%H:%M:%S")
   menit = (waktu_akhir - waktu_mulai).total_seconds() / 60   # Mengubah selisih waktu dari detik menjadi menit   # detik menjadi menit
   if menit < 0:   # Jika shift melewati tengah malam                          # jika shift lewat tengah malam
           menit += 24 * 60 
   return menit / 60   # Mengubah menit menjadi jam                   # menit menjadi jam

def hitung_gaji(presensi, database, username):
   # Menentukan gaji berdasarkan jabatan dan mengalikan total jam kerja dengan tarif per jam
   # KAMUS LOKAL
   # presensi : dict; database : list of dict; username, jabatan : str; tarif_per_jam, gaji_sebelumnya : int; total_jam, total_gaji_baru : float
   # Menentukan gaji berdasarkan jabatan dan mengalikan total jam kerja dengan tarif per jam
   # KAMUS LOKAL
   # database : list of list, username : str, tarif_per_jam : int/float, total_gaji_lama : float, total_gaji_baru = int.
   tarif_per_jam = 0
   jabatan = presensi["jabatan"]
   
   if jabatan == "General Manager":
      tarif_per_jam = 200000
   elif jabatan == "Manager":
      tarif_per_jam = 150000
   elif jabatan == "Supervisor":
      tarif_per_jam = 100000
   elif jabatan == "Staff":
      tarif_per_jam = 50000
   elif jabatan == "Magang":
      tarif_per_jam = 25000

   if tarif_per_jam == 0:
      print("Jabatan tidak valid!")
      return False

   total_jam = float(presensi["jam_kerja"])
   total_gaji_baru = total_jam * tarif_per_jam

   for baris in database:
      if baris["username"] == username:
         gaji_sebelumnya = int(baris["gaji"])
         baris["gaji"] = str(int(total_gaji_baru + gaji_sebelumnya))
         print("Gaji berhasil ditambahkan!")
         return True

   print("Data karyawan tidak ditemukan!")
   return False

main()
