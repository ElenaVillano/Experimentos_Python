#Selecciona una de las tres puertas, una te da la pantalla verde y las otras la pantalla roja

from psychopy import visual, core, event

myWin=visual.Window(monitor='testMonitor', units='cm', fullscr=True) #ventana
myWin.setColor([0,0,0], colorSpace='rgb255') #color de ventana
myWin.update() #actualizas ventana
myMouse=event.Mouse(myWin) #registra un evento dentro de la ventana

def waitforclick(themouse): #defines una funcion para esperar por click (themouse)
	clickdetected= False 
	while not clickdetected:
		clickdetected= themouse.getPressed()[0]==1 #el evento del mouse 0,1,2
	return themouse.getPos() #toma la posicion de el mouse

def getSelectedDoor (themouse, theDoors): #define otra funcion para la posicion del mouse
	mousepos=waitforclick(themouse) #espera por la posicion de la eleccion 
	for i in range(len(theDoors)): 
		if theDoors[i].contains(mousepos):
			return i
	return -1

doors= list() #hace una lista de puertas de imagenes en diferente posicion 
doors.append(visual.ImageStim(myWin, image='puerta.png'))
doors[0].pos=(-10,0)
doors.append(visual.ImageStim(myWin, image='puerta.png'))
doors[1].pos=(0,0)
doors.append(visual.ImageStim(myWin, image='puerta.png'))
doors[2].pos=(10,0)

for img in doors: #para cada imagen en puertas, dibujala
    img.draw()
myWin.update() #actualiza la ventana

waitforclick(myMouse)
selectedDoor= getSelectedDoor(myMouse,doors) #para seleccionar cualquier puerta
if selectedDoor==1: #si selecciona la 1, en medio, es verde
	myWin.setColor([0,255,0], colorSpace='rgb255')
	myWin.update()
	myWin.setColor([0,255,0], colorSpace='rgb255')
else: #cualquier otro caso, rojo
	myWin.setColor([255,0,0], colorSpace='rgb255')
	myWin.update()
	myWin.setColor([0,255,0], colorSpace='rgb255')

myWin.update()
core.wait(2)

#lo que sigue ese que si clickea fuera de la puerta que siga al programa.
