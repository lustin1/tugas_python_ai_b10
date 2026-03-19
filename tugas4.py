# ===============================
# TUGAS 4 - PYTHON DATA STRUCTURES
# ===============================

# 1. LIST – akses & manipulasi
print("=== LIST ===")

data = ["apel", 10, "jeruk", 25, "mangga", 50]

print("List awal:", data)
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])
print("Slicing [1:5:2]:", data[1:5:2]) #data[start:stop:step]

# manipulasi
print("\n-- Manipulasi List --")
print("Sebelum:", data)

data.append("pisang")
data.insert(1, "anggur")
data.extend([100, 200])
data.pop()
data.remove("jeruk")

print("Proses append, insert, extend, pop, remove...")
print("Sesudah:", data)

# ===============================

# 2. TUPLE – immutability & unpacking
print("\n=== TUPLE ===")

tup = ("A", "B", "C", "D", "E")

print("Tuple:", tup)
print("Panjang:", len(tup))
print("Akses indeks ke-2:", tup[2])

# unpacking
a, b, *rest = tup
print("Unpacking:")
print("a =", a)
print("b =", b)
print("rest =", rest)

# ===============================

# 3. SET – keunikan & operasi
print("\n=== SET ===")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set1:", set1)
print("Set2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# duplikat hilang
set_duplikat = {1, 1, 2, 2, 3, 3}
print("Set tanpa duplikat:", set_duplikat) #Set di Python TIDAK menyimpan nilai duplikat

# ===============================

# 4. DICTIONARY – key/value
print("\n=== DICTIONARY ===")

mahasiswa = {
    "nama": "Siti",
    "nim": "123456",
    "angkatan": 2023,
    "kota": "Batam"
}

print("Data awal:", mahasiswa)

# tambah
mahasiswa["prodi"] = "Informatika"

# ubah
mahasiswa["kota"] = "Jakarta"

# hapus
del mahasiswa["angkatan"]

print("Data setelah update:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("\nIterasi:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# ===============================

# 5. NESTED STRUCTURES
print("\n=== NESTED STRUCTURES ===")

buku = [
    {"judul": "Python Basics", "penulis": "A", "tahun": 2020},
    {"judul": "AI Intro", "penulis": "B", "tahun": 2022},
    {"judul": "Data Science", "penulis": "C", "tahun": 2021},
    {"judul": "Machine Learning", "penulis": "D", "tahun": 2023}
]

print("Daftar Judul Buku:")
for b in buku:
    print("-", b["judul"])

# filter
tahun_filter = 2021
hasil = [b for b in buku if b["tahun"] >= tahun_filter]

print("\nBuku >= 2021:")
for b in hasil:
    print("-", b["judul"], "-", b["tahun"])

# ===============================

# 6. COMPREHENSION & UTILITAS
print("\n=== COMPREHENSION ===")

angka = list(range(1, 21))

genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("Angka genap:", genap)
print("Kuadrat:", kuadrat)

# dict comprehension
mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("Mapping angka:", mapping)

# set comprehension
kalimat = "Belajar Python Itu Menyenangkan"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf_unik)

# ===============================

# 7. KEANGGOTAAN & PENCARIAN
print("\n=== KEANGGOTAAN ===")

list_cari = ["apel", "jeruk", "mangga"]

item = "jeruk"

if item in list_cari:
    print(f"{item} ditemukan di index:", list_cari.index(item))
else:
    print(f"{item} tidak ditemukan")

set_cari = {1, 2, 3, 4}

cek = 3
print(f"{cek} ada di set?" , cek in set_cari)
