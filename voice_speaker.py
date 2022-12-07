import pyttsx3

class Speaker:
    def __init__(self):
        
        self.engine = pyttsx3.init()
        


    def speak(self, audio):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices', voices[2].id)
        self.engine.say(audio)
        self.engine.runAndWait()        
    
