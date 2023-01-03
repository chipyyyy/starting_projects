from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import time
from playsound import playsound

# Wecker

def setAlarm(alarmTime):

    invalid = True
    while invalid:
        try:
            alarmTime = [int(n) for n in alarmTime.split(':')]
        except: 
            print('Du musst eine Zeit eingeben! (hh:mm)')
        if  alarmTime[0] > 24 or alarmTime[0] < 0:
            invalid = True
        elif alarmTime[1] > 59 or alarmTime[1] < 0:
            invalid = True
        else: 
            invalid = False
    now = datetime.now()
    dt_string = now.strftime('%H:%M')
    time_now = [int(n) for n in dt_string.split(':')]
    seconds_hms = [3600, 60, 1]
    alarmTimeSeconds = sum(a*b for a,b in zip(seconds_hms, alarmTime))
    time_nowSeconds = sum(a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second]))
    secondsUntilAlarm = alarmTimeSeconds - time_nowSeconds 
    if secondsUntilAlarm < 0: 
        secondsUntilAlarm += 86400
    print(f'Wecker ist gestellt in {timedelta(seconds=secondsUntilAlarm)}min')
    time.sleep(secondsUntilAlarm)
    playsound('/Users/tomhartmann/Desktop/alarm_alarmclock.mp3')


#Funktion, die Zeit aus GUI Entry liest (.get)

def getAlarm():
    alarmTime = f'{hour.get()}:{minutes.get()}'
    setAlarm(alarmTime)

#GUI 

guiWindow = Tk()
guiWindow.title('Wecker') #Fügt Titel hizu
guiWindow.geometry('300x100')#Formatiert das Fenster
guiWindow.config(bg = '#3C4540')#Konfiguriert die Hintergrundfarbe
guiWindow.resizable(width = False, height = False)
guiWindow.columnconfigure((0,6), weight = 1)
guiWindow.rowconfigure((0,8), weight = 1)

addHour = Label(
    guiWindow, 
    text = 'hh',
    fg = 'white',
    bg = '#617168',
    font = ("Helevetica", 15, "bold"),
    )

addHour.grid(row = 4, column = 2)

addColon = Label(
    guiWindow, 
    text = ':',
    fg = 'white',
    bg = '#617168',
    font = ("Helevetica", 15, "bold"),
    )

addColon.grid(row = 3, column = 3)

hour = StringVar()
setAlarmHour = Entry(
    guiWindow,
    textvariable=hour,
    width = 5,
    font = ("Helevetica", 15, "bold"),
    justify = CENTER
    )

setAlarmHour.grid(row = 3, column = 2)

addMinutes = Label(
    guiWindow,
    text = 'mm',
    fg = 'white',
    bg = '#617168',
    font = ("Helevetica", 15, "bold"),
    )

addMinutes.grid(row = 4, column = 4)

minutes = StringVar()
setAlarmMinutes = Entry(
    guiWindow,
    textvariable=minutes,
    width = 5, 
    font = ("Helevetica", 15, "bold"), 
    justify=CENTER
    )

setAlarmMinutes.grid(row = 3, column = 4)

submit = Button(
    guiWindow,
    text='OK',
    fg = "black",  
    bg = "#82B74B",  
    width = 5,  
    command=getAlarm
    )

submit.grid(row = 4, column = 6)

guiWindow.mainloop() #Startet GUI








