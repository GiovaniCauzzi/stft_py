import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import stft

# Load the WAV file
sample_rate, signal = wavfile.read('04-lead solo-200606_1700.wav')  # Replace with your file path

# If stereo, take only one channel
if signal.ndim == 2:
    signal = signal[:, 0]

# Normalize signal (optional but often helpful for visualization)
signal = signal / np.max(np.abs(signal))

# Compute STFT
f, t_stft, Zxx = stft(signal, fs=sample_rate, nperseg=2048)

# Plot the spectrogram
plt.figure(figsize=(12, 6))
plt.pcolormesh(t_stft, f, np.abs(Zxx), shading='gouraud')
plt.title('Spectrogram of Audio File')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.ylim(0, 3000)  # Limit frequency 
plt.colorbar(label='Magnitude')
plt.tight_layout()
plt.show()
