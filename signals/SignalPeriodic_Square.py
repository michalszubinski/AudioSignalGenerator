from signals.SignalPeriodic import SignalPeriodic
import math

class SignalPeriodic_Square(SignalPeriodic):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase)

    def generate_sample_value(self, current_sample_time):
        if math.sin((current_sample_time * 2 * math.pi * self.frequency / (self.sample_rate)) + self.phase) >= 0:
            value = self.max_amplitude
        else:
            value = -self.max_amplitude
        return value

