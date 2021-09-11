#PENGERTIAN DICTIONARY PYTHON
"""
Dictionary Python berbeda dengan List ataupun Tuple.
Karena setiap urutanya berisi key dan value. 
Setiap key dipisahkan dari value-nya oleh titik dua (:), item dipisahkan oleh koma, dan semuanya tertutup dalam kurung kurawal. 
Dictionary kosong tanpa barang ditulis hanya dengan dua kurung kurawal, seperti ini: {}.

Nilai kamus bisa berupa tipe apa pun, namun key harus berupa tipe data yang tidak berubah seperti string, angka, atau tupel.
"""

#AKSES NILAI DALAM DICTIONARY PYTHON
"""
Untuk mengakses elemen Dictionary, Anda dapat menggunakan tanda kurung siku yang sudah dikenal bersama dengan key untuk mendapatkan nilainya. 
Berikut adalah contoh sederhananya :
"""
    #Contoh cara membuat Dictionary pada Python
"""
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
"""

#UPDATE NILAI DALAM DICTIONARY PYTHON
"""
Anda dapat memperbarui Dictionary dengan menambahkan entri baru 
atau pasangan nilai kunci, memodifikasi entri yang ada, 
atau menghapus entri yang ada seperti ditunjukkan pada contoh sederhana yang diberikan di bawah ini.
"""
    #Update dictionary python
"""
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # Mengubah entri yang sudah ada
dict['School'] = "DPS School" # Menambah entri baru
dict['city'] = "Bogor" # coba nambah entri baru

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
print ("dict['city']: ", dict['city']) 

print(dict) # untuk menampilkan dict seluruhnya
"""

#HAPUS ELEMEN DICTIONARY PYTHON
"""
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # hapus entri dengan key 'Name'
dict.clear()     # hapus semua entri di dict
del dict         # hapus dictionary yang sudah ada

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

"""
# FUNGSI Build-in PADA DICTIONARY PYTHON
"""
Fungsi Python	    Penjelasan
cmp(dict1, dict2)	Membandingkan unsur keduanya.
len(dict)	        Memberikan panjang total Dictionary. Ini sama dengan jumlah item dalam Dictionary.
str(dict)	        Menghasilkan representasi string yang dapat dicetak dari Dictionary
type(variable)	    Mengembalikan tipe variabel yang lulus. Jika variabel yang dilewatkan adalah Dictionary, maka akan mengembalikan tipe Dictionary.
"""
# Method Build-in Pada Dictionary Python
"""
Method Python	                        Penjelasan
dict.clear()	                        Menghapus semua elemen Dictionary
dict.copy()	                            Mengembalikan salinan Dictionary
dict.fromkeys()	                        Buat Dictionary baru dengan kunci dari seq dan nilai yang disetel ke nilai.
dict.get(key, default=None)	            For key, nilai pengembalian atau default jika tombol tidak ada dalam Dictionary
dict.has_key(key)	                    Mengembalikan true jika key dalam Dictionary, false sebaliknya
dict.items()	                        Mengembalikan daftar dari pasangan tuple dictionary (key, value)
dict.keys()	                            Mengembalikan daftar key dictionary
dict.setdefault(key, default=None)	    Mirip dengan get (), tapi akan mengatur dict [key] = default jika kunci belum ada di dict
dict.update(dict2)	                    Menambahkan pasangan kunci kata kunci dict2 ke dict
dict.values()	                        Mengembalikan daftar nilai dictionary
"""
