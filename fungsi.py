#Mendefinisikan Fungsi Python
"""
Anda dapat menentukan fungsi untuk menyediakan fungsionalitas yang dibutuhkan. Berikut adalah aturan sederhana untuk mendefinisikan fungsi dengan Python.

-Fungsi blok dimulai dengan def kata kunci diikuti oleh nama fungsi dan tanda kurung (()).
-Setiap parameter masukan atau argumen harus ditempatkan di dalam tanda kurung ini. Anda juga dapat menentukan parameter di dalam tanda kurung ini.
-Pernyataan pertama dari sebuah fungsi dapat berupa pernyataan opsional - string dokumentasi fungsi atau docstring.
-Blok kode dalam setiap fungsi dimulai dengan titik dua (:) dan indentasi.
-Pernyataan kembali [ekspresi] keluar dari sebuah fungsi, secara opsional menyampaikan kembali ekspresi ke pemanggil. Pernyataan pengembalian tanpa argumen sama dengan return None.
"""
#Contoh fungsi

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   #return

def salam(nama):
    print("Hallo!")
    print("Selamat pagi", nama)
    print("Apa kabarmu hari ini?")

def BMII(berat, tinggi):
    print("BMII :",berat/(tinggi*tinggi))

def BMII2(berat, tinggi):
    return berat/(tinggi*tinggi) #menggunakan return hanya akan menghasilkan nilai

printme("Vikri")

salam("Vikri")
BMII(55,1.75)
BMII(tinggi=1.75,berat=55) # bisa dibalik urutannya tetapi harus diberi keterangan variable
BMII2(55,1.75)
