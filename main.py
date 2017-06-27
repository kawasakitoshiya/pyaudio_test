# -*- coding: utf-8 -*-
import pyaudio
import time
import numpy
from collections import deque

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RETENSION_SECONDS = 100
CHUNK = 2**11
from matplotlib import pyplot as plt


audio = pyaudio.PyAudio()
deque_len = RATE * RETENSION_SECONDS
frames = deque([0]*deque_len, maxlen=deque_len)
def callback(in_data, frame_count, time_info, status):
    d = numpy.fromstring(in_data, dtype=numpy.int16)
    frames.extend(list(d))
    return(None, pyaudio.paContinue)

stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                input_device_index=0,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

print ("recording...")
stream.start_stream()

while True:
#    plt.plot(frames)
    plt.specgram(frames,Fs = 2)
    plt.pause(.1)
    plt.gcf().clear()

stream.stop_stream()
stream.close()
audio.terminate()
