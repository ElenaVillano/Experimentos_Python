from psychopy import visual, core

myWindow = visual.Window(monitor="testMonitor", units = "cm")
myWindow.setColor([0,0,0], colorSpace="rgb255")
myWindow.update()
txt1 = visual.TextStim(win=myWindow, text="Hello World", height=4, color = (255, 255, 255), colorSpace='rgb255')
img1 = visual.ImageStim(myWindow, image="mundo.jpg")
txt1.draw()
img1.draw()
myWindow.update()
core.wait(3.14)