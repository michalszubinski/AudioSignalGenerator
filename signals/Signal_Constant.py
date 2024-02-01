from signals.Signal import Signal


class Signal_Constant(Signal):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude)

    def generate_sample_value(self, current_sample_time):
        return self.max_amplitude

