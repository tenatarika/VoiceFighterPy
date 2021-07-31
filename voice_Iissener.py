import speech_recognition as sr 

class VoiceLissener:
    """Слушает комманды"""
    
        
        
    def takeCommands(self):
        """Слушает голос"""
        
        recorder = sr.Recognizer()
        with sr.Microphone() as source:
            
            recorder.pause_threshold = 0.75
            recorder.adjust_for_ambient_noise(source)
            audio = recorder.listen(source)
            
            try:
                print('recording')
                
                Query = recorder.recognize_google(audio, language="en-US")
                        
            except Exception as e:
                print(e)
                return "None"
            
            
        return Query
            
        
        