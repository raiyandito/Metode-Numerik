import numpy as np
import matplotlib.pyplot as plt

# diketahui
L = 0.5  # H
C = 10e-6  # F
f_target = 1000  # Hz
toleransi = 0.1  # Ohm

# def fungsi f(R) dan turunannya f'(R)
def f_R(R): # fungsi untuk menghitung frekuensi resonansi tergantung nilai R
    expr = (1 / (L * C)) - (R**2 / (4 * L**2))
    if expr >= 0:
        return (1 / (2 * np.pi)) * np.sqrt(expr)
    else:
        return np.nan  # kalo hasil negatif, return NaN

def f_prime_R(R): # turunan dari fungsi frekuensi resonansi terhadap R
    expr = (1 / (L * C)) - (R**2 / (4 * L**2))
    if expr > 0:
        return -R / (4 * np.pi * L**2 * np.sqrt(expr))
    else:
        return np.nan  # kalo hasil negatif, return NaN

# fungsi untuk menemukan akar dengan metode biseksi
def bisection_method(f, target, a, b, tol): # melakukan iterasi untuk menemukan nilai R yang mendekati f_target dengan toleransi tol
    iterasii = []
    while (b - a) / 2 > tol:
        pertengahan = (a + b) / 2
        f_mid = f(pertengahan)
        error = abs(f_mid - target)
        iterasii.append((pertengahan, error))

        if np.isnan(f_mid):
            print("Nilai NaN ditemukan pada biseksi, cek interval.")
            return None, iterasii

        if f_mid == target:
            return pertengahan, iterasii
        elif f_mid < target:
            a = pertengahan
        else:
            b = pertengahan
    return (a + b) / 2, iterasii

# fungsi untuk menemukan akar dengan metode newton-raphson
def newton_raphson_method(f, f_prime, target, x0, tol): # melakukan iterasi untuk mengira2 nilai R dengan metode newton-raphson dengan toleransi tol
    x = x0
    iterasi = []
    while True:
        fx = f(x)
        error = abs(fx - target)
        iterasi.append((x, error))

        if np.isnan(fx):
            print("Nilai NaN ditemukan pada newton-raphson, metode gagal.")
            return None, iterasi

        if error < tol:
            break
        fpx = f_prime(x)
        if fpx == 0:
            print("Turunan nol, metode gagal.")
            break
        x = x - (fx - target) / fpx
    return x, iterasi

# mencari nilai R dengan metode biseksi
R_biseksi, biseksi_iterasi = bisection_method(f_R, f_target, 0, 100, toleransi)

# mencari nilai R dengan metode newton-raphson
R_newton, newton_iterasi = newton_raphson_method(f_R, f_prime_R, f_target, 50, toleransi)

# print hasil
print("Hasil dengan metode Biseksi:", R_biseksi)
print("Hasil dengan metode Newton-Raphson:", R_newton)

# visualisasi konvergensi
# untuk memperlihatkan kecepatan konvergensi dari dua metode. hasil error tiap iterasi diambil dan diplot untuk memperjelas bedanya.
biseksi_error = [err for _, err in biseksi_iterasi]
newton_error = [err for _, err in newton_iterasi]

plt.plot(biseksi_error, label='Metode Biseksi')
plt.plot(newton_error, label='Metode Newton-Raphson')
plt.yscale('log')
plt.xlabel('Iterasi')
plt.ylabel('Error (log scale)')
plt.title('Perbandingan Konvergensi Metode Biseksi dan Newton-Raphson')
plt.legend()
plt.grid(True)
plt.show()

# kesimpulan:
# metode biseksi perlu lebih banyak iterasi tapi stabil dalam konvergensinya, karena selalu mempersempit interval hingga menemukan solusi dengan toleransi yang diinginkan.
# metode newton-raphson lebih cepat buat mendapat solusi, tapi kecepatan konvergensi tergantung pada tebakan awal. kalo tebakan awal jauh dari solusi, metode ini mungkin perlu iterasi lebih banyak atau bisa saja gagal konvergen.
# grafik hasil menunjukkan perbedaan kecepatan konvergensi antara kedua metode, dengan newton-raphson biasanya lebih efisien tapi perlu tebakan awal yang tepat.