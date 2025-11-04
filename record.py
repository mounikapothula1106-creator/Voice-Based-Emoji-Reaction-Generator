import sounddevice as sd
import soundfile as sf
import sys
SAMPLE_RATE = 16000  # 16kHz is enough for speech
CHANNELS = 1
DURATION = 3
OUT_FILE = "output.wav"

def record(duration=DURATION, sr=SAMPLE_RATE, channels=CHANNELS, filename=OUT_FILE):
    print(f"Recording for {duration} seconds... Speak now.")
    try:
        recording = sd.rec(int(duration * sr), samplerate=sr, channels=channels, dtype='int16')
        sd.wait()  # wait until recording completes
        sf.write(filename, recording, sr, subtype='PCM_16')
        print(f"Saved recording to '{filename}' successfully.")
    except Exception as e:
        print("Recording failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    record()
