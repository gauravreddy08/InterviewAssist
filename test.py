import sounddevice as sd
import numpy as np
from pydub import AudioSegment
import keyboard
import threading

# Initialize the variables
sample_rate = 44100
channels = 2
audio_data = []
recording = False  # Variable to track recording state
sd.default.device = 1

def record_audio():
    global audio_data
    with sd.InputStream(samplerate=sample_rate, channels=channels, dtype='int16') as stream:
        while recording:
            audio_data.append(stream.read(1024)[0])

def start_recording():
    global recording, audio_data
    audio_data = []
    recording = True
    print("Recording started...")
    threading.Thread(target=record_audio).start()

def stop_recording():
    global recording
    recording = False
    print("Recording stopped")
    # Convert the list of numpy arrays to a single numpy array
    recorded_audio = np.concatenate(audio_data, axis=0)

    # Convert to an AudioSegment
    audio_segment = AudioSegment(
        recorded_audio.tobytes(),
        frame_rate=sample_rate,
        sample_width=recorded_audio.dtype.itemsize,
        channels=channels
    )

    # Save the audio as an MP3 file
    output_file = "output.mp3"
    audio_segment.export(output_file, format="mp3")
    print(f"Audio saved as {output_file}")

def toggle_recording():
    global recording
    if not recording:
        start_recording()
    else:
        stop_recording()

def start():
    print("Press the '=' key to start/stop recording.")
    # Wait for the '=' key press
    keyboard.wait('=')
    toggle_recording()
    
    keyboard.wait('=')
    toggle_recording()

if __name__ == "__main__":
    pass
