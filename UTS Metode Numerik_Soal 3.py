import numpy as np
import matplotlib.pyplot as plt

# fungsi resistansi R(T)
def R(T): # menghitung resistansi berdasarkan persamaan yang diberikan
    return 5000 * np.exp(3500 * (1 / T - 1 / 298))

# turunan eksak dR/dT
def dR_dT_exact(T): # menghitung turunan eksak dari R(T)
    return -5000 * 3500 * np.exp(3500 * (1 / T - 1 / 298)) / T**2

# a) metode selisih maju, mundur, dan tengah. untuk menghitung turunan numerik
def forward_difference(f, T, h=1e-5):
    return (f(T + h) - f(T)) / h

def backward_difference(f, T, h=1e-5):
    return (f(T) - f(T - h)) / h

def central_difference(f, T, h=1e-5):
    return (f(T + h) - f(T - h)) / (2 * h)

# b) fungsi menghitung nilai eksak dR/dT sudah ada di eksak_dR_dT

# c) hitung dR/dT untuk rentang suhu 250K sampai 350K. menghitung turunan numerik dan eksak buat rentang suhu 250K sampai 350K
temperatur2 = np.arange(250, 351, 10)  # rentang suhu
dR_dT_nilai_eksak = dR_dT_exact(temperatur2)
dR_dT_maju = np.array([forward_difference(R, T) for T in temperatur2])
dR_dT_mundur = np.array([backward_difference(R, T) for T in temperatur2])
dR_dT_tengah = np.array([central_difference(R, T) for T in temperatur2])

# d) plot error relatif untuk ketiga metode numerik dibandingkan dgn nilai eksak. menghitung error relatif dari tiap metode dan memplotnya buat perbandingan
error_maju = np.abs((dR_dT_maju - dR_dT_nilai_eksak) / dR_dT_nilai_eksak) * 100
error_mundur = np.abs((dR_dT_mundur - dR_dT_nilai_eksak) / dR_dT_nilai_eksak) * 100
error_tengah = np.abs((dR_dT_tengah - dR_dT_nilai_eksak) / dR_dT_nilai_eksak) * 100

plt.figure(figsize=(10, 6))
plt.plot(temperatur2, error_maju, label='Selisih Maju', marker='o')
plt.plot(temperatur2, error_mundur, label='Selisih Mundur', marker='o')
plt.plot(temperatur2, error_tengah, label='Selisih Tengah', marker='o')
plt.xlabel("Temperatur (K)")
plt.ylabel("Error Relatif (%)")
plt.title("Error Relatif dari Metode Numerik")
plt.legend()
plt.grid()
plt.show()

# e) metode ekstrapolasi richardson supaya akurasi meningkat
def richardson_extrapolation(f, T, h=1e-5):
    D1 = (f(T + h) - f(T)) / h
    D2 = (f(T + h/2) - f(T)) / (h/2)
    return (4 * D2 - D1) / 3  # ekstrapolasi richardson

# hitung dR/dT dengan ekstrapolasi richardson
dR_dT_richardson = np.array([richardson_extrapolation(R, T) for T in temperatur2])

# error relatif untuk ekstrapolasi richardson
error_richardson = np.abs((dR_dT_richardson - dR_dT_nilai_eksak) / dR_dT_nilai_eksak) * 100

# plot hasil ekstrapolasi richardson dan bandingkan dengan metode numerik yang lain
plt.figure(figsize=(10, 6))
plt.plot(temperatur2, error_maju, label='Selisih Maju', marker='o')
plt.plot(temperatur2, error_mundur, label='Selisih Mundur', marker='o')
plt.plot(temperatur2, error_tengah, label='Selisih Tengah', marker='o')
plt.plot(temperatur2, error_richardson, label='Ekstrapolasi Richardson', marker='o')
plt.xlabel("Temperatur (K)")
plt.ylabel("Error Relatif (%)")
plt.title("Error Relatif dengan Ekstrapolasi Richardson")
plt.legend()
plt.grid()
plt.show()

# kesimpulan:
# metode selisih maju, mundur, tengah memberi pendekatan yang mendekati turunan eksak, dengan metode selisih tengah biasanya lebih akurat kalo dibanding dengan selisih maju dan mundur.
# ekstrapolasi richardson meningkatkan akurasi turunan numerik, menghasilkan error yang lebih kecil dibanding metode selisih biasa.
# grafik error relatif menunjukkan kalo ekstrapolasi richardson adalah metode yang paling akurat untuk menghitung turunan numerik kalo dibanding metode selisih biasa. ini menandakan kalo ekstrapolasi richardson berguna untuk meningkatkan ketelitian dalam perhitungan numerik.