#clickear en cada opcion para pasar a la siguiente imagen 

from psychopy import visual, core, event

myWindow = visual.Window(monitor="testMonitor",
 units="cm", fullscr=True) 
#para elegir monitor, pixeles o cms, pantalla completa, visual.Window=clase
myWindow.setColor([0,0,0], colorSpace='rgb255')
#poner color de la pantalla
myWindow.update() 
#actualizas la ventana con el color
myMouse=event.Mouse(win=myWindow)
#creas una variable que registra un evento
txt1=visual.TextStim(myWindow,text='Click para el siguiente mundo...', height=2, 
 color=(255,117,5), colorSpace='rgb255')
#para poner texto en la ventaja
txt1.pos=(-10,3) 
#para cambiar posicion del texto .pos
txt1.draw() 
#dibuja tu variable en este caso texto
img1=visual.ImageStim(myWindow, image='images.png')
#poner imagen junto con texto y la imagen debe de estar en la misma carpeta
img1.pos=(0,-5)
#posicion de imagen
img1.draw()
#dibuja tu imagen
myWindow.update() 
#actualiza tu imagen y espera el evento
clickdetected=False 
#creas una variable que registrara el evento y es 
#falso pero se hara verdad si pasa el mientras
while not clickdetected: 
	buttons= myMouse.getPressed() #getpressed se asigna a buttons que te dice cual clickear
	if buttons [2] == 1: # 0,1,2 izq, centro, der
		clickdetected=True
	keys=event.getKeys() #getKeys regresa cual tecla fue seleccionada 
	for k in keys: # si la tecla en el evento es igual a escaque se sale de la pantalla
		if k == 'escape':
			clickdetected=True 


#y lo repites 2 veces mas para que salga en total tres veces un texto e imagen diferente

#2
myWindow.update() 
myMouse=event.Mouse(win=myWindow)
myWindow.setColor([0,0,0], colorSpace='rgb255')
txt2=visual.TextStim(myWindow,text='Click para el ultimo mundo...', height=2, 
color=(255,117,5), colorSpace='rgb255')  
txt2.pos=(0,3) 
txt2.draw()
img2=visual.ImageStim(myWindow, image='images.png')
img2.pos=(10,-3)
img2.draw()
myWindow.update() 
clickdetected=False 
while not clickdetected:
	buttons= myMouse.getPressed()
	if buttons [2] == 1:
		clickdetected=True
	keys=event.getKeys()
	for k in keys: 
		if k == 'escape':
			clickdetected=True 

#3
myWindow.update()
myMouse=event.Mouse(win=myWindow)
myWindow.setColor([0,0,0], colorSpace='rgb255')
txt3=visual.TextStim(myWindow,text='Click para ADIOS', height=2, 
color=(255,117,5), colorSpace='rgb255') #para poner texto 
txt3.pos=(10,3) #para cambiar posicion .pos
txt3.draw()
img3=visual.ImageStim(myWindow, image='images.png')
img3.pos=(-10,-3)
img3.draw()
myWindow.update() 

clickdetected=False 
while not clickdetected:
	buttons= myMouse.getPressed()
	if buttons [2] == 1:
		clickdetected=True
	keys=event.getKeys()
	for k in keys: 
		if k == 'escape':
			clickdetected=True 
		
