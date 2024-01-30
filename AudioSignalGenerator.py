from signals import *

class AudioSignalGenerator:

    def __init__(self, sample_rate, bit_rate):
        self.sample_rate = sample_rate
        self.bit_rate = bit_rate
        self.duration_seconds = 0
        self.sample_values = []
        self.timestamps = []
        self.signals = list()

    def add_signal(self, signal):
        self.signals.append(signal)

    def generate_samples(self):
        for signal in self.signals:

            signal.generate()
            current_sample_time = signal.start_on_sample

            while len(self.sample_values) < signal.start_on_sample:
                self.sample_values.append(0)
                self.timestamps.append(len(self.sample_values) - 1)

            while current_sample_time <= signal.end_on_sample:
                if len(self.sample_values) == current_sample_time:
                    self.sample_values.append(signal.sample_values[current_sample_time - signal.start_on_sample])
                    self.timestamps.append(current_sample_time)
                else:
                    self.sample_values[current_sample_time] += signal.sample_values[current_sample_time - signal.start_on_sample]

                current_sample_time += 1

        for sample in self.sample_values: # PREVENT CLIPPING
            if sample > 1:
                sample = 1
            elif sample < -1:
                sample = -1

    def save_audio(self,filename): #TODO
        pass

