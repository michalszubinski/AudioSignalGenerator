from signals.SignalPeriodic import SignalPeriodic
import math

class SignalPeriodic_Sinus(SignalPeriodic):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase)

    def generate(self):  # TODO
        self.clear()
        current_sample_time = self.start_on_sample

        while current_sample_time <= self.end_on_sample:
            self.timestamps.append(current_sample_time) # timestamp

            # value
            value = self.max_amplitude * math.sin((current_sample_time*2*math.pi*self.frequency/(self.sample_rate)) + self.phase)
            self.sample_values.append(value)

            current_sample_time += 1
