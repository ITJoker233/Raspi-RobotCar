###########################################
#Writer: ITJoker                          #
#Time: 2018.6.03                          #
#Version:3.0                              #
#Trig=GPIO 2                              #
#Echo=GPIO 3                              #
###########################################
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from socket import *
import csb
import Read
import ip
import time
def t_init():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(11,GPIO.OUT)
        GPIO.setup(12,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        GPIO.setup(15,GPIO.OUT)
def chaoshenbo():
        csb.setup()
        a=csb.checkdist()
        GPIO.cleanup()
        conn.send(str(a))
def t_stop():
        GPIO.output(11, False)
        GPIO.output(12, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(3, False)
        GPIO.output(2, False)
        time.sleep(1)
        GPIO.cleanup()
def t_up():
        t_init()
        GPIO.output(11, True)
        GPIO.output(12, False)
        GPIO.output(13, True)
        GPIO.output(15, False)
        time.sleep(1)
        GPIO.cleanup()
        chaoshenbo()
def t_down():
        t_init()
        GPIO.output(11, False)
        GPIO.output(12, True)
        GPIO.output(13, False)
        GPIO.output(15, True)
        time.sleep(1)
        GPIO.cleanup()
        chaoshenbo()
def t_right():
        t_init()
        GPIO.output(11, False)
        GPIO.output(12, True)
        GPIO.output(13, True)
        GPIO.output(15, False)
        time.sleep(1)
        GPIO.cleanup()
        chaoshenbo()
def t_left():
        t_init()
        GPIO.output(11, True)
        GPIO.output(12, False)
        GPIO.output(13, False)
        GPIO.output(15, True)
        time.sleep(1)
        GPIO.cleanup()
        chaoshenbo()
#########################################################
def commands (cmd):
    print cmd
    if cmd == 'd':
      t_down()
    elif cmd == 's':
      t_stop()
    elif cmd == 'u':
      t_up()
    elif cmd == 'l':
      t_left()
    elif cmd == 'r':
      t_right()
HOST=ip.getip()#the PORT of raspberry pi port
PORT=Read.LoadData('/config.conf')#the HOST of raspberry pi ip
s= socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print ('listening on',PORT)
while 1:
    conn, addr = s.accept()
    print ('Connected ok! By ',addr)
    while 1:
            command= conn.recv(20).replace('\n','')
            if command == 'g':
              conn.close
              break
            elif not command:break
            commands(bytearray(command)) #command
    conn.close()
