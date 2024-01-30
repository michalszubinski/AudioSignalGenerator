import AudioSignalGenerator
from signals.SignalPeriodic_Sinus import *
from signals.Signal_Constant import Signal_Constant

if __name__ == "__main__":
    audioSignalGenerator = AudioSignalGenerator.AudioSignalGenerator(44100)
    sinus = Signal_Constant(44100, 1, 3,0.2)
    audioSignalGenerator.add_signal(sinus)
    audioSignalGenerator.generate_samples()
    print(audioSignalGenerator.samples)
    print(audioSignalGenerator.timestamps)