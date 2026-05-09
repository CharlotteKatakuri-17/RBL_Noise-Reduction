import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Membuat sinyal asli
fs = 1000

t = np.linspace(0, 1, fs)

signal = np.sin(2 * np.pi * 5 * t)

# Menambahkan noise
noise = np.random.normal(0, 0.5, fs)

noisy_signal = signal + noise

# Fungsi low pass filter

def lowpass(data, cutoff, fs):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist

    b, a = butter(4, normal_cutoff, btype='low')

    filtered = filtfilt(b, a, data)

    return filtered

filtered_signal = lowpass(noisy_signal, 10, fs)

# Plot hasil
plt.figure(figsize=(10,6))

plt.plot(t, noisy_signal, label='Sinyal Ber-noise', alpha=0.5)

plt.plot(t, filtered_signal, label='Setelah Filter', linewidth=2)

plt.plot(t, signal, label='Sinyal Asli', linestyle='dashed')

plt.xlabel('Waktu')
plt.ylabel('Amplitudo')
plt.title('Noise Reduction pada Sinyal Audio')

plt.legend()

plt.savefig('hasil/grafik_noise_reduction.png')

plt.show()
