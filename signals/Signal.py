from abc import ABC, abstractmethod

class Signal(ABC):

    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude):
        self.sample_rate = sample_rate
        self.start_on_sample = start_on_sample
        self.end_on_sample = end_on_sample
        self.max_amplitude = max_amplitude
        self.sample_values = []
        self.timestamps = []

    @abstractmethod
    def generate_sample_value(self, current_sample_time):
        return 1.0

    def generate(self):
        self.clear()
        current_sample_time = self.start_on_sample

        while current_sample_time <= self.end_on_sample:

            self.timestamps.append(current_sample_time)
            self.sample_values.append(self.generate_sample_value(current_sample_time))

            current_sample_time += 1

    def clear(self):
        self.sample_values.clear()
        self.timestamps.clear()

    def calculate_rms(self): #TODO
        return 1.0