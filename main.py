from recognition import  Ears
from voice import voice
from commands import Command
import time


listener = Ears()
text_gen = listener.listen()
voice.text_to_speech('Hello! I am maiden!')
for text in text_gen:
    print(text)
    listener.stream.stop_stream()
    Command(text)
    time.sleep(1)
    listener.stream.start_stream()