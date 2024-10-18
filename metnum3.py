import math 

# definisi f(x)
def f(x):
    return x - math.exp(-x)

# definisi turunan f'(x)
def df(x):
    return 1 + math.exp(-x)

# metode newton-raphson
def newton_raphson(x0, Toleransi=1e-7, Max_iterasi=100):
    x = x0
    for i in range(Max_iterasi):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            raise ValueError("Turunan f'(x) adalah nol. Metode gagal.")
        
        x_new = x - fx / dfx
        
        # mengecek konvergensi
        if abs(x_new - x) < Toleransi:
            print(f"Konvergen dalam {i+1} iterasi.")
            return x_new
        
        x = x_new
    
    raise ValueError(f"Metode tidak konvergen dalam {Max_iterasi} iterasi")

# nilai awal x0
x0 = 0

# fungsi dijalankan
hasil = newton_raphson(x0)
print(f"Akar yang ditemukan: {hasil}")
