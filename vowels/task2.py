# task - 2 (converting sample sounds of vowels and consonants into Freq domain to mark in inkscape)

# importing necessary libraries 
import matplotlib.pyplot as plt # library to plot data
import numpy as np # numerical operations library
import wave # library to import the .wav file and get other info from it
from scipy.fftpack import fftfreq,fft # frequency analysis library

#loading all different sound files that will be used to compare with original
#sample to mark vowels and consonant points in the freq spectrum.
soundFiles = ["a.wav", "o.wav", "i_e.wav","ck.wav","f.wav","g.wav","z.wav"]
for i in range(len(soundFiles)):
    spf = wave.open(soundFiles[i], "r") # loading the recording file
    # the sentence chosen: "the quick brown fox jumps over a lazy dog"
    
    #task-1 Plotting Time Domain and Bode plots of the Recording
    
    # Extract Raw Audio from Wav File
    signal = spf.readframes(-1)  # getting each hexadecimal value
    signal = np.fromstring(signal, dtype=np.int16)  # converting from a string of hex values to array 
    frames = spf.getnframes() # total number of frames in recording
    rate = spf.getframerate() # sampling rate
    
    normalized_signal = signal/np.max(np.abs(signal)) # normalizing signal   
    signalfft = fft(normalized_signal)
    fftabs = np.abs(signalfft)
    fftdb = 20*np.log10(fftabs)  # generating amplitude in decibels
    freqs = fftfreq(frames,1/rate) # generating frequency scale for the signal
    
    # Frequency plot of signal
    plt.figure(i)
    plt.title("Bode Plot of Signal " + soundFiles[i])
    plt.xlim( [10, rate/2] )
    plt.xscale( 'log' )
    plt.grid( True )
    plt.ylabel( 'Amplitude (dB)')
    plt.xlabel( 'Frequency (Hz)' )
    plt.plot(freqs[:int(freqs.size/2)],fftdb[:int(freqs.size/2)])
    plt.savefig(soundFiles[i]+'.svg', format='svg')