import pyttsx3

class Speaker:
    def __init__(self):
        
        self.engine = pyttsx3.init('sapi5')
        
        
        
    def speak(self, audio):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices', voices[1].id)
        self.engine.say(audio)
        self.engine.runAndWait()        
    
