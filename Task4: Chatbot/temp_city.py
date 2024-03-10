
from config import key
import requests
import socket
def get_ip(host):
    try:
        # Get the first IP address from the list returned by getaddrinfo
        addr_info = socket.getaddrinfo(host, None)
        ip_address = addr_info[0][4][0]
        return ip_address
    except Exception as e:
        print(e)
        return f"Error in finding IP: {e}"

def Talk_with_ai(chat):
    messages=[]
    system_message=f"You are an AI Assitant, your name is Phoenix.Find the content related to query:"
    message={"role":"user","parts" : [{"text ": system_message+"  "+chat}]}
    messages.append(message)
    data={"contents":messages}
    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response=requests.post(url,json=data)
    
    t1=response.json()
    #hprint(t1)
    t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2) 
    return t2


def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":city,"format":"json","u":"f"}

    headers = {
        "X-RapidAPI-Key": "4a80611551msh297e8330f96f861p18bbcfjsn366ba902f16d",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    d1=response.json()
    loc=d1.get("location").get("city")
    d1=d1.get("current_observation")
    hum=d1.get("atmosphere").get("humidity")
    temp=d1.get("condition").get("temperature")
    temp=round((temp-32)*5/9,2)
    return (f"City: {loc},\nHumidity:{hum},\nTemperature in Celcius:{temp}")


defintion=[{
    "name":"Talk_with_ai",
    "description":"Hi Hello",
    "parameters":{
        "type":"object",
        "properties":{
            "chat":{
                "type":"String",
                "description":"full query asked by user"
            }
        }
    }
},
    {
    "name":"temp_city",
    "description":"Find temperature,weather of the city",
    "parameters":{
        "type":"object",
        "properties":{
            "city":{
                "type":"String",
                "description":"City to find teamperature"
            }
        }
    }
},
{
    "name": "get_ip",
    "description": "Find IP address of a given host",
    "parameters": {
        "type": "object",
        "properties": {
            "host": {
                "type": "string",
                "description": "Host to find IP address"
            }
        }
    }
}]



if __name__=="__main__":
    print(temp_city(city))