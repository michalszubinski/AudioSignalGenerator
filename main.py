import AudioSignalGenerator
from signals.SignalPeriodic_Sinus import *
from signals.Signal_Constant import Signal_Constant
import matplotlib.pyplot as plt

if __name__ == "__main__":
    audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
    sin = SignalPeriodic_Sinus(44100, 0, 44100, 0.1, 1000, 0)
    audioSignalGenerator.add_signal(sin)
    audioSignalGenerator.generate_samples()

    #print(audioSignalGenerator.sample_values)
    #plt.plot(audioSignalGenerator.timestamps,audioSignalGenerator.sample_values)
    #plt.show()

    audioSignalGenerator.save_audio('test.wav')
