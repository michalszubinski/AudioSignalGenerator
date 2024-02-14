import numpy as np
import scipy
from matplotlib import pyplot as plt, pyplot

from signals.Signal import Signal
import random

from signals.Signal_UniformWhiteNoise import Signal_UniformWhiteNoise


class Signal_UniformPinkNoise(Signal):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude)

    def generate_sample_value(self, current_sample_time):
        return None

    def generate(self):
        whitenoise = Signal_UniformWhiteNoise(self.sample_rate, self.start_on_sample, self.end_on_sample, self.max_amplitude)
        whitenoise.generate()

        #plt.plot(np.fft.rfftfreq(len(whitenoise.sample_values)), np.fft.rfft(whitenoise.sample_values))
        #plt.show()

        #EQ

        fft_whitenoise = np.fft.rfft(whitenoise.sample_values)
        #t = np.arange(len(whitenoise.sample_values))
        S = np.fft.rfftfreq(len(whitenoise.sample_values))
        #S[0] = S[1] / 8192
        #S = 1/S
        S = S * self.sample_rate/2
        S = np.sqrt(S)
        S = 1 / np.where(S == 0, float('inf'), np.sqrt(S)) # operation on fft
        S = S / np.sqrt(np.mean(S**2)) # to preserve the energy of the white noise

        pinknoise_fft = fft_whitenoise * S

        pinknoise = np.fft.irfft(pinknoise_fft)

        # NORMALIZE
        flatten_pinknoise = list(pinknoise.flatten())
        max_sample = max(flatten_pinknoise)
        min_sample = min(flatten_pinknoise)
        abs_max_sample = max_sample

        if max_sample < abs(min_sample):
            abs_max_sample = abs(min_sample)



        pinknoise = pinknoise * (self.max_amplitude/abs_max_sample)
        #for sample in pinknoise:
        #    self.sample_values.append(sample.real)
        """
        plt.plot(np.fft.rfftfreq(len(whitenoise.sample_values)), 20*np.log10(pinknoise_fft))
        pyplot.xscale('log')
        plt.show()

        plt.plot(np.fft.rfftfreq(len(whitenoise.sample_values)), 20*np.log10(pinknoise_fft))
        pyplot.xscale('linear')
        plt.show()
        """

        self.sample_values = list(pinknoise.flatten())
        self.sample_values.append(self.sample_values[-1])


