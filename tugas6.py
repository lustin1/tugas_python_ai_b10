# ===============================
# TUGAS 6 - NUMPY, PANDAS, FILE I/O, OOP
# ===============================

import numpy as np
import pandas as pd
import os

# optional seed
np.random.seed(42)


# ---------- CLASS ----------
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df["nilai"].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        lulus = len(self.df[self.df["nilai"] >= threshold])
        return round((lulus / total) * 100, 2)

    def save_summary(self, path: str):
        total = len(self.df)
        lulus = len(self.df[self.df["nilai"] >= 70])
        tidak_lulus = total - lulus

        with open(path, "a") as f:
            f.write("\n=== OOP SUMMARY ===\n")
            f.write(f"Total Data: {total}\n")
            f.write(f"Rata-rata Nilai: {self.average():.2f}\n")
            f.write(f"Persentase Lulus: {self.pass_rate()}%\n")
            f.write(f"Lulus: {lulus}\n")
            f.write(f"Tidak Lulus: {tidak_lulus}\n")

    def __str__(self):
        return f"GradeBook(total={len(self.df)}, rata={self.average():.2f})"


# ---------- MAIN ----------
if __name__ == "__main__":

    # ===============================
    # NUMPY
    # ===============================
    print("=== NUMPY ===")

    nilai_np = np.random.randint(50, 100, size=10)

    print("Data nilai:", nilai_np)

    rata = np.mean(nilai_np)
    median = np.median(nilai_np)
    std = np.std(nilai_np)
    minimum = np.min(nilai_np)
    maximum = np.max(nilai_np)

    print("Rata-rata:", rata)
    print("Median:", median)
    print("Standar Deviasi:", std)
    print("Min:", minimum)
    print("Max:", maximum)

    # ===============================
    # PANDAS
    # ===============================
    print("\n=== PANDAS ===")

    data = {
        "nama": ["Budi", "Siti", "Andi", "Rina", "Dewi"],
        "nim": ["A01", "A02", "A03", "A04", "A05"],
        "nilai": nilai_np[:5]
    }

    df = pd.DataFrame(data)

    # tambah kolom status
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

    print(df.head())

    # ===============================
    # FILE I/O
    # ===============================
    file_path = "ringkasan_tugas6.txt"

    total = len(df)
    lulus = len(df[df["status"] == "LULUS"])
    tidak_lulus = total - lulus

    with open(file_path, "w") as f:
        f.write("=== STATISTIK NUMPY ===\n")
        f.write(f"Rata-rata: {rata:.2f}\n")
        f.write(f"Median: {median:.2f}\n")
        f.write(f"Standar Deviasi: {std:.2f}\n")
        f.write(f"Min: {minimum}\n")
        f.write(f"Max: {maximum}\n")

        f.write("\n=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah Data: {total}\n")
        f.write(f"Lulus: {lulus}\n")
        f.write(f"Tidak Lulus: {tidak_lulus}\n")

    # ===============================
    # OOP
    # ===============================
    print("\n=== OOP: GRADEBOOK ===")

    gb = GradeBook(df)

    print(gb)
    print("Average:", gb.average())
    print("Pass Rate:", gb.pass_rate(), "%")

    gb.save_summary(file_path)

    print("\nRingkasan disimpan di:", file_path)
