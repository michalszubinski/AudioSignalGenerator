import math
import os
import unittest
import wave

import numpy as np
import scipy

import AudioSignalGenerator
from signals.SignalPeriodic_Sinus import SignalPeriodic_Sinus
from signals.Signal_Constant import Signal_Constant
from signals.Signal_GaussianWhiteNoise import Signal_GuassianWhiteNoise
from signals.Signal_UniformWhiteNoise import Signal_UniformWhiteNoise
from utilities.Converter import Converter
from utilities.DBFS import DBFS


class MyTestCase(unittest.TestCase):
    # Generating signals
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

    def test_generate_sinus_sample_rate_100_amplitude_1_end_on_sample_100(self):
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(100, 16)
        sin = SignalPeriodic_Sinus(100, 0, 100, 1, 1, 0)
        audioSignalGenerator.add_signal(sin)
        audioSignalGenerator.generate_samples()

        self.assertEqual(len(audioSignalGenerator.timestamps), 101)

        self.assertLess(audioSignalGenerator.sample_values[0], 0.05)
        self.assertGreater(audioSignalGenerator.sample_values[0], -0.05)

        self.assertLessEqual(audioSignalGenerator.sample_values[25], 1)
        self.assertGreater(audioSignalGenerator.sample_values[25], 0.95)

        self.assertLess(audioSignalGenerator.sample_values[50], 0.05)
        self.assertGreater(audioSignalGenerator.sample_values[50], -0.05)

        self.assertLess(audioSignalGenerator.sample_values[75], -0.95)
        self.assertGreaterEqual(audioSignalGenerator.sample_values[75], -1)

    def test_generate_sinus_sample_rate_100_amplitude_1_end_on_sample_100_phase_pi(self):
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(100, 16)
        sin = SignalPeriodic_Sinus(100, 0, 100, 1, 1, math.pi)
        audioSignalGenerator.add_signal(sin)
        audioSignalGenerator.generate_samples()

        self.assertEqual(len(audioSignalGenerator.timestamps), 101)

        self.assertLessEqual(audioSignalGenerator.sample_values[75], 1)
        self.assertGreater(audioSignalGenerator.sample_values[75], 0.95)

        self.assertLess(audioSignalGenerator.sample_values[0], 0.05)
        self.assertGreater(audioSignalGenerator.sample_values[0], -0.05)

        self.assertLess(audioSignalGenerator.sample_values[25], -0.95)
        self.assertGreaterEqual(audioSignalGenerator.sample_values[25], -1)

        self.assertLess(audioSignalGenerator.sample_values[50], 0.05)
        self.assertGreater(audioSignalGenerator.sample_values[50], -0.05)

    def test_generate_two_sinus_sample_rate_100_amplitude_1_end_on_sample_100_opposite_phase(self):
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(100, 16)
        sin1 = SignalPeriodic_Sinus(100, 0, 100, 1, 1, 0)
        sin2 = SignalPeriodic_Sinus(100, 0, 100, 1, 1, math.pi)
        audioSignalGenerator.add_signal(sin1)
        audioSignalGenerator.add_signal(sin2)
        audioSignalGenerator.generate_samples()

        self.assertEqual(len(audioSignalGenerator.timestamps), 101)

        for sample in audioSignalGenerator.sample_values:
            self.assertLess(sample, 0.05)
            self.assertGreater(sample, -0.05)

    # Generate noises
    def test_generate_uniform_white_noise_44100_16_500_samples(self): #TODO
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
        uniformwhitenoise = Signal_UniformWhiteNoise(44100, 0, 500, 0.1)
        audioSignalGenerator.add_signal(uniformwhitenoise)
        audioSignalGenerator.generate_samples()

        self.assertEqual(len(audioSignalGenerator.sample_values), 501)
        # find the conditions to check if the noise is correct


    def test_generate_gaussian_white_noise_44100_16_500_samples(self): #TODO
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
        guassianwhitenoise = Signal_GuassianWhiteNoise(44100, 0, 500, 0.1)
        audioSignalGenerator.add_signal(guassianwhitenoise)
        audioSignalGenerator.generate_samples()

        self.assertEqual(len(audioSignalGenerator.sample_values), 501)
        # find the conditions to check if the noise is correct


    # Save file
    def test_generate_and_save_as_wav_44100_16_sin_1000hz_1s_mono(self):
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
        sin = SignalPeriodic_Sinus(44100, 0, 44100, 0.1, 1000, 0)
        audioSignalGenerator.add_signal(sin)
        audioSignalGenerator.generate_samples()

        filename = 'test_generate_and_save_as_wav_44100_16_sin_1000hz_1s_mono.wav'

        audioSignalGenerator.save_audio(filename)
        self.assertTrue(os.path.exists(filename))

        wav_file = wave.open(filename, 'r') # OPEN FILE

        self.assertEqual(wav_file.getnchannels(), 1)
        self.assertEqual(wav_file.getframerate(), 44100)
        self.assertEqual(wav_file.getsampwidth(), 2)
        self.assertEqual(wav_file.getnframes(), 44101) # number of frames

        # Check if samples are similar

        wav_file.close() # CLOSE FILE

        os.remove(filename) # REMOVE FILE

    # Signals and RMS
    def test_calculate_rms_sin_1k_1_amp_1s(self):
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
        sin = SignalPeriodic_Sinus(44100, 0, 44100, 1, 1000, 0)
        audioSignalGenerator.add_signal(sin)
        audioSignalGenerator.generate_samples()

        rms = sin.calculate_rms()
        # sqrt(2) = 0.70710678
        self.assertLessEqual(rms, 0.7071 + 0.02)
        self.assertGreaterEqual(rms, 0.7071 - 0.02)

    def test_calculate_rms_constant_signal_1000_samples(self):
        audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
        const = Signal_Constant(44100, 0, 1000, 0.5)
        audioSignalGenerator.add_signal(const)
        audioSignalGenerator.generate_samples()

        rms = const.calculate_rms()

        self.assertLessEqual(rms, 0.5 + 0.01)
        self.assertGreaterEqual(rms, 0.5 - 0.01)
        self.assertEqual(rms, 0.5)

    # Convertion
    def test_convert_linear_to_dbfs_value_1(self):
        temp_dbfs = Converter.linear_to_dbfs(1)
        self.assertLessEqual(temp_dbfs.DBFS,0.01)
        self.assertGreaterEqual(temp_dbfs.DBFS,-0.01)
        self.assertEqual(temp_dbfs.sign, 1)

    def test_convert_linear_to_dbfs_value_negative_1(self):
        temp_dbfs = Converter.linear_to_dbfs(-1)
        self.assertLessEqual(temp_dbfs.DBFS,0.01)
        self.assertGreaterEqual(temp_dbfs.DBFS,-0.01)
        self.assertEqual(temp_dbfs.sign, -1)


    def test_convert_linear_to_dbfs_value_05(self):
        temp_dbfs = Converter.linear_to_dbfs(0.5)
        self.assertLessEqual(temp_dbfs.DBFS, 5.97)
        self.assertGreaterEqual(temp_dbfs.DBFS, -6.03)
        self.assertEqual(temp_dbfs.sign, 1)


    def test_convert_linear_to_dbfs_value_025(self):
        temp_dbfs = Converter.linear_to_dbfs(0.25)
        self.assertLessEqual(temp_dbfs.DBFS, 11.95)
        self.assertGreaterEqual(temp_dbfs.DBFS, -12.05)
        self.assertEqual(temp_dbfs.sign, 1)

    def test_convert_dbfs_to_linear_value_0(self):
        temp_linear = Converter.dbfs_to_linear(DBFS(0))
        self.assertEqual(temp_linear, 1)

    def test_convert_dbfs_to_linear_value_0_sign_negative(self):
        temp_linear = Converter.dbfs_to_linear(DBFS(0,-1))
        self.assertEqual(temp_linear, -1)

    def test_convert_dbfs_to_linear_value_minus3_sign_negative(self):
        temp_linear = Converter.dbfs_to_linear(DBFS(-3,-1))
        self.assertLessEqual(temp_linear, -0.7071 + 0.01)
        self.assertGreaterEqual(temp_linear, -0.7071 - 0.01)

    def test_convert_dbfs_to_linear_value_minus6(self):
        temp_linear = Converter.dbfs_to_linear(DBFS(-6))
        self.assertLessEqual(temp_linear, 0.51)
        self.assertGreaterEqual(temp_linear, 0.49)

    def test_convert_linear_to_dbfs_bits_value_32768_bits_16(self):
        temp_dbfs = Converter.linear_to_dbfs_bits(32768,16)
        self.assertLessEqual(temp_dbfs.DBFS, 0.01)
        self.assertGreaterEqual(temp_dbfs.DBFS, -0.01)
        self.assertEqual(temp_dbfs.sign, 1)

    def test_convert_linear_to_dbfs_bits_value_16384_bits_16(self):
        temp_dbfs = Converter.linear_to_dbfs_bits(16384, 16)
        self.assertLessEqual(temp_dbfs.DBFS, -5.97)
        self.assertGreaterEqual(temp_dbfs.DBFS, -6.03)
        self.assertEqual(temp_dbfs.sign, 1)

    def test_convert_linear_to_dbfs_bits_value_minus16384_bits_16(self):
        temp_dbfs = Converter.linear_to_dbfs_bits(16384, 16)
        self.assertLessEqual(temp_dbfs.DBFS, -5.97)
        self.assertGreaterEqual(temp_dbfs.DBFS, -6.03)
        self.assertEqual(temp_dbfs.sign, 1)

    def test_convert_dbfs_to_linear_bits_value_0_bits_16(self):
        temp_linear = Converter.dbfs_to_linear_bits(DBFS(0),16)
        self.assertEqual(temp_linear, 32768)

    def test_convert_dbfs_to_linear_bits_value_0_sign_negative_bits_16(self):
        temp_linear = Converter.dbfs_to_linear_bits(DBFS(0,-1),16)
        self.assertEqual(temp_linear, -32768)

    def test_convert_dbfs_to_linear_bits_value_minus6_sign_negative_bits_16(self):
        temp_linear = Converter.dbfs_to_linear_bits(DBFS(-6,-1),16)
        self.assertLessEqual(temp_linear, -16384 + 50)
        self.assertGreaterEqual(temp_linear, -16384 - 50)

    def test_convert_dbfs_to_linear_bits_value_minus6_bits_16(self):
        temp_linear = Converter.dbfs_to_linear_bits(DBFS(-6),16)
        self.assertLessEqual(temp_linear, 16384 + 50)
        self.assertGreaterEqual(temp_linear, 16384 - 50)



if __name__ == '__main__':
    unittest.main()
