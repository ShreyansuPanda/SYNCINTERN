import temp_city
from config import key
import requests
import wikipedia

def parse_function_response(message):
    function_call= message[0].get("functionCall")
    function_name= function_call["name"]
    print("Gemini: call function",function_name)
    try:
        arguments=function_call.get("args")
        print("Gemini arguments are  ",arguments)
        if arguments:
            d=getattr(temp_city,function_name)
            print("function is:",d)
            function_respose=d(**arguments)
            
        else:
            function_respose= "No Arguments"
            
    except Exception as e:
        print(e)
        function_respose= "Invalid Function"
    return function_respose
        
    
def run_conversation(user_message):
    messages=[]
    system_message="You are an AI bot, named Phoenix that can do everything using function call.When you are asked to do something, use the function call you have available and then respond with message."
    message={"role":"user","parts" : [{"text": system_message+" "+user_message}]}
    
    messages.append(message)
    
    data={"contents":[messages],"tools":[{"functionDeclarations": temp_city.defintion}]} 
    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response=requests.post(url,json=data)
    
    if response.status_code !=200:
        print(response.text)
        
    t1=response.json()
    if "content" not in t1.get("candidates")[0]:
        print("Error: No Content")
    message=t1.get("candidates")[0].get("content").get("parts")
    print("Message:",message)
    
    if "functionCall" in message[0]:
        res1=parse_function_response(message)
        res1=f'<div class="ai-response">{res1}</div>'
        print("Actual Response:",res1)
        return res1
    else:
        print("No  Function Call Found")
    
    #print("NOW:",t1)
if __name__=="__main__":
    user_message ="find IP address of google.com" 
    print(run_conversation(user_message))