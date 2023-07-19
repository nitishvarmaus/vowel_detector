# importing necessary libraries 
import matplotlib.pyplot as plt # library to plot data
import numpy as np # numerical operations library
import wave # library to import the .wav file and get other info from it
from scipy.fftpack import fftfreq,fft,ifft # frequency analysis library
from scipy.io.wavfile import write

spf = wave.open("original.wav", "r") # loading the recording file
# the sentence chosen: "the quick brown fox jumps over a lazy dog"

#task-1 Plotting Time Domain and Bode plots of the Recording

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)  # getting each hexadecimal value
signal = np.fromstring(signal, dtype=np.int16)  # converting from a string of hex values to array 

# get the appropriate time scale from the file
frames = spf.getnframes() # total number of frames in recording
rate = spf.getframerate() # sampling rate
duration = frames / float(rate) # time length of recording
time = np.linspace(0,duration,len(signal)) # finnaly generating the time values for each amplitude

normalized_signal = signal/np.max(np.abs(signal)) # normalizing signal

# time plot of normalized signal
plt.figure(1) 
plt.title("Normalized Signal Wave")
plt.grid( True )
plt.ylabel( 'Amplitude')
plt.xlabel( 'time (seconds)' )
plt.plot(time,normalized_signal)
plt.show()

signalfft = fft(normalized_signal)
fftabs = np.abs(signalfft)
fftdb = 20*np.log10(fftabs)  # generating amplitude in decibels
freqs = fftfreq(frames,1/rate) # generating frequency scale for the signal

# Frequency plot of signal
plt.figure(2)
plt.title("Bode Plot of Signal")
plt.xlim( [10, rate/2] )
plt.xscale( 'log' )
plt.grid( True )
plt.ylabel( 'Amplitude (dB)')
plt.xlabel( 'Frequency (Hz)' )
plt.plot(freqs[:int(freqs.size/2)],fftdb[:int(freqs.size/2)])
plt.show()

#task-3 Using Fourier Transform to Improve Signal
amp1=int(len(signalfft)/rate*1000) #boosting or amplifying index place for 1000Hz 
amp2=int(len(signalfft)/rate*20000) #boosting or amplifying index place for 20000Hz (maxm limit of human voice)
f1=int(len(signalfft)/rate*10) #index place for 10Hz
f2=int(len(signalfft)/rate*100) #index place for 100Hz
f3=int(len(signalfft)/rate*20001) #index place for 20001Hz
f4=int(len(signalfft)/rate*np.max(freqs)) #index place for highest frequency recorded
signalfft[f3:f4]=signalfft[f3:f4]/6000 # reduction in the region beyond 20kHz
# Mirroring from right to left to reduce noise
signalfft[int(len(signalfft)-f4):int(len(signalfft)- f3)]=signalfft[int(len(signalfft)-f4):int(len(signalfft)-f3)]/6000 
signalfft[f1:f2]=signalfft[f1:f2]/6000
# Mirroring from right to left to reduce noise
signalfft[int(len(signalfft)-f2):int(len(signalfft)-f1)]=signalfft[int(len(signalfft)-f2):int(len(signalfft)-f1)]/6000 
signalfft[amp1:amp2]=signalfft[amp1:amp2]*10 
# amplification of region with highest hormonics
signalfft[int(len(signalfft)-amp2):int(len(signalfft)- amp1)]=signalfft[int(len(signalfft)-amp2):int(len(signalfft)-amp1)]*10
fftabs = np.abs(signalfft)
fftdb = 20*np.log10(fftabs)  # generating amplitude in decibels

plt.figure(3)
plt.title("Bode Plot of Improved Signal")
plt.xlim( [10, rate/2] )
plt.xscale( 'log' )
plt.grid( True )
plt.ylabel( 'Amplitude (dB)')
plt.xlabel( 'Frequency (Hz)' )
plt.plot(freqs[:int(freqs.size/2)],fftdb[:int(freqs.size/2)])
plt.show()

signal_new = ifft(signalfft)
signal_new = np.int16(signal_new/np.max(np.abs(signal_new)) * 32767)
write('improved.wav', 44100, signal_new)

