#contoh sederhana pembuatan List
list11 = ['kimia', 'fisika', 1993, 2017]
list22 = [1, 2, 3, 4, 5 ]
list33 = ["a", "b", "c", "d"]

#Cara mengakses nilai di dalam list Python

list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#update nilai pada List
#Anda dapat memperbarui satu atau beberapa nilai di dalam list dengan memberikan potongan di sisi kiri 
#operator penugasan, dan Anda dapat menambahkan nilai ke dalam list dengan metode append (). 
#Sebagai contoh :
list = ['fisika', 'kimia', 1993, 2017]
print ("Nilai ada pada index 2 : ", list[2])

list[2] = 2001
print ("Nilai baru ada pada index 2 : ", list[2])

#cara menghapus nilai dalam List python
#Untuk menghapus nilai di dalam list python, 
#Anda dapat menggunakan salah satu pernyataan del jika Anda tahu persis elemen yang Anda hapus. 
#Anda dapat menggunakan metode remove() jika Anda tidak tahu persis item mana yang akan dihapus. 
#Sebagai contoh :

#Contoh cara menghapus nilai pada list python

list = ['fisika', 'kimia', 1993, 2017]

print (list)
del list[2]
print ("Setelah dihapus nilai pada index 2 : ", list)
