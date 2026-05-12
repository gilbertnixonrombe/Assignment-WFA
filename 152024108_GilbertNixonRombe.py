from concurrent.futures import ThreadPoolExecutor
import time

daftar_nilai = [78, 85, 90, 67, 88, 92, 74, 80, 95, 69,
                73, 84, 91, 76, 89, 97, 70, 82, 86, 93]

def hitung_grade(nilai):
    time.sleep(0.2)

    if nilai >= 90:
        grade = "A"
    elif nilai >= 80:
        grade = "B"
    elif nilai >= 70:
        grade = "C"
    else:
        grade = "D"

    status = "Lulus" if nilai >= 70 else "Tidak Lulus"

    return nilai, grade, status

print("Program Data Parallelism - Pengolahan Nilai")
print("==========================================")
print("Data nilai mahasiswa:")
print(daftar_nilai)
print()

waktu_mulai = time.time()

with ThreadPoolExecutor(max_workers=4) as executor:
    hasil = list(executor.map(hitung_grade, daftar_nilai))

waktu_selesai = time.time()

print("Hasil Pengolahan:")
print("Nilai | Grade | Status")
print("----------------------")

for nilai, grade, status in hasil:
    print(f"{nilai:5} | {grade:5} | {status}")

print("----------------------")
print("Total waktu proses:", round(waktu_selesai - waktu_mulai, 2), "detik")

print()
print("Penjelasan:")
print("Program ini menggunakan data parallelism.")
print("Data nilai yang berbeda diproses dengan fungsi yang sama, yaitu hitung_grade().")
print("Setiap nilai dicek grade dan status kelulusannya.")
print("Dengan ThreadPoolExecutor, beberapa data nilai bisa diproses secara bersamaan.")