from signals.SignalPeriodic import SignalPeriodic
import math

class SignalPeriodic_PulseWave(SignalPeriodic):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase, duty):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase)
        self.duty = duty
        self.level_change_phase = 0
        self.time_level_change_positive = 0
        self.time_level_change_negative = 0

    def generate_sample_value(self, current_sample_time):
        time_value = (current_sample_time * 2 * math.pi * self.frequency / (self.sample_rate)) + self.phase
        time_value_in_period = (time_value % (math.pi * 2)) / (math.pi * 2)

        if self.duty >= 1:
            return self.max_amplitude

        if time_value_in_period <= self.time_level_change_positive or time_value_in_period >= self.time_level_change_negative:
            value = self.max_amplitude
        else:
            value = 0
        return value

    def before_generating_any_samples(self):
        if self.duty > 1:
            self.level_change_phase = 2 * math.pi + 0.01
        elif self.duty < 0:
            self.level_change_phase = 0
        else:
            self.level_change_phase = 2 * math.pi * self.duty / 2

        self.time_level_change_positive = self.level_change_phase / (math.pi*2)
        self.time_level_change_negative = (2*math.pi - self.level_change_phase) / (math.pi*2)





