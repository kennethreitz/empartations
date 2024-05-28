from pydub import AudioSegment
from pydub.generators import Sine
import simpleaudio as sa
import io


def generate_tone(frequency, duration_ms=1000):
    # Generate a sine wave at the specified frequency and duration
    tone = Sine(frequency).to_audio_segment(duration=duration_ms)
    return tone


def play_audio(audio_segment):
    # Play the audio segment
    playback = sa.play_buffer(
        audio_segment.raw_data,
        num_channels=audio_segment.channels,
        bytes_per_sample=audio_segment.sample_width,
        sample_rate=audio_segment.frame_rate,
    )
    playback.wait_done()


def main():
    frequencies = [7.83, 14, 20, 26]  # Schumann resonances frequencies in Hz
    duration = 6000  # Duration for each tone in milliseconds

    for freq in frequencies:
        print(f"Playing {freq} Hz")
        tone = generate_tone(freq, duration)
        play_audio(tone)


if __name__ == "__main__":
    main()
