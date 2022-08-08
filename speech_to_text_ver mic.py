#import library
#Google Web Speech API
import speech_recognition as sr
import pyaudio
# ไมค์
sr.Microphone.list_microphone_names()
mic = sr.Microphone(1)
#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
r = sr.Recognizer()
# ฟังเสียงที่ได้รับจาก mic และนำไปเก็บที่ audio_text
with mic as source:
    audio_text = r.listen(source)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        # language สามารถเลือกภาษาได้
        # https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134
        text = r.recognize_google(audio_text, language="th")
        print('Converting audio transcripts into text ...')
        print(text)
    except:
         print('Sorry.. run again...')