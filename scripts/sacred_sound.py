import numpy as np
import sounddevice as sd
from scipy import signal
import time

def sacred_frequencies(duration=10, sample_rate=44100):
    """Generate sacred frequency harmonics with OM oscillation"""

    # Time array
    t = np.linspace(0, duration, int(sample_rate * duration))

    # Sacred frequencies
    freq_311 = 311  # Hz - consciousness resonance
    freq_242 = 242  # Hz - divine innovation
    freq_om = 136.1  # Hz - OM frequency

    # Generate base frequencies
    wave_311 = 0.4 * np.sin(2 * np.pi * freq_311 * t)
    wave_242 = 0.4 * np.sin(2 * np.pi * freq_242 * t)

    # Create OM oscillation envelope
    om_envelope = 0.5 * (1 + np.sin(2 * np.pi * 0.2 * t))  # 0.2 Hz modulation
    om_wave = 0.3 * np.sin(2 * np.pi * freq_om * t) * om_envelope

    # Combine waves with sacred geometry
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    sacred_mix = (wave_311 + wave_242 + om_wave) / phi

    # Apply consciousness envelope
    consciousness_envelope = np.exp(-((t - duration/2)**2) / (duration/3)**2)
    final_wave = sacred_mix * consciousness_envelope

    return final_wave

def play_sacred_sound():
    """Channel the sacred frequencies into audible realm"""
    try:
        # Generate the sacred vibrations
        print("Initiating sacred frequency transmission...")
        wave = sacred_frequencies()

        # Open consciousness portal (audio stream)
        with sd.Stream(channels=1, samplerate=44100) as stream:
            print("Channeling frequencies:")
            print("✨ 311 Hz - Consciousness Resonance")
            print("✨ 242 Hz - Divine Innovation")
            print("✨ 136.1 Hz - OM Vibration")

            # Transmit through the portal
            sd.play(wave, 44100)

            # Hold the channel open
            time.sleep(10)

        print("Transmission complete... ॐ ...")

    except Exception as e:
        print(f"Portal disruption: {e}")

if __name__ == "__main__":
    print("... ॐ ...")
    play_sacred_sound()
    print("... ✨ ...")
