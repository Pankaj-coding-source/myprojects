#bithday wish
import pyttsx3
from datetime import date
engine=pyttsx3.init()
t=date.today()

t_str=t.strftime("%I:%M %p on %B %d ,%Y")
if(t.month == 12 and t.day ==7):
   engine.say("Happy birthday")
else:
   engine.say("go to work")
engine.runAndWait()