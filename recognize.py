#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
from tts_test.config import GSTTKEY
import speech_recognition as sr
def get_string_from_text_microphone():

    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    print("Analyzing...")
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        #to use another API key, use `r.recognize_google(audio, key="SOME FUCKING KEY")`
        # instead of `r.recognize_google(audio)`

        if GSTTKEY is not None:
            text = r.recognize_google(audio, key = GSTTKEY)
        else:
            text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None