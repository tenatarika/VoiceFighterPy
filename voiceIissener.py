import speech_recognition as sr 

class VoiceLissener:
    """Слушает комманды"""
    def __init__(self, query):
        self.query = query
        
    def takeCommand(self):
        """Слушает голос"""
        
        recorder = sr.Recognizer()
        with sr.Microphone() as source:
            
            recorder.pause_threshold = 0.75
            
            audio = recorder.listen(source)
            
            try:
                print('recording')
                
                Query = recorder.recognize_google(audio, language="en-US")
                        
            except Exception as e:
                print(e)
                return "None"
            
            
        return Query
            
        
        