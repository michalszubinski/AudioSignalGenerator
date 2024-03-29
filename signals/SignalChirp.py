from abc import ABC, abstractmethod

import numpy as np

from signals.Signal import Signal


class SignalChirp(Signal, ABC):

    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude, min_frequency, max_frequency,
                 frequency_variation='lin', start_on_min_frequency=True):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude)
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.frequency_variation = frequency_variation  # lin, log, exp, hyp
        self.start_on_min_frequency = start_on_min_frequency
        self.current_frequency = min_frequency
        self.delta_frequency_lin = 0
        self.fixed_frequency_list = list()
        self.fixed_frequency_list_position = 0

        self.clear()

    def clear(self):
        self.sample_values.clear()
        self.timestamps.clear()

        self.fixed_frequency_list_position = 0

        self.delta_frequency_lin = (self.max_frequency - self.min_frequency) / (self.end_on_sample - self.start_on_sample)
        if self.frequency_variation == 'log':
            self.fixed_frequency_list = np.geomspace(self.min_frequency, self.max_frequency, self.end_on_sample - self.start_on_sample + 1)

    def change_values_after_generating_a_sample(self, current_sample_time):
        # TODO:
        # Calculate frequency change based on linear, logarithmic, exponential or hyperbolic functions
        # Calculate frequency based on direction ('slow-fast', 'fast-slow')
        if self.frequency_variation == 'lin':
            self.current_frequency += self.delta_frequency_lin
        if self.frequency_variation == 'log':
            self.current_frequency = self.fixed_frequency_list[self.fixed_frequency_list_position]
            self.fixed_frequency_list_position += 1



    def post_sample_generation(self):
        if not self.start_on_min_frequency:
            #self.sample_values = self.sample_values[::-1]
            self.sample_values = [-value for value in self.sample_values[::-1]] # MULTIPIES -1 AND REVERSES THE LIST
