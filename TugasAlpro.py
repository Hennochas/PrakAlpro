#Nama : Hennoch Azarya Saragih
#Universitas Kristen Duta Wacana 
#Sumber Soal : https://saintif.com/rumus-percepatan-2/

''' Diketahui sebuah mobil melaju dengan kecepatan awal yaitu 10 m/s.
Setelah mobil melaju 10 sekon, kecepatan mobil tersebut bertambah menjadi 30 m/s.
Berapa percepatan yang dimiliki oleh mobil tersebut ?
Rumus : a = (v2-v1)/(t2-t1)

a = percepatan
v1 = kecepatan awal
v2 = kecepatan akhir
t1 = waktu awal
t2 = waktu akhir
'''

'''
Input : 
v1 = 10
v2 = 30
t1 = 0
t2 = 10

Proses:
a = (30-10)/(30-0)

Output :
percepatan yang dimiliki mobil adalah...
'''
v1 = int(input("Masukkan Kecepatan Awal = "))
v2 = int(input("Masukkan Kecepatan Akhir = "))
t1 = int(input("Masukkan Waktu awal = "))
t2 = int(input("Masukkan Waktu Akhir = "))

rumus = (v2-v1)/(t2-t1)

print("jadi Nilai Percepatannya adalah ", rumus, "m/s^2")

