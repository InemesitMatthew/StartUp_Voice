import argparse
import pyttsx3
import datetime
from pydub import AudioSegment
from pydub.playback import play

def get_time_of_day():
    # Get the current time
    current_time = datetime.datetime.now().time()

    # Determine the time of day
    if 5 <= current_time.hour < 12:
        return "morning"
    elif 12 <= current_time.hour < 18:
        return "afternoon"
    else:
        return "night"

def play_regular_voice(voice_line):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Say the specified voice line
    engine.say(voice_line)

    # Wait for the speech to finish
    engine.runAndWait()

def play_custom_voice(audio_file):
    # Load the custom voice recording
    sound = AudioSegment.from_wav(audio_file)

    # Play the custom voice recording
    play(sound)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Play a startup voice.")
    parser.add_argument("--custom", action="store_true", help="Play a custom voice recording.")
    args = parser.parse_args()

    if args.custom:
        # Get the path to the custom audio file from the user
        custom_audio_file = input("Enter the path to your custom voice recording (WAV format): ")

        # Play the custom voice recording
        play_custom_voice(custom_audio_file)
    else:
        # Determine the time of day
        time_of_day = get_time_of_day()

        # Set different voice lines based on the time of day
        if time_of_day == "morning":
            voice_line = "Good morning! Time to start your day."
        elif time_of_day == "afternoon":
            voice_line = "Good afternoon! Hope you're having a productive day."
        else:
            voice_line = "Good night! Time to rest and recharge."

        # Play the regular voice based on the determined time of day
        play_regular_voice(voice_line)
