from config import key
import requests
from mic_text import mic1
import temp_city

def Talk_with_ai(chat):
    messages=[]
    system_message="You are an AI Assitant, your name is Phoenix."
    message={"role":"user","parts" : [{"text": system_message+" "+chat}]}
    messages.append(message)
    data={"contents":messages}
    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response=requests.post(url,json=data)
    
    t1=response.json()
    #hprint(t1)
    t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2) 

a=input("Do you wish to type or speak?")
if a=="speak":
    print("Pls Speak your question:\n")
    chat= mic1()
else:
    chat=input("How can i help you today?\n")
Talk_with_ai(chat)