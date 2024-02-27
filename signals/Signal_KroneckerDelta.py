from signals.Signal import Signal


class Signal_KroneckerDelta(Signal):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude)
        self.flag_after_first_sample = False

    def generate_sample_value(self, current_sample_time):
        if not self.flag_after_first_sample:
            self.flag_after_first_sample = True
            return self.max_amplitude

        return 0

