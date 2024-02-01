import AudioSignalGenerator
from signals.SignalPeriodic_Sinus import *
from signals.Signal_Constant import Signal_Constant
import matplotlib.pyplot as plt

from signals.Signal_GaussianWhiteNoise import Signal_GuassianWhiteNoise
from signals.Signal_UniformWhiteNoise import Signal_UniformWhiteNoise

if __name__ == "__main__":
    audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100, 16)
    guassianwhitenoise = Signal_GuassianWhiteNoise(44100, 0, 500, 0.1)
    audioSignalGenerator.add_signal(guassianwhitenoise)
    audioSignalGenerator.generate_samples()

    print(audioSignalGenerator.sample_values)
    plt.plot(audioSignalGenerator.timestamps,audioSignalGenerator.sample_values)
    plt.show()
