
#! / usr / bin / env python3
# PyAudio ve PySpeech gerektirir.

import speech_recognition as konus
from os import system as komut

buyukAlfabe = "ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe ="abcçdefgğhiıjklmnoöprsştuüvyz"

def lower(text:str):
    neWText = str()
    for i in text:
        if i in buyukAlfabe:
            index = buyukAlfabe.index(i)
            neWText += kucukAlfabe[index]
        else:
            neWText += i


    return  neWText

# Record Audio
r = konus.Recognizer()
with konus.Microphone() as source:
    komut("clear") #Ekranı Temizledik.
    print("Hadi Bir Şeyler Söyle ;")
    audio = r.listen(source,timeout=2, phrase_time_limit=2)


Flag = False

try:
    text = r.recognize_google(audio,language="tr-TR")
    print("Algıladığım :" + text)
    Flag = True
    text = lower(text)
except konus.UnknownValueError:
    print("Hocam Valla Ne Dediğini Anlayamadım ?")
except konus.RequestError as e:
    print("Şuan Google ile aramda sıkıntı var hocam inan sana yardımcı olamıyorum; {0}".format(e))

if Flag:
    if text == "atomu çalıştır":
        komut("atom")
elif Flag:
    if text =="internete bağlan":
        komut("opera-developer")
elif Flag:
    if text =="telegramı aç":
        komut("telegram-desktop")
