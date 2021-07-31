from voice_Iissener import VoiceLissener
from voice_speaker import  Speaker



def main():
    
    lissener = VoiceLissener()
    speaker = Speaker()
    
    speaker.speak("Вы хотите разрушить мир?")
    take = lissener.takeCommands()
    
    choice = take
    if "yes" in choice:
        speaker.speak("Ваш мир будет разрушен через 10 секунд")
        for i in range(9, 0, -1):
            
            speaker.speak(i)
        
        
    if "no" in choice:
        speaker.speak("thanks")
        
    
    

if __name__ == '__main__':
    main()
    