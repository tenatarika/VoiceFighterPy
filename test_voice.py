from voice_Iissener import VoiceLissener
from voice_speaker import  Speaker



def main():
    
    lissener = VoiceLissener()
    speaker = Speaker()
    
    speaker.speak("Can  you say YES?")
    take = lissener.takeCommands()
    choice = take
    if "да" in choice:
        speaker.speak("Списибо большое за внимание!")
        for i in range(9, 0, -1):
            speaker.speak(i)

    if "нет" in choice:
        speaker.speak("жаль")
        
        
    

if __name__ == '__main__':
    main()
    