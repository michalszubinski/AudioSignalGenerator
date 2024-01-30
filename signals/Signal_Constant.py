from signals.Signal import Signal


class Signal_Constant(Signal):
    def __init__(self, sample_rate, start_on_sample, end_on_sample, max_amplitude):
        super().__init__(sample_rate, start_on_sample, end_on_sample, max_amplitude)

    def generate(self):
        self.clear()
        current_sample_time = self.start_on_sample

        while current_sample_time <= self.end_on_sample:

            self.timestamps.append(current_sample_time)
            self.sample_values.append(self.max_amplitude)

            current_sample_time += 1

