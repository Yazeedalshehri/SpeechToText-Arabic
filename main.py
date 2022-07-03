from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as src:
    print('Say something....')

    audio = r.listen(src)

    t = r.recognize_google(audio, language='ar-AR')
    print(t)
    f = open('text.txt', 'a', encoding='utf-8')
    f.writelines(t+'\n')
    f.close()
    obj = gTTS(text=t, lang='ar', slow=False)
    obj.save('text.mp3')
    playsound('text.mp3')
