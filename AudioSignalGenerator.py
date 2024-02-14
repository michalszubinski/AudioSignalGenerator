import math
import struct
import wave

import numpy as np
import scipy

from signals import *

class AudioSignalGenerator:

    def __init__(self, sample_rate, bit_depth, nchannels=1):
        self.sample_rate = sample_rate
        self.bit_depth = bit_depth
        self.duration_seconds = 0
        self.sample_values = []
        self.timestamps = []
        self.signals = list()
        self.nchannels = nchannels

    def add_signal(self, signal):
        self.signals.append(signal)

    def generate_samples(self):
        for signal in self.signals:

            signal.generate()
            current_sample_time = signal.start_on_sample

            while len(self.sample_values) < signal.start_on_sample:
                self.sample_values.append(0)
                self.timestamps.append(len(self.sample_values) - 1)

            while current_sample_time <= signal.end_on_sample:
                if len(self.sample_values) == current_sample_time:
                    self.sample_values.append(signal.sample_values[current_sample_time - signal.start_on_sample])
                    self.timestamps.append(current_sample_time)
                else:
                    self.sample_values[current_sample_time] += signal.sample_values[current_sample_time - signal.start_on_sample]

                current_sample_time += 1

        for sample in self.sample_values: # PREVENT CLIPPING
            if sample > 1:
                sample = 1
            elif sample < -1:
                sample = -1

    def save_audio(self,filename):
        """
        #TODO:
        # * ADD ABILITY TO SAVE MULTICHANNEL WAVE
        # * ALLOW TO CHANGE BIT DEPTH
        # maybe helpful: https://stackoverflow.com/questions/33879523/python-how-can-i-generate-a-wav-file-with-beeps
        self.sample_values = np.array(self.sample_values).astype(np.float32)
        scipy.io.wavfile.write(filename, int(self.sample_rate), np.array(self.sample_values))
        """
        #maybe use wave module? https://stackoverflow.com/questions/16767248/how-do-i-write-a-24-bit-wav-file-in-python

        new_sample_list = list()

        for sample in self.sample_values:
            new_sample_list.append(sample * (math.pow(2,(self.bit_depth - 1) - 1)))

        if self.bit_depth == 16:
            new_sample_list = np.array(new_sample_list).astype(np.int16)
        elif self.bit_depth == 24: #TODO: SAVES AS 32 FOR NOW
            print('24 bit option unsupported currently. Saving 24 bit signal to 32 bit PCM...')
            new_sample_list = np.array(new_sample_list).astype(np.int32)
        elif self.bit_depth == 32:
            new_sample_list = np.array(new_sample_list).astype(np.int32)
        elif self.bit_depth == 8:
            sample_list_8_bit = list()
            for sample in new_sample_list:
                sample_list_8_bit.append(sample + 128)
            new_sample_list = np.array(sample_list_8_bit).astype(np.uint8)
        else:
            print('Unsupported bit depth! Currently supported are: 8, 16, 32 bits')
            return


        scipy.io.wavfile.write(filename, int(self.sample_rate), np.array(new_sample_list))


