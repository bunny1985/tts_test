import pyttsx3
import random
from tts_test.recognize import get_string_from_text_microphone

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello! Let's play the game. Guess the number between 1 and 100")

number = random.randrange(1, 100)
guess = -1
while guess != number:
    speak("Say the number")
    text = get_string_from_text_microphone()
    if text is not None:
        try:
            guess = int(text)
        except:
            speak(text + "is not a number")
    if guess > number:
        speak("To high...")
    elif number > guess:
        speak("To low...")
    else:
        speak("That's right! Congratulations!")
