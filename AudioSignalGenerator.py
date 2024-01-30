from signals import *

class AudioSignalGenerator:

    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.duration_seconds = 0
        self.samples = []
        self.timestamps = []
        self.signals = list()

    def add_signal(self, signal):
        self.signals.append(signal)

    def generate_samples(self):
        for signal in self.signals:

            signal.generate()
            current_sample_time = signal.start_on_sample

            while len(self.samples) < signal.start_on_sample:
                self.samples.append(0)
                self.timestamps.append(len(self.samples) - 1)

            while current_sample_time <= signal.end_on_sample:
                if len(self.samples) == current_sample_time:
                    self.samples.append(signal.sample_values[current_sample_time - signal.start_on_sample])
                    self.timestamps.append(current_sample_time)
                else:
                    self.samples[current_sample_time] += signal.sample_values[current_sample_time - signal.start_on_sample]

                current_sample_time += 1

