from signals.SignalPeriodic import SignalPeriodic
import math

class SignalPeriodic_Triangle(SignalPeriodic):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase)

    def generate_sample_value(self, current_sample_time):
        time_value = (current_sample_time * 2 * math.pi * self.frequency / (self.sample_rate)) + self.phase
        current_sin_value = math.sin(time_value)
        current_cos_value = math.cos(time_value)

        # BECAUSE OF PYTHONS CALCULATIONS
        if abs(current_sin_value) < 0.001:
            current_sin_value = 0
        if abs(current_cos_value) < 0.001:
            current_cos_value = 0

        if current_sin_value > 0 and current_cos_value > 0: # FIRST PART
            value = self.max_amplitude * self.a_expression(current_sample_time, time_value)
        elif current_sin_value > 0 and current_cos_value < 0: # SECOND PART
            value = self.max_amplitude * (1 - self.a_expression(current_sample_time, time_value))
        elif current_sin_value < 0 and current_cos_value < 0: # THIRD PART
            value = -self.max_amplitude * self.a_expression(current_sample_time, time_value)
        elif current_sin_value < 0 and current_cos_value > 0: # FORTH PART
            value = -self.max_amplitude * (1 - self.a_expression(current_sample_time, time_value))
        elif current_sin_value == 0 and current_cos_value > 0: # SPECIAL CASES
            value = 0 # OK
        elif current_sin_value == 0 and current_cos_value < 0:
            value = 0 # OK
        elif current_sin_value > 0 and current_cos_value == 0:
            value = self.max_amplitude
        elif current_sin_value < 0 and current_cos_value == 0:
            value = -self.max_amplitude # OK
        return value

    def a_expression(self, current_sample_time, time_value):
        return (time_value % (math.pi / 2)) / (math.pi/2)

