from voice import voice
import handlers


COMMANDS = [
    {'id': 0, 'text': 'joke', 'handler': handlers.create},  #creates new joke
    {'id': 1, 'text': 'single', 'handler': handlers.single_joke},   #creates single-type joke
    {'id': 2, 'text': 'punchline', 'handler': handlers.twopart_joke},   #creates twopart-type joke
    {'id': 3, 'text': 'book', 'handler': handlers.write_down},  #writes joke to a file
    {'id': 3, 'text': 'flush', 'handler': handlers.clear}   #clears joke_list.txt file
] 

ACTIVATION = 'michael'


class Command:

    def __init__(self, text):
        self.text = text
        self.map()
        
    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION, '').strip()
            for cmd in COMMANDS:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech('I dont know this command sorry!')
           
            

    def run(self, cmd):
        handler = cmd['handler']
        text = self.text.replace(cmd['text'], '').strip()
        handler(text)
        