
import pyttsx3

class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.speaker = 0

    def text_to_speech(self, text='Hallo'):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def set_voice(self, speaker):
        self.speaker = speaker

voice = Voice()

if __name__ == '__main__':
    voice = Voice()
    voice.text_to_speech()