# ===============================
# TUGAS 3 - PYTHON BASICS
# ===============================

# 1. Deklarasi Variabel dan Tipe Data
nama = "Siti"        # string
umur = 20               # integer
tinggi = 160.5          # float
is_student = True       # boolean
hobi = ["coding", "reading", "music", "gaming", "travel"]  # list

print("=== Variabel & Tipe Data ===")
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa:", is_student)
print("Hobi:", hobi)

# ===============================

# 2. Manipulasi String
print("\n=== Manipulasi String ===")

teks = "hello world"
print("Teks asli:", teks)
print("Huruf besar:", teks.upper())
print("Huruf kecil:", teks.lower())
print("Panjang teks:", len(teks))

# Gabung string
kalimat = "Halo, nama saya " + nama
print(kalimat)

# ===============================

# 3. Operasi Matematika
print("\n=== Operasi Matematika ===")

a = 10
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)

# ===============================

# 4. List dan Akses Elemen
print("\n=== List ===")

buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]

print("List awal:", buah)
print("Elemen pertama:", buah[0])
print("Elemen ketiga:", buah[2])

# Tambah item
buah.append("melon")
print("Setelah tambah:", buah)

# Hapus item
buah.remove("jeruk")
print("Setelah hapus:", buah)

# ===============================

# 5. Input User
print("\n=== Input User ===")

user_nama = input("Masukkan nama kamu: ")
user_umur = input("Masukkan umur kamu: ")

print(f"Halo, nama saya {user_nama} dan umur saya {user_umur} tahun.")
