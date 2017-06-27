# -*- coding: utf-8 -*-
import pyaudio
import time
import numpy

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2**11
RECORD_SECONDS = 0.1
from matplotlib import pyplot as plt


audio = pyaudio.PyAudio()
frames = []
def callback(in_data, frame_count, time_info, status):
    d = numpy.fromstring(in_data, dtype=numpy.int16)
    frames.extend(list(d))
    print(len(frames))
    return(None, pyaudio.paContinue)

stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                input_device_index=0,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

print ("recording...")
stream.start_stream()
time.sleep(RECORD_SECONDS)
print ("finished recording")


stream.stop_stream()
stream.close()
audio.terminate()

plt.plot(frames)
plt.show()
