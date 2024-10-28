import numpy as np

# matriks koefisien dan vektor hasil untuk sistem persamaan
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]], dtype=float)
b = np.array([5, 3, 4], dtype=float)

# a) fungsi eliminasi gauss untuk menyelesaikan sistem persamaan
def gauss_elimination(A, b): # fungsi ini mengeliminasi elemen2 di bawah pivot untuk membentuk matriks segitiga atas terus melakukan substitusi mundur untuk mendapat hasil/solusi.
    n = len(b)
    # gabung A dan b menjadi matriks yang diperbesar
    Ab = np.hstack((A, b.reshape(-1, 1)))

    # eliminasi maju
    for i in range(n):
        # pivoting
        baris_maks = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, baris_maks]] = Ab[[baris_maks, i]]

        # normalisasi baris pivot
        Ab[i] = Ab[i] / Ab[i, i]

        # eliminasi
        for j in range(i + 1, n):
            Ab[j] = Ab[j] - Ab[j, i] * Ab[i]

    # substitusi mundur
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.sum(Ab[i, i+1:n] * x[i+1:n])
    return x

# b) fungsi determinan dengan ekspansi kofaktor
def determinant(matriks): # fungsi ini menghitung determinan matriks memakai metode ekspansi kofaktor.
    if len(matriks) == 1:
        return matriks[0, 0]
    if len(matriks) == 2:
        return matriks[0, 0] * matriks[1, 1] - matriks[0, 1] * matriks[1, 0]

    det = 0
    for c in range(len(matriks)):
        minor = np.delete(np.delete(matriks, 0, axis=0), c, axis=1)
        kofaktor = ((-1) ** c) * matriks[0, c] * determinant(minor)
        det += kofaktor
    return det

# c) menggunakan fungsi tadi untuk menyelesaikan sistem persamaan
x_gauss = gauss_elimination(A.copy(), b.copy()) # fungsi ini memperluas eliminasi sampai membentuk matriks identitas, jadi solusi langsung bisa diambil dari kolom terakhir
det_A = determinant(A)

print("Solusi dengan Eliminasi Gauss:", x_gauss)
print("Determinan matriks A:", det_A)

# d) implementasi metode gauss-jordan
def gauss_jordan(A, b):
    n = len(b)
    # gabung A dan b menjadi matriks yang diperbesar
    Ab = np.hstack((A, b.reshape(-1, 1)))

    # eliminasi maju
    for i in range(n):
        # pivoting
        baris_makss = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, baris_makss]] = Ab[[baris_makss, i]]

        # normalisasi baris pivot
        Ab[i] = Ab[i] / Ab[i, i]

        # eliminasi atas dan bawah
        for j in range(n):
            if j != i:
                Ab[j] = Ab[j] - Ab[j, i] * Ab[i]

    # hasil/solusi ada di kolom terakhir
    return Ab[:, -1]

x_gauss_jordan = gauss_jordan(A.copy(), b.copy())
print("Solusi dengan Gauss-Jordan:", x_gauss_jordan)

# e) fungsi untuk menghitung inverse matriks dengan metode adjoint
def cofactor_matrix(matriks):
    n = len(matriks)
    kofaktor2 = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(matriks, i, axis=0), j, axis=1)
            kofaktor2[i, j] = ((-1) ** (i + j)) * determinant(minor)
    return kofaktor2

def adjoint(matriks):
    return cofactor_matrix(matriks).T

def inverse(matriks): # fungsi ini memakai metode kofaktor dan adjoint untuk menghitung inverse matriks.
    det = determinant(matriks)
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers.")
    adj = adjoint(matriks)
    return adj / det

inverse_A = inverse(A)
print("Inverse matriks A dengan metode adjoint:")
print(inverse_A)

# kesimpulan:
# eliminasi gauss dan gauss-jordan memberi solusi akurat untuk sistem persamaan linier. tapi, gauss-jordan lebih lengkap karena mengubah matriks menjadi bentuk identitas, yang membuat gampang pengecekan konsistensi sistem.
# perhitungan determinan memakai ekspansi kofaktor member hasil yang sama dengan metode langsung, tapi lebih efisien untuk matriks yang lebih kecil.
# inverse matriks yang dihitung dengan metode adjoin menunjukkan hasil yang pas dengan inverse matriks standar, tapi metode ini kurang efisien untuk matriks besar kalo dibandingkan dengan gauss-jordan.
# perbandingan menunjukkan bahwa gauss dan gauss-jordan efektif untuk menyelesaikan sistem linier yang kecil, tapi metode yang lebih efisien diperlukan untuk matriks yang lebih besar.