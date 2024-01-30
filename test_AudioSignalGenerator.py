import unittest

import AudioSignalGenerator
from signals.Signal_Constant import Signal_Constant


class MyTestCase(unittest.TestCase):
    def test_generate_signal_constant_in_range_1_3_check_amplitude_and_length(self):
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100)
        const = Signal_Constant(44100, 1, 3, 0.2)
        audioSignalGenerator.add_signal(const)
        audioSignalGenerator.generate_samples()

        self.assertEqual(len(audioSignalGenerator.sample_values), 4)
        self.assertEqual(len(audioSignalGenerator.timestamps), 4)
        self.assertEqual(audioSignalGenerator.sample_values, [0, 0.2, 0.2, 0.2])
        self.assertEqual(audioSignalGenerator.timestamps, [0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
