from voice import voice
import handlers


COMMANDS = [
    {'id': 0, 'text': 'joke', 'handler': handlers.create}
    # {'id': 1, 'text': 'хватит', 'handler': handlers.stop},
    # {'id': 2, 'text': 'thank you', 'handler': handlers.thanks}
] 

ACTIVATION = 'travis'


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
        