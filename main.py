import AudioSignalGenerator
from signals.SignalPeriodic_Sinus import *
from signals.Signal_Constant import Signal_Constant
import matplotlib.pyplot as plt

if __name__ == "__main__":
    audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
    sin = SignalPeriodic_Sinus(100, 0, 100, 1, 1, math.pi)
    audioSignalGenerator.add_signal(sin)
    audioSignalGenerator.generate_samples()

    print(audioSignalGenerator.sample_values)
    plt.plot(audioSignalGenerator.timestamps,audioSignalGenerator.sample_values)
    plt.show()
