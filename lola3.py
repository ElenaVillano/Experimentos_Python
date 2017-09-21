#Tarea de eleccion temporal y probabilistica
# -*- coding: utf-8 -*-
#registra bien la posicion
from psychopy import core, visual, data, event
import csv
import random
import time

myWindow = visual.Window(monitor="testMonitor", units="cm", fullscr=False)
myWindow.setColor([255,255,255], colorSpace="rgb255")
myWindow.update()

def click():
    keys = event.getKeys()
    for k in keys:
        if k == "escape":
            core.quit()
    myMouse=event.Mouse()	
    clickdetected = False
    while not clickdetected:
        buttons = myMouse.getPressed()
        if buttons [0] == 1:
            clickdetected = True
