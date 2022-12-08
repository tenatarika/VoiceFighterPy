from voice_Iissener import VoiceLissener
from voice_speaker import  Speaker



def dialog():
    
    lissener = VoiceLissener()
    speaker = Speaker()
    
    speaker.speak("Можете сказать да?")
    take = lissener.takeCommands()
    choice = take
    if "да" in choice:
        speaker.speak("Списибо большое за внимание!")
        for i in range(9, 0, -1):
            speaker.speak(i)

    if "нет" in choice:
        speaker.speak("жаль")


def get_voice_by_text(text: str):
    speaker = Speaker()
    speaker.speak(text)


def get_text_by_voice():
    lissener = VoiceLissener()
    take = lissener.takeCommands()
    print(take)


if __name__ == '__main__':

    while True:
        print("1 - run dialog")
        print("2 - get voice by text")
        print("3 - get text by voice")
        print("4 - exit")
        option = int(input('Enter your choice: '))

        if option == 1:
            dialog()
        elif option == 2:
            get_voice_by_text(str(input('Enter your text: ')))
        elif option == 3:
            get_text_by_voice()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
