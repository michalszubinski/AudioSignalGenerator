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
    def generate(self):
        pass

    def clear(self):
        self.sample_values.clear()
        self.timestamps.clear()

    def calculate_rms(self): #TODO
        return 1.0