#tuple
"""
Sebuah tupel adalah urutan objek Python yang tidak berubah. 
Tupel adalah urutan, seperti daftar. 
Perbedaan utama antara tupel dan daftarnya adalah bahwa tupel tidak dapat diubah tidak seperti List Python. 
Tupel menggunakan tanda kurung, sedangkan List Python menggunakan tanda kurung siku.

Membuat tuple semudah memasukkan nilai-nilai yang dipisahkan koma. 
Secara opsional, Anda dapat memasukkan nilai-nilai yang dipisahkan koma ini di antara tanda kurung juga. 
Sebagai contoh :
"""
#Contoh sederhana pembuatan tuple pada bahasa pemrograman python

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
"""
Tupel kosong ditulis sebagai dua tanda kurung yang tidak berisi apa-apa, 
contohnya : tup1 = (); 
Untuk menulis tupel yang berisi satu nilai, Anda harus memasukkan koma, meskipun hanya ada satu nilai, 
contohnya : tup1 = (50,) Seperti indeks String, indeks tuple mulai dari 0, dan mereka dapat diiris, digabungkan, dan seterusnya
"""
#Akses Nilai Dalam Tuple Python

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

#Update Nilai Dalam Tuple Python
"""
Tuple tidak berubah, yang berarti Anda tidak dapat memperbarui atau mengubah nilai elemen tupel. 
Anda dapat mengambil bagian dari tupel yang ada untuk membuat tupel baru seperti ditunjukkan oleh contoh berikut.
"""
tupB1 = (12, 34.56)
tupB2 = ('abc', 'xyz')

    # Aksi seperti dibawah ini tidak bisa dilakukan pada tuple python
    # Karena memang nilai pada tuple python tidak bisa diubah
        # tup1[0] = 100;

    # Jadi, buatlah tuple baru sebagai berikut
tupB3 = tupB1 + tupB2
print (tupB3)

#Operasi Dasar Pada Tuple Python
"""
Tupel merespons operator + dan * sama seperti String; 
Mereka berarti penggabungan dan pengulangan di sini juga berlaku, kecuali hasilnya adalah tupel baru, bukan string.

Python Expression	                        Hasil	                                Penjelasan
len((1, 2, 3))	3	                                                                Length
(1, 2, 3) + (4, 5, 6)	                    (1, 2, 3, 4, 5, 6)	                    Concatenation
(‘Halo!’,) * 4	                            (‘Halo!’, ‘Halo!’, ‘Halo!’, ‘Halo!’)	Repetition
3 in (1, 2, 3)	                            True	                                Membership
for x in (1,2,3) : print (x, end = ‘ ‘)	    1 2 3	                                Iteration

"""

#ndexing, Slicing dan Matrix Pada Tuple Python
"""
Karena tupel adalah urutan, pengindeksan dan pengiris bekerja dengan cara yang sama untuk tupel seperti pada String, dengan asumsi masukan berikut

Dengan asumsi input berikut : T = ('C++', 'Java', 'Python')

Python Expression	Hasil	            Penjelasan
T[2]	            'Python'	        Offset mulai dari nol
T[-2]	            'Java'	            Negatif: hitung dari kanan
T[1:]	            ('Java', 'Python')	Slicing mengambil bagian
"""
#Fungsi Build-in Pada Tuple Python
"""
Python Function	        Penjelasan
cmp(tuple1, tuple2)	#   Tidak lagi tersedia dengan Python 3
len(tuple)	            Memberikan total panjang tuple.
max(tuple)	            Mengembalikan item dari tuple dengan nilai maks.
min(tuple)	            Mengembalikan item dari tuple dengan nilai min.
tuple(seq)	            Mengubah seq menjadi tuple.
"""
