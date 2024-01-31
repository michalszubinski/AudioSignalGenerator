from abc import ABC, abstractmethod
from signals.Signal import Signal

class SignalPeriodic(Signal, ABC):

    def __init__(self,  sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency, phase):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude)
        self.frequency = frequency
        self.phase = phase

    def calculate_period_rms(self): #TODO
        return 1.0