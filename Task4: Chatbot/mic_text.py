import speech_recognition as sr
"""for index, name in enumerate(sr.Microphone.list_microphone_names()):
   print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))"""
   
recognizer=sr.Recognizer()
def mic1():
    with sr.Microphone(device_index=1) as source:
        print("Say:")
        recognizer.adjust_for_ambient_noise(source)
        
        audio=recognizer.listen(source)
        print("Recognizing..")
        text=recognizer.recognize_google(audio)
        print(text)
        return text
