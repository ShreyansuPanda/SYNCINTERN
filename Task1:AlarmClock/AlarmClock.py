from tkinter import Tk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk,Image
from time import sleep
from pygame import mixer
from datetime import datetime
import threading

#Window:
main=Tk()
main.title("Alarm Clock")
main.geometry('350x150')
main.config(bg='#ffffff')

#frames
frame_line=Frame(main,width=400,height=5,bg='#566FC6')
frame_line.grid(row=0,column=0)

frame_body=Frame(main,width=400,height=290,bg='#ffffff')
frame_body.grid(row=1,column=0)

#configure
img=Image.open('icon2.png')
img.resize((100,100))
img=ImageTk.PhotoImage(img)
app_img= Label(frame_body,height=100,image=img,bg='#ffffff')
app_img.place(x=10,y=10)
name=Label(frame_body,text="Alarm",height=1,font='IVY 18 bold',bg='#ffffff')
name.place(x=125,y=10)

hour=Label(frame_body,text="Hour",height=1,font='IVY 10 bold',bg='#ffffff')
hour.place(x=127,y=40)
c_hour=Combobox(frame_body,width=2,font='arial 15')
c_hour.place(x=130,y=58)
c_hour['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)

min=Label(frame_body,text="Minutes",height=1,font='IVY 10 bold',bg='#ffffff')
min.place(x=180,y=40)
c_min=Combobox(frame_body,width=2,font='arial 15')
c_min.place(x=180,y=58)
c_min['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12",
                 "13","14","15","16","17","18","19","20","21","22","23","24","25",
                 "26","27","28","29","30","31","32","33","34","35","36","37","38",
                 "39","40","41","42","43","44","45","46","47","48","49","50","51",
                 "52","53","54","55","56","57","58","59","60")
c_min.current(0)

sec=Label(frame_body,text="Seconds",height=1,font='IVY 10 bold',bg='#ffffff')
sec.place(x=227,y=40)
c_sec=Combobox(frame_body,width=2,font='arial 15')
c_sec.place(x=230,y=58)
c_sec['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12",
                 "13","14","15","16","17","18","19","20","21","22","23","24","25",
                 "26","27","28","29","30","31","32","33","34","35","36","37","38",
                 "39","40","41","42","43","44","45","46","47","48","49","50","51",
                 "52","53","54","55","56","57","58","59","60")
c_sec.current(0)

per=Label(frame_body,text="Period",height=1,font='IVY 10 bold',bg='#ffffff')
per.place(x=277,y=40)
c_per=Combobox(frame_body,width=3,font='arial 15')
c_per.place(x=280,y=58)
c_per['values']=("AM","PM")
c_per.current(0)

def activate_alarm():
    t = threading.Thread(target=alarm)
    t.start()
def deactivate_alarm():
    print("Deactivate alarm",selected.get())
    mixer.music.stop()
    
selected=IntVar()

rad1=Radiobutton(frame_body,font=("arial 10 bold"),value=1,text="Activate",bg="#ffffff",command=activate_alarm,variable=selected)
rad1.place(x=125,y=95)

#alarm function
def alarm():
    while(True):
        control=selected.get()
        print(control)
        alarm_hour=c_hour.get()
        alarm_min=c_min.get()
        alarm_sec=c_sec.get()
        alarm_per=c_per.get()
        alarm_per=str(alarm_per).upper()
        now=datetime.now()
        hour=now.strftime("%I")
        min=now.strftime("%M")
        sec=now.strftime("%S")
        per=now.strftime("%p")
        if control==1:
            if alarm_per==per:
                if alarm_hour==hour:
                    if alarm_min==min:
                        if alarm_sec==sec:
                            print("Take a Break!")
                            sound_alarm()
        sleep(1)
def sound_alarm():
    mixer.music.load('alarm.mp3')
    mixer.music.play()
    selected.set(0)
    rad2=Radiobutton(frame_body,font=("arial 10 bold"),value=2,text="Deactivate",bg="#ffffff",command=deactivate_alarm,variable=selected)
    rad2.place(x=200,y=95)
mixer.init()


main.mainloop()