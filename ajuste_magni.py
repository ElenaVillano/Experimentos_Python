#Tarea de eleccion temporal y probabilistica
# -*- coding: utf-8 -*-
#registra bien la posicion
from psychopy import visual, core, event
import csv
import random
import time

global choices
choices = []

que1 =[2000]
que2 =[2000]
que3 =[2000]
que4 =[2000]
que5 =[2000]
que6 =[2000]
que7 =[2000]
que8 =[2000]
que9 =[2000]
que10=[2000]
que11=[2000]
que12=[2000]
que13=[2000]
que14=[2000]
que15=[2000]
que16=[2000]
que17=[200]
que18=[200]
que19=[200]
que20=[200]
que21=[200]
que22=[200]
que23=[200]
que24=[200]
que25=[200]
que26=[200]

allques =[que1,que2,que3,que4,que5,que6,que7,que8,que9,que10,que11,que12,que13,que14,que15,que16,que17,que18,que19,que20,que21,que22,que23,que24,que25,que26]


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

##### Preguntas        1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17  18  19  20  21  22  23  24  25  26
magnitude_adjusted    = [2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,200,200,200,200,200,200,200,200,200,200]
time_fixed_small      = [   2,   4,   6,   2,   4,   2,  14,  16,  18,  14,  16,  14,   8,   2,   8,   2,  2,  4,  6,  2, 14, 16, 18, 14, 8 ,  2]
magnitude_fixed_large = [4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,400,400,400,400,400,400,400,400,400,400]
time_fixed_large      = [   4,   6,   8,   6,   8,   8,  16,  18,  20,  18,  20,  20,  14,  14,  20,  20,  4,  6,  8,  8, 16, 18, 20, 20, 14, 20]






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


def ajuste(ajustada,ajuste2,fija,conjunto):
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
		lola = ajustada - abs((ajuste2 - ajustada)/2)

		small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(time_fixed_small[j]) + ' semanas',
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
		lola = ajustada + abs((ajuste2-ajustada)/2)

		small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(time_fixed_small[j]) + ' semanas',
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
    	conjunto.append(lola)
	choices.append(eleccion.getRating())




#######################################Comienzo experimento
####################### Aqui pones todas las funciones y los ciclos asi como quieres que sucedan
instrucciones()
myWindow.update()
for j in (range(len(magnitude_adjusted))):
	small_reward = visual.TextStim(myWindow,text= str(magnitude_adjusted[j]) +' pesos en '+ str(time_fixed_small[j]) + ' semanas',
		height=tamano_letra, 
		color=col_alter,colorSpace='rgb255')
	large_reward = visual.TextStim(myWindow,text= str(magnitude_fixed_large[j]) +' pesos en '+ str(time_fixed_large[j]) + ' semanas',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")

	seleccionletra(small_reward,large_reward)
	myWindow.update()
	ajuste(magnitude_adjusted[j],magnitude_fixed_large[j],large_reward,allques[j])
	myWindow.update()
	ajuste(lola,magnitude_adjusted[j],large_reward,allques[j])


	for i in range(4):
		myWindow.update()
		ajuste(lola,allques[j][1+i],large_reward,allques[j])

	conjunto = visual.TextStim(myWindow,text= 'siguiente conjunto',
	height=tamano_letra,color=col_alter,colorSpace='rgb255')
	conjunto.draw()
	myWindow.update()
	click()

cantidades=que1+que2+que3+que4+que5+que6+que7+que8+que9+que10+que11+que12+que13+que14+que15+que16+que17+que18+que19+que20+que21+que22+que23+que24+que25+que26


print " --- "
print "Update list"
print cantidades
print choices

ensayos=range(len(cantidades))


salvadatos=('sujeto_adju_tiempo.csv')
with open(salvadatos,'wb') as csvfile:
	ensayo=csv.writer(csvfile,delimiter=',')
	ensayo.writerow(['trial','smaller_money','choices'])
	for i in range(len(cantidades)):
		ensayo.writerow([ensayos[i]+1,
			cantidades[i],
			choices[i]])


