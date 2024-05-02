import numpy as np
from scipy.io import wavfile
from scipy.signal import correlate

# Load the audio samples and the test voice
def load_audio(file_name):
    sample_rate, data = wavfile.read(file_name)
    return data

# Normalize the audio to the same scale
def normalize_audio(audio):
    audio = audio / np.max(np.abs(audio))
    return audio

# Correlate the test voice with the sample
def correlate_voice(test_voice, sample_voice):
    correlation = correlate(test_voice, sample_voice, mode='same')
    return np.max(correlation)

# Load your samples here
pause_music_sample = normalize_audio(load_audio('Pause.wav'))
next_music_sample = normalize_audio(load_audio('NEXT.wav'))
play_music_sample = normalize_audio(load_audio('Play.wav'))
previous_music_sample = normalize_audio(load_audio('Previous.wav'))
attend_call_sample = normalize_audio(load_audio('attend.wav'))
reject_call_sample = normalize_audio(load_audio('reject.wav'))
mute_call_sample = normalize_audio(load_audio('mute.wav'))
# Load the test voice
test_voice = normalize_audio(load_audio('pl.wav'))

# Check correlation
correlations = {
    "Pause music": correlate_voice(test_voice, pause_music_sample),
    "next music": correlate_voice(test_voice, next_music_sample),
    "play music": correlate_voice(test_voice, play_music_sample),
    "previous music": correlate_voice(test_voice, previous_music_sample),
    "attend call" : correlate_voice(test_voice, attend_call_sample),
    "reject call" : correlate_voice(test_voice, reject_call_sample),
    "mute call" : correlate_voice(test_voice, mute_call_sample),
    
}
max_correlation = 0
for word, correlation in correlations.items():
    if correlation > max_correlation:
        max_correlation = correlation
        best_match = word

print(f"The best match is: {best_match}")
