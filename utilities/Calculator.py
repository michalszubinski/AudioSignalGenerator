import numpy as np


class Calculator:

    @staticmethod
    def get_signal_frequency(signal):
        return Calculator.get_frequency_from_sample_values(signal.sample_values, signal.sample_rate)

    @staticmethod
    def get_frequency_from_sample_values(sample_values, sample_rate):
        no_samples = len(sample_values)  # length of the signal
        k = np.arange(no_samples)
        T = no_samples / sample_rate

        frequency_range = k / T  # two sides frequency range
        frequency_range = frequency_range[:len(frequency_range) // 2]  # one side frequency range

        Y = np.fft.fft(sample_values) / no_samples  # dft and normalization
        Y = Y[:no_samples // 2]

        Y_list = list(Y)

        max_index_fft_value = Y_list.index(max(Y_list))
        return frequency_range[max_index_fft_value]