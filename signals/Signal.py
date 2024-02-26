import math
from abc import ABC, abstractmethod

from utilities.Calculator import Calculator


class Signal(ABC):

    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude):
        self.sample_rate = sample_rate
        self.start_on_sample = start_on_sample
        self.end_on_sample = end_on_sample
        self.max_amplitude = max_amplitude
        self.sample_values = []
        self.timestamps = []
        self.forced_normalization = False

    @abstractmethod
    def generate_sample_value(self, current_sample_time):
        return 1.0

    def generate(self):
        self.clear()
        current_sample_time = self.start_on_sample
        self.before_generating_any_samples()

        while current_sample_time <= self.end_on_sample:
            self.change_values_before_generating_a_sample(current_sample_time)
            current_sample_time = self.generate_single_sample_in_the_loop(current_sample_time)
            self.change_values_after_generating_a_sample(current_sample_time)
        self.post_sample_generation()

        if self.forced_normalization:
            self.normalize()

    def generate_single_sample_in_the_loop(self, current_sample_time):
        self.timestamps.append(current_sample_time)
        self.sample_values.append(self.generate_sample_value(current_sample_time))

        current_sample_time += 1
        return current_sample_time

    def clear(self):
        self.sample_values.clear()
        self.timestamps.clear()

    def calculate_rms(self):
        return self.calculate_rms_timeframe(self.start_on_sample, self.end_on_sample)

    def calculate_rms_timeframe(self, rms_timeframe_start, rms_timeframe_end):
        try:
            current_sample = rms_timeframe_start

            rms = 0

            while current_sample <= rms_timeframe_end:
                rms += pow(self.sample_values[current_sample], 2)
                current_sample += 1
            rms = math.sqrt(rms/(rms_timeframe_end - rms_timeframe_start + 1))
            return rms
        except Exception as e:
            print(e)
            print('Error in calculating rms timeframe - signals/Signal.py')
            return None

    def change_values_before_generating_a_sample(self, current_sample_time):
        pass

    def post_sample_generation(self):
        pass

    def change_values_after_generating_a_sample(self, current_sample_time):
        pass
    def normalize(self):
        max_sample = max(self.sample_values)
        min_sample = min(self.sample_values)
        abs_max_sample = max_sample

        if max_sample < abs(min_sample):
            abs_max_sample = abs(min_sample)

        self.sample_values = [sample * (self.max_amplitude/abs_max_sample) for sample in self.sample_values]
        #self.sample_values = self.sample_values * (self.max_amplitude/abs_max_sample)

    def calculate_frequency(self):
        return Calculator.get_signal_frequency(self)

    def before_generating_any_samples(self):
        pass
