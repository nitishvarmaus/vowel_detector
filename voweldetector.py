from scipy.io import wavfile
import numpy as np


def voweldetector(wav):
    audio = wavfile.read(wav)
    audio = audio[1]
    fs = 44100
    xf = abs(np.fft.fft(audio))
    index_1 = int(420*len(xf)/fs)
    index_2 = int(430*len(xf)/fs)
    index_3 = int(460*len(xf)/fs)
    index_4 = int(470*len(xf)/fs)
    avg_a = sum(xf[index_1:index_2]) / len(xf[index_1:index_2])
    avg_o = sum(xf[index_3:index_4]) / len(xf[index_3:index_4])
    if avg_a > 15000000:
        vowel_detected = 'a'
    if avg_o > 15000000:
        vowel_detected = 'o'
    return vowel_detected


vowel1 = voweldetector('vowel1.wav')
print (vowel1)
vowel2 = voweldetector('vowel2.wav')
print (vowel2)