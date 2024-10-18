def regulafalsi(f, a, b, tolerance=1e-6, max_iteration=10):
    if f(a) * f(b) > 0:
        print("Fungsi tidak memiliki akar di interval tersebut.")
        return None
    
    iteration_count = 0
    c = a  # inisialisasi variabel c

    while abs(b - a) > tolerance and iteration_count < max_iteration:
        # hitung nilai c (titik potong dengan sumbu-x)
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        
        # tampilkan status tiap iterasi
        print(f"Iterasi ke-{iteration_count}: c = {c}, f(c) = {f(c)}")

        # jika nilai f(c) mendekati nol atau tepat nol, maka telah ada akar
        if abs(f(c)) < tolerance:
            return c
        
        # memperbarui interval [a, b]
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        iteration_count += 1
    
    # kembalikan hasil setelah iterasi selesai
    if iteration_count == max_iteration:
        print("Peringatan: Iterasi maksimum tercapai.")
    
    return c


# definisi fungsi
def f(x):
    return x**2 - 4

# call fungsi regulafalsi
root = regulafalsi(f, 1, 3)

# cetak hasil
print(f"Akar yang ditemukan: {root}")
