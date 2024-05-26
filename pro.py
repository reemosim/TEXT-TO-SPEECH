import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3 
import os

root=Tk()
root.title("text to speech with N&N")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#305065")

engine=pyttsx3.init()

def speaknow():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voice')
    def setvoice():
        #start conditions
        if(gender=='Male'):
            voices = engine.getProperty('voices')#byR
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            voices = engine.getProperty('voices')#byR
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if (speed=="fast"):
            engine.setProperty('rate', 350)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
#------------------------------------------------------------------------
#download voice file to the device
def download():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voice')
    def setvoice():
        if(gender=='Male'):
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    if(text):
        if (speed=="fast"):
            engine.setProperty('rate', 350)
            setvoice()
        elif(speed=="Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

image_icon=PhotoImage(file="C:/Users/96650/Desktop/images/email.png")
root.iconphoto(False ,image_icon)
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="C:/Users/96650/Desktop/images/email.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)
Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)
text_area=Text(root,font="Roboter 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)
Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)
gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')
speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')
imageicon=PhotoImage(file="C:/Users/96650/Desktop/images/email.png")
btn=Button(root,text="Speak",compound=LEFT,image=imageicon,width=130,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)
imageicon2=PhotoImage(file="C:/Users/96650/Desktop/images/email.png")
save=Button(root,text="save",compound=LEFT,image=imageicon2,width=130,bg="#39c790",font="arial 14 bold", command=download)#command=download by reem
save.place(x=730,y=280)
root.mainloop()
