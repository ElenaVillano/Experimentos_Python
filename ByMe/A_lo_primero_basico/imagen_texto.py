from psychopy import visual, core
#primero cargas tu ventana inicial, la cual depende de cuantas ventanas quieras
myWindow = visual.Window(monitor="testMonitor", units="cm", fullscr=True) 
#para elegir monitor pues puede haber varios, elegir pixeles o centimetros, pantalla completa
myWindow.setColor([0,0,0], colorSpace='rgb255')
#elige el color que quieras de escala rgb
myWindow.update() 
#actualizas la ventana con el color
txt1=visual.TextStim(myWindow,text='Hola mundo', height=2, color=(255,117,5), colorSpace='rgb255') 
#para poner texto en myWindow, el texto, el tamano y el color rgb
txt1.draw() 
#dibuja tu variable 
img1=visual.ImageStim(myWindow, image='mundo.png')
#para poner imagen junto con el texto
img1.draw()
#dibuja tu imagen
myWindow.update() 
#actualiza tu ventana 
core.wait(5)
#el tiempo que quieres que espere la imagen

