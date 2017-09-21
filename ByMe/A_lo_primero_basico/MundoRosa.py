from psychopy import visual, core, event

myWindow = visual.Window(monitor="testMonitor",
 units="cm", fullscr=True) 
#para elegir monitor, pixeles o cms, pantalla completa
myWindow.setColor([0,0,0], colorSpace='rgb255')
myWindow.update() #actualizas la ventana con el color

myMouse=event.Mouse(win=myWindow)

txt=visual.TextStim(myWindow,text='Hola, da click para ver mundos', height=2, 
color=(255,0,77), colorSpace='rgb255') #para poner texto 
txt.pos=(0,0) #para cambiar posicion .pos
txt.draw() #dibuja tu variable 
myWindow.update()

clickdetected=False 
while not clickdetected:
	buttons= myMouse.getPressed()
	if buttons [0] == 1:
		clickdetected=True
	keys=event.getKeys()
	for k in keys: 
		if k == 'escape':
			clickdetected=True 
            
myMouse=event.Mouse(win=myWindow)
txt1=visual.TextStim(myWindow,text='Click para el siguiente mundo...', height=2, 
color=(255,0,77), colorSpace='rgb255') #para poner texto 
txt1.pos=(-10,3) #para cambiar posicion .pos
txt1.draw() #dibuja tu variable 
img1=visual.ImageStim(myWindow, image='mundorosa.png')
img1.pos=(0,-5)
img1.draw()
myWindow.update() 

clickdetected=False 
while not clickdetected:
	buttons= myMouse.getPressed()
	if buttons [0] == 1:
		clickdetected=True
	keys=event.getKeys()
	for k in keys: 
		if k == 'escape':
			clickdetected=True 

myWindow.update()
myMouse=event.Mouse(win=myWindow)
myWindow.setColor([0,0,0], colorSpace='rgb255')
txt2=visual.TextStim(myWindow,text='Click para el ultimo mundo...', height=2, 
color=(255,0,77), colorSpace='rgb255') #para poner texto 
txt2.pos=(-3,10) #para cambiar posicion .pos
txt2.draw()
img2=visual.ImageStim(myWindow, image='mundorosa.png')
img2.pos=(10,-3)
img2.draw()
myWindow.update() 

clickdetected=False 
while not clickdetected:
	buttons= myMouse.getPressed()
	if buttons [0] == 1:
		clickdetected=True
	keys=event.getKeys()
	for k in keys: 
		if k == 'escape':
			clickdetected=True 

myWindow.update()
myMouse=event.Mouse(win=myWindow)
myWindow.setColor([0,0,0], colorSpace='rgb255')
txt3=visual.TextStim(myWindow,text='ADIOS', height=2, 
color=(255,0,77), colorSpace='rgb255') #para poner texto 
txt3.pos=(10,3) #para cambiar posicion .pos
txt3.draw()
img3=visual.ImageStim(myWindow, image='mundorosa.png')
img3.pos=(-10,-3)
img3.draw()
myWindow.update() 

clickdetected=False 
while not clickdetected:
	buttons= myMouse.getPressed()
	if buttons [0] == 1:
		clickdetected=True
	keys=event.getKeys()
	for k in keys: 
		if k == 'escape':
			clickdetected=True 
		

#mientras no detecte click 
#core.wait(3)#dura tres segundos
