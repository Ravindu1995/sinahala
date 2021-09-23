import os
from pocketsphinx import AudioFile, get_model_path, get_data_path

model_path = get_model_path()
data_path = get_data_path()

config = {
    'verbose': False,
    'audio_file': os.path.join(data_path, 'C:/Users/home/Desktop/4th year/Research/Blockchain/blockchain_client (1)/speech_recognition/output/nine.wav'),
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'C:/Users/home/Desktop/4th year/Research/Blockchain/blockchain_client (1)/speech_recognition/output/sinhala.ci_cont'),
    'lm': os.path.join(model_path, 'C:/Users/home/Desktop/4th year/Research/Blockchain/blockchain_client (1)/speech_recognition/output/sinhala.dic'),
    'dict': os.path.join(model_path, '/speech_recognition/output/sinhala.lm')
}

audio = AudioFile(**config)
for phrase in audio:
    print(phrase)
