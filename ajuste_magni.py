#Tarea de eleccion temporal y probabilistica
# -*- coding: utf-8 -*-
#registra bien la posicion
from psychopy import visual, core, event
import csv
import random
import time

global choices
global lolas
global lola

choices = []
lolas = []


myWindow = visual.Window(monitor="testMonitor", units="cm", fullscr=True) # Especificaciones de la pantalla principal llamada myWindow
myWindow.setColor([255,255,255], colorSpace="rgb255") # Color de fondo de pantalla
myWindow.update() # Actualizacion de la ventana
myMouse = event.Mouse(myWindow) # Registra un evento de raton dentro de myWindow

tamano_letra = 1.2 #Tamano letra de opciones
col_alter=(120,120,120) #color de opciones 

def click(): # Funcion que detecta el click en la pantalla
	keys = event.getKeys()
	for k in keys:
		if k == "escape":
			core.quit()
	myMouse=event.Mouse(win=myWindow)	
	clickdetected = False
	while not clickdetected:
		buttons = myMouse.getPressed()
		if buttons [0] == 1:
			clickdetected = True

def instrucciones(): # Funcion que genera la primera pantalla, 
	txt_instruc1 = visual.TextStim(myWindow,text="INSTRUCCIONES:", # esta son las especificaciones del texto
		height=1.5, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,5),alignHoriz='center')
	txt_instruc1_2 = visual.TextStim(myWindow,text=u"A continuación se te presentarán una serie de pares de alternativas de las cuales debes de elegir una de acuerdo a tu preferencia. Cada una de las alternativas es diferente en cantidad de dinero y tiempo de entrega, por ejemplo:",
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,0),alignHoriz='center',wrapWidth = 40)
	txt_instruc1_3 = visual.TextStim(myWindow,text=u"Da click para empezar",
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,-5),alignHoriz='center',wrapWidth = 40)
	txt_instruc1.draw() # draw es lo que dibuja ese texto y hay tres draw porque hiciste tres variables de texto
	txt_instruc1_2.draw()
	txt_instruc1_3.draw()
	myWindow.update() # todas estos textos se mostraron en una pantalla al mismo tiempo
	click()

##### Alternatives
magnitude_adjusted = 2000
time_fixed_small = 2
magnitude_fixed_large = 4000
time_fixed_large = 4


#Grupo short delays
small_reward = visual.TextStim(myWindow,text= str(magnitude_adjusted) +' pesos en '+ str(time_fixed_small) + ' semana',
		height=tamano_letra, 
		color=col_alter,colorSpace='rgb255')
large_reward = visual.TextStim(myWindow,text= str(magnitude_fixed_large) +' pesos en '+ str(time_fixed_large) + ' semanas',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")




def seleccionletra(cual_a,cual_b):
	global choices
	txt_pregunta = visual.TextStim(myWindow,text=u'¿Cuál alternativa prefieres?', #texto permanente
		height=1, 
		color=col_alter, colorSpace="rgb255",
		pos=(0,8))
	txt_o = visual.TextStim(myWindow,text=u'ó',
		height=1, 
		color=col_alter, colorSpace="rgb255",
		pos=(0,1))	

	eleccion = visual.RatingScale(myWindow, choices=['A','B'], 
		marker='hover', size=2, stretch=0.8) 
	#RatingScale el que A y B a seleccionar, minTime= restriccion temporal 
# lo que genera la letra a y b

	cual_a.pos= (-12,1)
	cual_b.pos= (12,1) # posicion de las variables que se pondran en cual a y cual b

	while eleccion.noResponse: 	#si no registra respuesta dibujar texto y eleccion
		txt_pregunta.draw() 
		txt_o.draw()
		cual_a.draw()
		cual_b.draw()
		eleccion.draw()
		myWindow.flip()

	choices.append(eleccion.getRating())


def ajuste(ajustada,fija):
	global choices
	txt_pregunta = visual.TextStim(myWindow,text=u'¿Cuál alternativa prefieres?', #texto permanente
		height=1, 
		color=col_alter, colorSpace="rgb255",
		pos=(0,8))
	txt_o = visual.TextStim(myWindow,text=u'ó',
		height=1, 
		color=col_alter, colorSpace="rgb255",
		pos=(0,1))	

	eleccion = visual.RatingScale(myWindow, choices=['A','B'], 
		marker='hover', size=2, stretch=0.8) 
	global lola
	if choices[-1] == 'A': #choices[-1] get last list item 
		lola = ajustada- ((magnitude_fixed_large - ajustada)/2)

		small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(time_fixed_small) + ' semana',
		height=tamano_letra, 
		color=col_alter,colorSpace='rgb255')

		small_reward_ad.pos= (-12,1) # posicion de las variables que se pondran en cual a y cual b
		fija.pos= (12,1)

		while eleccion.noResponse:
			txt_pregunta.draw()
			txt_o.draw()
			small_reward_ad.draw()
			fija.draw()
			eleccion.draw()
			myWindow.flip()
	else:
		lola = ajustada + ((magnitude_fixed_large - ajustada)/2)

		small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(time_fixed_small) + ' semana',
		height=tamano_letra, 
		color=col_alter,colorSpace='rgb255')

		small_reward_ad.pos= (-12,1) # posicion de las variables que se pondran en cual a y cual b
		fija.pos= (12,1)

		while eleccion.noResponse:
			txt_pregunta.draw()
			txt_o.draw()
			small_reward_ad.draw()
			fija.draw()
			eleccion.draw()
			myWindow.flip()
			
    	lolas.append(lola)
	choices.append(eleccion.getRating())




#######################################Comienzo experimento
####################### Aqui pones todas las funciones y los ciclos asi como quieres que sucedan
instrucciones()
myWindow.update()
seleccionletra(small_reward,large_reward)
myWindow.update()
ajuste(magnitude_adjusted,large_reward)

for i in range(7):
	myWindow.update()
	ajuste(lola,large_reward)


print " --- "
print "Update list"
print lolas
print choices


# for i in range(3): #ciclo que permite que se repitan los ensayos con diferentes valores
# 	myMouse=event.Mouse(win=myWindow,newPos=(0,-3))	






