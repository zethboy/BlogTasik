# Buat file baru bernama control_flow.py di folder belajar python.
# Masukkan salah satu contoh kode di atas dan jalankan.
# Kalau sudah, coba kreasikan sendiri (misalnya, program untuk memeriksa bilangan ganjil/genap)

# program untuk memeriksa bilangan genap atau ganjil

# angka = int(input("Masukan angka :"))
# if angka % 2 == 0:
#   print(f"{angka} adalah bilangan genap")
# else:
#   print(f"{angka} adalah bilangan ganjil")
 


# Buat list berisi nama 3 temanmu, tambahkan 1 nama, lalu hapus 1 nama.
# Buat dictionary untuk menyimpan informasi (nama, umur, dan hobi) dan tambahkan 1 informasi baru.
# Buat set berisi angka 1-5, tambahkan angka 6, lalu cek hasilnya.


# teman = ["iweuh", "adot", "emon"]
# print(teman)

# teman.append("rakka")
# print(teman)

# teman.remove("iweuh")
# print(teman)

# pribadi = {"nama": "Yogi", "umur": 18, "hobi": "ngeband"}
# print(pribadi)

# pribadi["tinggi"] = 167
# print(pribadi)

# angka = {1, 2, 3, 4, 5}
# print(angka)

# angka.add(6)
# print(angka)


# Buat fungsi untuk menghitung keliling lingkaran (dengan parameter jari-jari).
# Buat fungsi untuk menampilkan pesan sambutan (dengan parameter nama dan pesan default: "Selamat datang!").
# Buat fungsi rekursif untuk menghitung bilangan pangkat (contoh: 2^3 = 8).

# def keliling(pi, r):
#   return 2 * pi * r 

# hasil = keliling(22/7, 7)
# print (f"hasil dari keliling lingkaran adalah {hasil}")

# def pesan_sambutan(nama, pesan = "Selamat Datang!"):
#   print(f"hai {nama}, {pesan} di acara kami")

# pesan_sambutan("Yogi")

# def pangkat(m, n):
#   if n == 0:
#     return 1
#   else:
#     return m * pangkat (m, n - 1)
# print(pangkat(2, 3))

# latihan konversi suhu temperatur
#  konversi celcius ke satuan lain
# celcius = float(input("masukan suhu celcius :"))
# print("suhu adalah :", celcius, "celcius")

# reamur = (4/5) * celcius
# print("suhu dalam reamur adalah ", reamur, "reamur")

# fahrenheit = ((9/5) * celcius) + 32
# print("suhu dalam fahrenheit adalah ", fahrenheit, "fahrenheit")

# kelvin = celcius + 273
# print("suhu dalam kelvin adalah ", kelvin, "kelvin")

#  konversi reamur ke satuan lain
# reamur = float(input("masukkan suhu dalam reamur"))
# celcius = 5/4 * reamur
# print("suhu dalam celcius adalah ", celcius, "celcius")
# fahrenheit = ((9/4) * reamur) + 32
# print("suhu dalam fahrenheit adalah ", fahrenheit, "fahrenheit")
# kelvin = ((5/4) * reamur )+ 273
# print("suhu dalam kelvin adalah ", kelvin, "kelvin")

#  konversi fahrenheit ke satuan lain
# fahrenheit = float(input("masukkan suhu dalam fahrenheit"))
# celcius = (5/9) * (fahrenheit -32)
# print("suhu dalam celcius adalah ", celcius, "celcius")
# reamur = (4/9)*(fahrenheit - 32)
# print("suhu dalam reamur adalah ", reamur, "reamur")
# kelvin = celcius + 273
# print("suhu dalam kelvin adalah ", kelvin, "kelvin")

#  konversi kelvin ke satuan lain
# kelvin = float(input("masukkan suhu dalam kelvin : "))
# celcius = kelvin - 273
# print("suhu dalam celcius adalah ", celcius, "celcius")
# reamur = (4/5) * (kelvin - 273)
# print("suhu dalam reamur adalah ", reamur, "reamur")
# fahrenheit = ((9/5) * celcius) + 32
# print("suhu dalam fahrenheit adalah ", fahrenheit, "fahrenheit")


# operasi logika atau boolean
# not, or, and, xor

# print('===NOT===') 
# a = True
# b = not a 
# print(b)

# print('===OR===')
# c = True
# d = False
# e = c or d
# print(c, 'OR', d, '=', e)
# c = False
# d = True
# e = c or d
# print(c, 'OR', d, '=', e)
# c = True
# d = True
# e = c or d
# print(c, 'OR', d, '=', e)
# c = False
# d = False
# e = c or d
# print(c, 'OR', d, '=', e)

# print('===AND===')
# f = True
# g = False
# h = f and g
# print(f, 'and', g, '=', h)
# f = False
# g = True
# h = f and g
# print(f, 'and', g, '=', h)
# f = True
# g = True
# h = f and g
# print(f, 'and', g, '=', h)
# f = False
# g = False
# h = f and g
# print(f, 'and', g, '=', h)

# print('===XOR===')
# i = True
# j = False
# k = i ^ j
# print(i, 'xor', j, '=', k)
# i = False
# j = True
# k = i ^ j
# print(i, 'xor', j, '=', k)
# i = True
# j = True
# k = i ^ j
# print(i, 'xor', j, '=', k)
# i = False
# j = False
# k = i ^ j
# print(i, 'xor', j, '=', k)