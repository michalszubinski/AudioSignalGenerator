from abc import ABC, abstractmethod
from signals.Signal import Signal

class SignalPeriodic(Signal, ABC):

    def __init__(self,  sample_rate, start_on_sample, end_on_sample, max_amplitude, min_frequency, max_frequency, frequency_variation = 'lin', direction = 'slow-fast'):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude)
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.frequency_variation = frequency_variation # lin, log, exp, hyp
        self.direction = direction # slow-fast, fast-slow

    def generate_single_sample_in_the_loop(self, current_sample_time):
        #TODO:
        # Calculate frequency change based on linear, logarithmic, exponential or hyperbolic functions
        # Calculate frequency based on direction ('slow-fast', 'fast-slow')
        pass
