from gtts import gTTS
import os
import playsound



def talk(text,lang='en',tld='co.in'):
    text=gTTS(text=text, lang=lang,tld=tld)
    text.save('file.mp3')
    playsound.playsound('file.mp3')
    os.remove('file.mp3')

