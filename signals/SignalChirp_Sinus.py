from signals.SignalChirp import SignalChirp
from signals.SignalPeriodic import SignalPeriodic
import math


class SignalChirp_Sinus(SignalChirp):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude, min_frequency, max_frequency,
                 frequency_variation='lin', initial_frequency_change='slow-fast', start_on_min_frequency=True, phase=0):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude, min_frequency, max_frequency,
                         frequency_variation, initial_frequency_change, start_on_min_frequency)
        self.phase = phase

    def generate_sample_value(self, current_sample_time):
        value = self.max_amplitude * math.sin(
            (current_sample_time * 2 * math.pi * self.current_frequency / self.sample_rate) + self.phase)
        return value
