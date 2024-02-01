from signals.Signal import Signal
import random


class Signal_UniformWhiteNoise(Signal):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude)

    def generate_sample_value(self, current_sample_time):
        return random.uniform(-self.max_amplitude, self.max_amplitude)
