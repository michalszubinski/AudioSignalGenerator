from signals.SignalPeriodic import SignalPeriodic
import math

class SignalPeriodic_Sawtooth(SignalPeriodic):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase)

    def generate_sample_value(self, current_sample_time):
        time_value = (current_sample_time * 2 * math.pi * self.frequency / (self.sample_rate)) + self.phase

        value = -self.max_amplitude * (1 - (2*self.a_expression(current_sample_time, time_value)))
        return value


    def a_expression(self, current_sample_time, time_value):
        return (time_value % (math.pi * 2)) / (math.pi*2)

