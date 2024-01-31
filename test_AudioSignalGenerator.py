import math
import unittest

import AudioSignalGenerator
from signals.SignalPeriodic_Sinus import SignalPeriodic_Sinus
from signals.Signal_Constant import Signal_Constant


class MyTestCase(unittest.TestCase):
    def test_generate_signal_constant_in_range_1_3_check_amplitude_and_length(self):
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
        const = Signal_Constant(44100, 1, 3, 0.2)
        audioSignalGenerator.add_signal(const)
        audioSignalGenerator.generate_samples()

        self.assertEqual(len(audioSignalGenerator.sample_values), 4)
        self.assertEqual(len(audioSignalGenerator.timestamps), 4)
        self.assertEqual(audioSignalGenerator.sample_values, [0, 0.2, 0.2, 0.2])
        self.assertEqual(audioSignalGenerator.timestamps, [0, 1, 2, 3])

    def test_generate_two_signal_constants_in_range_1_3_check_amplitude_and_length(self):
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
        const1 = Signal_Constant(44100, 1, 3, 0.2)
        const2 = Signal_Constant(44100, 1, 3, 0.3)
        audioSignalGenerator.add_signal(const1)
        audioSignalGenerator.add_signal(const2)
        audioSignalGenerator.generate_samples()

        self.assertEqual(len(audioSignalGenerator.sample_values), 4)
        self.assertEqual(len(audioSignalGenerator.timestamps), 4)
        self.assertEqual(audioSignalGenerator.sample_values, [0, 0.5, 0.5, 0.5])
        self.assertEqual(audioSignalGenerator.timestamps, [0, 1, 2, 3])

    def test_generate_sinus_sample_rate_100_amplitude_1_phase_pi(self): #TODO
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(100, 16)
        sin = SignalPeriodic_Sinus(100, 0, 100, 1, 1, math.pi)
        audioSignalGenerator.add_signal(sin)
        audioSignalGenerator.generate_samples()

        print(audioSignalGenerator.sample_values)
        #plt.plot(audioSignalGenerator.timestamps, audioSignalGenerator.sample_values)
        #plt.show()


if __name__ == '__main__':
    unittest.main()
