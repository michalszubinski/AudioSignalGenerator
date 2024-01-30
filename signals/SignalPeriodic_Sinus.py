from signals.SignalPeriodic import SignalPeriodic

class SignalPeriodic_Sinus(SignalPeriodic):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude, frequency)

    def generate(self):  # TODO
        pass
