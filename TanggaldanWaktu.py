
#https://belajarpython.com/tutorial/tanggal-waktu-python
# PENGERTIAN
"""
Program Python dapat menangani tanggal dan waktu dengan beberapa cara. 
Konversi antara format tanggal adalah tugas umum untuk komputer. 
Modul waktu dan kalender Python melacak tanggal dan waktu.
"""

# Apa itu Tick?
"""
Interval waktu adalah bilangan floating-point dalam satuan detik. Instansi tertentu dalam waktu dinyatakan dalam hitungan detik sejak pukul 12:00 1 Januari 1970.

Dibawah ini adalah contoh penggunanaya.

import time; # Digunakan untuk meng-import modul time

ticks = time.time()
print ("Berjalan sejak 12:00am, January 1, 1970:", ticks)
"""

# Apa itu TimeTuple Python?
"""
Index   Field	              Value
0	      4-digit year	      2008
1	      Bulan	              1 sampai 12
2	      Hari	              1 sampai 31
3	      Jam	                0 sampai 23
4	      Menit	              0 sampai 59
5	      Detik	              0 sampai 61
6	      Hari dalam Minggu	  0 sampai 6 (0 adalah Senin)
7	      Hari dalam Bulan	  1 sampai 366
8	      Daylight savings	  -1, 0, 1, -1 means library determines DST

Tuple di atas setara dengan struktur struct_time. 
Struktur ini memiliki atribut berikut

Index	  Atribut     Value
0	      tm_year	    2008
1	      tm_mon  	  1 sampai 12
2	      tm_mday	    1 sampai 31
3	      tm_hour	    0 sampai 23
4	      tm_min	    0 sampai 59
5	      tm_sec	    0 sampai 61
6	      tm_wday	    0 sampai 6 (0 adalah Senin)
7	      tm_yday	    1 sampai 366
8	      tm_isdst	  -1, 0, 1, -1 means library determines DST
"""

#Mendapatkan Waktu Saat Ini
"""
Untuk menerjemahkan waktu instan dari satu detik sejak nilai floating-point ke waktu menjadi tupel waktu, lewati nilai floating-point ke fungsi (mis., Localtime) yang mengembalikan waktu tupel dengan semua sembilan item valid.

import time;

localtime = time.localtime(time.time())
print ("Waktu lokal saat ini :", localtime)
"""

#Mendapatkan Waktu yang berformat
"""
Anda dapat memformat kapan saja sesuai kebutuhan Anda, namun metode sederhana untuk mendapatkan waktu dalam format yang mudah dibaca adalah asctime ()
"""
import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Waktu lokal saat ini :", localtime)

#Mendapatkan kalender dalam sebulan
"""
Modul kalender memberikan berbagai macam metode untuk dimainkan dengan kalender tahunan dan bulanan. Di sini, kami mencetak kalender untuk bulan tertentu (Jan 2008)
"""
import calendar;

cal = calendar.month(2008, 1)
print ("Dibawah ini adalah kalender:")
print (cal)

#MODUL TIME DAN MODUL CALENDARN PADA PYTHON
###
