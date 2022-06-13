from playsound import playsound
from threading import Thread
p="test.wav"


ALARM_ON = False

def sound_alarm(p):
	# play an alarm sound
    playsound(p)

t = Thread(target=sound_alarm(p))
t.deamon = True
t.start()