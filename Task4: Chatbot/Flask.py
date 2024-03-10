#SYNC INTERN'S Task 4: AI ChatBot Using Google Gemini
#This  is a simple AI chatbot using Google Gemini API. It can understand and respond to user's queries about the weather, time, or any other topic
from flask import  Flask,render_template,jsonify,request
from agent import run_conversation
app= Flask(__name__)
@app.route("/process_message",methods =["POST"])
def process_message_func1():
    msg=request.json['message']
    print("WE ARE GETTING",msg)
    resp=run_conversation(msg)
    return jsonify({"response":resp})
    #return resp

@app.route("/")
def index():
    return render_template("index.html")
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
