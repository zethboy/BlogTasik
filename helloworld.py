# print("hello world")

# #integer
# angka = 10

# #float
# desimal = 3.14

# #string 
# teks = "hallo nama aku yogi" 

# #boolean 
# is_phyton_fun = True

# nama = input("siapa nama kamu :")
# print("nama aku adalah "+ nama +"!")

# if nama == "yogi":
#   print("kamu gaboleh lanjut")
# elif nama == "aya":
#   print ("aya pacar ogii")
# else:
#   print ("well")

# a = 5
# b = 2

# # print(a+b)
# # print(a-b)
# # print(a/b)
# # print(a*b)
# # print(a**b)
# # print(a%b)

# looping fir untuk iterasi
 
# for i in range (5):
#   print("perulangan ke", i)

# while loop
# i = 0
# while i<5:
#   print("perulanagan ke", i)
#   i += 1

# break dan continue

# for i in range (5):
#   if i == 3:
#     break
#   print (i)

# for i in range (5):
#   if i == 3:
#     continue
#   print (i)

# nested control flow

# for i in range (3):
#   for j in range (3):
#     print(f"i={i}, j={j}")

# list

# membuat list
# buah = ["apel", "anggur", "pepaya"]

# # akses elemen
# print(buah[0])

# #menambahkan elemen

# buah.append("salak")
# print(buah)

# # menghapus elemen

# buah.remove("pepaya")
# print(buah)

# tuple (hampir sama tapi ga bisa diubah)

# angka = (1,2,3)
# print (angka[2])

# dictionary

# # membuat dictionary
# mahasiswa = {"Nama": "Yogi", "Kelas": "C", "NPM" : 123456789}

# # mengakses elemen dictionary
# print(mahasiswa["NPM"])

# # menambahkan
# mahasiswa["angkatan"] = 2024
# print(mahasiswa["angkatan"])

# # menghapus 
# del mahasiswa["Kelas"]
# print (mahasiswa)

# set
# membuat set
# angka = {1, 2, 3, 4}
# print(angka)

# # menambahkan
# angka.add(8)
# print (angka)

# fungsi
# def sapa(nama):
#   print(f"hallo {nama}, selamat belajar phyton")

# sapa("yogi")

# # fungsi dengan return
# def hitung_persegi(sisi):
#   return sisi * sisi

# hasil = hitung_persegi(8)
# print(f"hasilnya adalah : {hasil}")

# # parameter default

# def woi(nama = "Yogi"):
#   print(f"hallo {nama}, semangat yaa!")

# woi()
# woi("ayaa")

# # dengan banyak parameter

# def hitungluaspersegipanjang(panjang, lebar):
#   return panjang * lebar

# hasil = hitungluaspersegipanjang(3, 12)
# print(f"Hasil luasnya adalah {hasil}")

#fungsi rekursif 

# def factorial(n):
#   if n == 1:
#     return 1
#   else:
#     return n * factorial ( n - 1 )
  
# print(factorial(5))

# def fibonnaci(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fibonnaci(n-1) + fibonnaci(n-2)
# print (fibonnaci(6))

# def fibonnaci_optimized(n, memo={}):
#   if n in memo:
#     return memo[n]
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     result = fibonnaci_optimized(n - 1, memo) + fibonnaci_optimized(n - 2, memo)
#     memo[n] = result  
#     return result

# print(fibonnaci_optimized(50))\

# ARRAY

# number = ['Yogi', 'Ayaa', 'Renata', 'Tiasya']
# number.append('ALLEA')
# number.insert(3,'TIASYA')

# print(number)

# number = [5, 2, 1, 4, 3]

# number.append(6)
# number.sort()

# print(len(number))

# dictionary

# myDict = {'nama' : 'Yogi', 'age' : 18}
# print(myDict)
# myDict['nama'] = 'Ayaa'
# print(myDict)
# myDict['age'] = 17
# print(myDict)

# # stack

# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack)

# stack.pop()

# print(stack)

# from collections import deque

# queue = deque()

# queue.append(1)
# queue.append(2)
# queue.append(3)

# print("queue setelah engueue", list(queue))

# queue.popleft()
# print("queue setelah deque", list(queue))

# buble sort

# def buble_sort(arr):
#   n = len(arr)
#   for i in range(n):
#     for j in range(0, n-i-1):
#       if arr[j] > arr[j+1]:
#         arr[j], arr[j+1] = arr[j+1], arr[j]

# my_list = [65, 79, 29, 4, 90, 13, 187]
# buble_sort(my_list)
# print("hasil buble sort :", my_list)

# def buble_sort(arr):
#   n = len(arr)
#   for i in range(n):
#     for j in range(0, n-i-1):
#       if arr[j] > arr [j + 1]:
#         arr[j], arr[j + 1] = arr [j + 1], arr [j]
# myList = [90, 12, 34, 51, 8, 190]
# buble_sort(myList)
# print("Buble short nya adalah :", myList)

# linear search
# def linear(arr, target):
#   for i in range(len(arr)):
#     if arr[i] == target:
#       return i
#   return -1
# arr = [10, 20, 30, 40, 50]
# target = 30
# result = linear(arr, target)

# if result != 1:
#   print("target ditemukan di indeks ke:", result)
# else:
#   print("target not detected")

# binary search

# def binary(arr, target):
#   left = 0
#   right = len(arr) - 1

#   while left <= right:
#     mid = (left + right) // 2
#     if arr[mid] == target:
#       return mid
#     elif arr[mid] < target:
#       left = mid + 1
#     else:
#       right = mid + 1
#   return-1

# arr = [10, 20, 30, 40, 50, 60, 70]
# target = 40
# result = binary(arr, target)

# if result != 1:
#   print("data ditemukan di indeks ke :", result)
# else:
#   print("data tidak ditemukan")

# a = 9
# b = 5
# c = a * b
# print(c)

# data  = input("masukkan data :")
# print("Data nya dalah", data, ",type =", type(data))

#  integer

# data  = int(input("masukkan data :"))
# print("Data nya dalah", data, ",type =", type(data))

# biar dapet boolean
# data  = bool(int(input("masukkan data :")))
# print("Data nya dalah", data, ",type =", type(data))



