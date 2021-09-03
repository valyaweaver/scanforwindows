from serial import *
import time
from datetime import datetime
from time import sleep
import os
import winsound

port0 = "COM10"

serialPort0 = Serial(port=port0, baudrate=9600, bytesize=8, timeout=2)

serialString = ""
usersfile = open("Z:/SMT/scandata/users.txt")
user = usersfile.readline()
open0 = 0

userid0 = 'user:none'

while 1:
    if serialPort0.in_waiting > 0:
        serialString = serialPort0.readline()
        open0 = str(serialString.decode("Ascii"))
        if (open0[0:9] in user):
            userid0 = open0[0:9]
        cur = datetime.now()
        tistamp = str(cur)
        qrdata0 = open0[0:17]
        if userid0 == 'user:none':
            # os.system("start C:/Users/hp/TF002.wav")
            # winsound.Beep(1111, 2000)
            winsound.PlaySound("TF002.wav", winsound.SND_FILENAME)
        print(qrdata0 + ' ' + userid0 + ' ' + tistamp)
        f0 = open("Z:/SMT/scandata/cut.txt", 'a')
        f0.write(str(qrdata0 + ' ' + userid0 + ' ' + tistamp + '\n'))
        f0.close()



