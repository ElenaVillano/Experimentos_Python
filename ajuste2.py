#Tarea de eleccion temporal y probabilistica
# -*- coding: utf-8 -*-
#registra bien la posicion

"""
Esta tarea fue desarrollada por Elena Villalobos en Octubre 2017.
Es una tarea de ajuste a la magnitud a 7 elecciones.
La recompensa pequena se ajusta de acuerdo a las elecciones del sujeto, 
mientras que los otros atributos se quedan fijos. 
Si elige la grande demorada, la recompensa pequena se hace mas atractiva. 
Si elige la pequena inmediata, la recompensa pequena se hace menos atractiva.
""" 

from psychopy import visual, core, event
import csv
import random
import time

"""Especificaciones generales de la pantalla"""

myWindow = visual.Window(monitor="testMonitor", units="cm", fullscr=True)  # Especificaciones de la pantalla principal llamada myWindow
myWindow.setColor([255,255,255], colorSpace="rgb255")                      # Color de fondo de pantalla
myWindow.update()                                                          # Actualizacion de la ventana
myMouse = event.Mouse(myWindow)                                            # Registra un evento del raton dentro de la pantalla (myWindow)

"""Especificaciones generales de variables 
que se utilizaran a lo largo  del experimento"""

global choices                                                             # Se hace global la variable de choices, donde se colocaran las elecciones de los sujetos
choices = []                                                               # Lista vacia de choices
tamano_letra = 1.2                                                         # Tamano letra de opciones
col_alter=(120,120,120)                                                    # Color de letra
yes = []                                                                   # Lista a llenar

"""Especificaciones de las preguntas con las que comienzas cada conjunto."""

# Listas con solo un primer valor
set1=[[ 200],( 200, 400, 3, 9)]
set2=[[ 200],( 200, 400,12,36)]
set3=[[ 200],( 200, 400,23,29)]
set4=[[2000],(2000,4000, 3, 9)]
set5=[[2000],(2000,4000,12,36)]
set6=[[2000],(2000,4000,23,29)]

# Todas las listas en una sola lista
Sets = [set1,set2,set3,set4,set5,set6]
# Las hacemos random
allSets = random.sample(Sets,len(Sets))


# Espericiaciones de cada pregunta a ajustar
#                        set1,set2,set3,set4,set5,set6



"""Funciones que se utilizaran en el experimento"""

def click():                                             # Funcion que detecta un click en la pantalla
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


def instrucciones():                                     # Funcion que genera las instrucciones del experimento
	# Primera pantalla (primeras instrucciones)
	txt_instruc1 = visual.TextStim(myWindow,text="INSTRUCCIONES:",
		height=1.5, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,5),alignHoriz='center')
	txt_instruc1_2 = visual.TextStim(myWindow,text=u"A continuación se te presentarán una serie de pares de alternativas de las cuales debes de elegir una de acuerdo a tu preferencia. \n \nCada una de las alternativas indica una cantidad monetaria que recibirías ante cierta demora, por ejemplo:",
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,0),alignHoriz='center',wrapWidth = 40)
	txt_instruc1_3 = visual.TextStim(myWindow,text=u"Da click en la pantalla para ver el ejemplo...",
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,-5),alignHoriz='center',wrapWidth = 40)
	txt_instruc1.draw()
	txt_instruc1_2.draw()
	txt_instruc1_3.draw()
	myWindow.update()
	click()

	# Segunda pantalla (ejemplo) 
	eleccion = visual.RatingScale(myWindow, choices=['A','B'], 
	marker='hover', size=1.2, stretch=0.5, pos=(0,0.06))
	txt_instruc2 = visual.TextStim(myWindow,text=u"¿Cuál alternativa prefieres?",
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,6),alignHoriz='center',wrapWidth = 40)
	txt_instruc2_1 = visual.TextStim(myWindow,text=u"300 pesos en 5 semanas ó 400 pesos en 6 semanas",
		height=1, 
		color=col_alter, colorSpace="rgb255",  italic=True,
		pos=(0,4),alignHoriz='center',wrapWidth = 40)
	txt_instruc2_2 = visual.TextStim(myWindow,text=u'Si eliges la letra A implica que recibirías 300 pesos dentro 5 semanas contando desde ahora, si eliges la letra B recibirías 400 pesos dentro de 6 semanas, contando desde ahora.',
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,-5),alignHoriz='center',wrapWidth = 40)	
	txt_instruc2_3 = visual.TextStim(myWindow,text=u'Da click en la pantalla para ver cómo elegir entre las alternativas...',
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,-8),alignHoriz='center',wrapWidth = 40)	
	txt_instruc2.draw()
	txt_instruc2_1.draw()
	txt_instruc2_2.draw()
	txt_instruc2_3.draw()
	eleccion.draw()
	myWindow.update()
	click()

	# Tercera pantalla (como elegir entre las alternativas)
	imgnar=visual.ImageStim(myWindow, image='letras.png',pos=(0,-4))
	txt_instruc3 = visual.TextStim(myWindow,text=u"¿Cuál alternativa prefieres?",
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,2),alignHoriz='center',wrapWidth = 40)
	txt_instruc3_1 = visual.TextStim(myWindow,text=u"300 pesos en 5 semanas                           ó                        400 pesos en 6 semanas",
		height=1, 
		color=col_alter, colorSpace="rgb255",  italic=True,
		pos=(0,-1),alignHoriz='center',wrapWidth = 40)
	txt_instruc3_2 = visual.TextStim(myWindow,text=u'Para elegir entre las alternativas debes de dirigir el cursor del mouse hacia la letra de tu preferencia la letra cambiará a color naranja (como se muestra más abajo en la pantalla). Una vez que el cursor esté dentro de la letra debes de dar click para elegir la alternativa que prefieras.',
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,9),alignHoriz='center',wrapWidth = 40)	
	txt_instruc3_3 = visual.TextStim(myWindow,text=u'Da click en la pantalla para seguir con las instrucciones...',
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,-10),alignHoriz='center',wrapWidth = 40)	
	imgnar.draw()
	txt_instruc3.draw()
	txt_instruc3_1.draw()
	txt_instruc3_2.draw()
	txt_instruc3_3.draw()
	myWindow.update()
	click()

	# Cuarta pantalla (retroalimentacion)
	txt_instruc6 = visual.TextStim(myWindow,text=u"Después de que hayas elegido tu alternativa dando click en la letra, la pantalla te mostrará cuál fue la alternativa que elegiste. Para continuar con la siguiente pregunta tendrás que dar click en el centro de la pantalla. \n \nEn esta siguiente pregunta se te presentará otro par de alternativas que pueden contener diferentes cantidades de dinero y/o demoras, y deberás elegir de entre ellas de nuevo.",
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,5),alignHoriz='center',wrapWidth = 40)
	txt_instruc6_2 = visual.TextStim(myWindow,text=u"Toma en cuenta dos cosas: \n \n1. El dinero de la alternativa menos demorada siempre cambia de pregunta a pregunta.\n \n2. Cada cierto número de preguntas el dinero de la alternativa más demorada, así como las demoras de ambas alternativas serán diferentes, estos cambios se indicarán con la leyenda: Da click para continuar con el siguiente conjunto. ",
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,-3),alignHoriz='center',wrapWidth = 40)
	txt_instruc6.draw()
	txt_instruc6_2.draw()
	myWindow.update()
	click()

	# Quinta pantalla (listos para comenzar)
	txt_instruc7 = visual.TextStim(myWindow,text=u"Este experimento tiene como finalidad investigar la manera en que la gente toma decisiones por lo tanto no existen respuestas correctas o incorrectas, solo estamos interesados en cuál opción eligirías tu.",
		height=1.1, 
		color=col_alter, colorSpace="rgb255", bold=True,
		pos=(0,5),alignHoriz='center',wrapWidth = 40)
	txt_instruc7_1 = visual.TextStim(myWindow,text=u"Cada una de las preguntas es importante, ELIGE CUIDADOSAMENTE.",
		height=1.1, 
		color=col_alter, colorSpace="rgb255", bold=True,
		pos=(0,1),alignHoriz='center',wrapWidth = 40)
	txt_instruc8 = visual.TextStim(myWindow,text=u"Sí estás listo, da click para comenzar con el experimento...",
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,-4),alignHoriz='center',wrapWidth=40)
	txt_instruc7.draw()
	txt_instruc7_1.draw()
	txt_instruc8.draw()
	myWindow.update()
	click()


def seleccionletra(cual_a,cual_b):                       # Funcion que regista la primera eleccion de cada pregunta fija

	# Eleccion entre A o B
	global choices
	txt_pregunta = visual.TextStim(myWindow,text=u'¿Cuál alternativa prefieres?', # Texto permanente
		height=1, 
		color=col_alter, colorSpace="rgb255",
		pos=(0,8))
	txt_o = visual.TextStim(myWindow,text=u'ó',
		height=1, 
		color=col_alter, colorSpace="rgb255",
		pos=(0,1))	

	eleccion = visual.RatingScale(myWindow, choices=['A','B'],       # Regista y genera A o B en variable eleccion 
		marker='hover', size=2, stretch=0.8)                         # minTime = restriccion temporal 

	global y                                                         # Genera 0 o 1 para acomodar posicion izquierda derecha
	y = random.randint(0,1)

	if y == 1:                                                       # Si 1 registra RSS en izquierda y RLL en derecha                                                       
		cual_a.pos = (-12,1)                                             
		cual_b.pos = (12,1)
	else:                                                            # Si 0 registra RLL en izquierda y RSS en derecha
		cual_b.pos = (-12,1)
		cual_a.pos = (12,1)


	while eleccion.noResponse:                                     	 # Si no registra respuesta dibuja texto y eleccion
		txt_pregunta.draw() 
		txt_o.draw()
		cual_a.draw()
		cual_b.draw()
		eleccion.draw()
		myWindow.flip()

	# Retroalimentacion
	elegiste_txt = visual.TextStim(myWindow,text=u'Elegiste:',       # Texto permanente 
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,5))
	sig_txt = visual.TextStim(myWindow,text=u'Da click aquí para la siguiente pregunta',
		height=0.8, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,-3))
	choice_trial = eleccion.getRating()                              # Registra la eleccion de este ensayo en choice_trial

	# Dependiente de la posicion, dibuja el texto de retroalimentacion 
	if y==1: # 1 RSS / RLL
		if choice_trial=='A':
			cual_a.pos=(0,2)
			cual_a.draw()
			elegiste_txt.draw()
			sig_txt.draw()
			myWindow.flip()
			click()
		else:
			cual_b.pos=(0,2)
			cual_b.draw()
			elegiste_txt.draw()
			sig_txt.draw()
			myWindow.flip()
			click()

	else: # 0 = RLL / RSS
		if choice_trial=='A':
			cual_b.pos=(0,2)
			cual_b.draw()
			elegiste_txt.draw()
			sig_txt.draw()
			myWindow.flip()
			click()
		else:
			cual_a.pos=(0,2)
			cual_a.draw()
			elegiste_txt.draw()
			sig_txt.draw()
			myWindow.flip()
			click()
	
	choices.append(eleccion.getRating())                             # Variable que guarda todas las elecciones en choices



def ajuste(ajustada,ajuste2,fija,conjunto):                          # Funcion que hace el ajuste una vez que ya se eligio
	global choices
	global lola
	global y

	txt_pregunta = visual.TextStim(myWindow,text=u'¿Cuál alternativa prefieres?', # Texto permanente
		height=1, color=col_alter, 
		colorSpace="rgb255", pos=(0,8))
	txt_o = visual.TextStim(myWindow,text=u'ó',
		height=1, color=col_alter, 
		colorSpace="rgb255", pos=(0,1))	

	eleccion = visual.RatingScale(myWindow, choices=['A','B'], 
		marker='hover', size=2, stretch=0.8) 
	
	elegiste_txt = visual.TextStim(myWindow,text=u'Elegiste:',
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,5))
	sig_txt = visual.TextStim(myWindow,text=u'Da click aquí para la siguiente pregunta',
		height=0.8, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,-3))


	if y == 1: # 1 = RSS / RLL 
		if choices[-1] == 'A':                                       # ([-1] get last list item) Si choices en el ensayo anterior es igual a A entonces
			lola = ajustada - abs((ajuste2 - ajustada)/2)            # lola se ajusta ante el valor absoluto

			small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(allSets[j][1][2]) + ' semanas',
			height=tamano_letra, color=col_alter, colorSpace='rgb255')

			while eleccion.noResponse:
				small_reward_ad.pos = (-12,1)
				fija.pos=(12,1)
				txt_pregunta.draw()
				txt_o.draw()
				small_reward_ad.draw()
				fija.draw()
				eleccion.draw()
				myWindow.flip()

			choice_trial = eleccion.getRating()

			if choice_trial == 'A':                                  # Retro alimentacion 
				small_reward_ad.pos=(0,2)
				small_reward_ad.draw()
				elegiste_txt.draw()
				sig_txt.draw()
				myWindow.flip()
				click()
			else:
				fija.pos=(0,2)
				fija.draw()
				elegiste_txt.draw()
				sig_txt.draw()
				myWindow.flip()
				click()

		else:
			lola = ajustada + abs((ajuste2-ajustada)/2)              # De cualquier otra manera 

			small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(allSets[j][1][2]) + ' semanas',
			height=tamano_letra, color=col_alter, colorSpace='rgb255')

			while eleccion.noResponse:
				small_reward_ad.pos=(-12,1)
				fija.pos=(12,1)
				txt_pregunta.draw()
				txt_o.draw()
				small_reward_ad.draw()
				fija.draw()
				eleccion.draw()
				myWindow.flip()
				
			choice_trial = eleccion.getRating()

			if choice_trial == 'A':
				small_reward_ad.pos=(0,2)
				small_reward_ad.draw()
				elegiste_txt.draw()
				sig_txt.draw()
				myWindow.flip()
				click()
			else:
				fija.pos=(0,2)
				fija.draw()
				elegiste_txt.draw()
				sig_txt.draw()
				myWindow.flip()
				click()

	else: # 1 RLL / RSS
		if choices[-1] == 'A': 
			lola = ajustada + abs((ajuste2 - ajustada)/2)

			small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(allSets[j][1][2]) + ' semanas',
			height=tamano_letra, color=col_alter, colorSpace='rgb255')

			while eleccion.noResponse:
				small_reward_ad.pos = (12,1)
				fija.pos=(-12,1)
				txt_pregunta.draw()
				txt_o.draw()
				small_reward_ad.draw()
				fija.draw()
				eleccion.draw()
				myWindow.flip()

			choice_trial = eleccion.getRating()

			if choice_trial == 'A':
				fija.pos=(0,2)
				fija.draw()
				elegiste_txt.draw()
				sig_txt.draw()
				myWindow.flip()
				click()
			else:
				small_reward_ad.pos=(0,2)
				small_reward_ad.draw()
				elegiste_txt.draw()
				sig_txt.draw()
				myWindow.flip()
				click()

		else:
			lola = ajustada - abs((ajuste2-ajustada)/2)

			small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(allSets[j][1][2]) + ' semanas',
			height=tamano_letra, color=col_alter, colorSpace='rgb255')

			while eleccion.noResponse:
				small_reward_ad.pos=(12,1)
				fija.pos=(-12,1)
				txt_pregunta.draw()
				txt_o.draw()
				small_reward_ad.draw()
				fija.draw()
				eleccion.draw()
				myWindow.flip()
				
			choice_trial = eleccion.getRating()

			if choice_trial == 'A':
				fija.pos=(0,2)
				fija.draw()
				elegiste_txt.draw()
				sig_txt.draw()
				myWindow.flip()
				click()
			else:
				small_reward_ad.pos=(0,2)
				small_reward_ad.draw()
				elegiste_txt.draw()
				sig_txt.draw()
				myWindow.flip()
				click()



    	conjunto.append(lola)
	

	choices.append(eleccion.getRating())


"""Como se desarrollara el experimento
Aqui pones todas las funciones y ciclos como quieres que sucedan a lo largo del experimento"""

instrucciones()
myWindow.update()
for j in range(len(allSets)):
	small_reward = visual.TextStim(myWindow,text= str(allSets[j][1][0]) +' pesos en '+ str(allSets[j][1][2]) + ' semanas',
		height=tamano_letra, 
		color=col_alter,colorSpace='rgb255')
	large_reward = visual.TextStim(myWindow,text= str(allSets[j][1][1]) +' pesos en '+ str(allSets[j][1][3]) + ' semanas',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")

	seleccionletra(small_reward,large_reward)                                   # Primera eleccion entre A y B
	myWindow.update()
	ajuste(allSets[j][1][0],allSets[j][1][1],large_reward,allSets[j][0])        # Se hace el ajuste en funcion de la eleccion entre la cantidad grande y pequena
	myWindow.update()
	ajuste(lola,allSets[j][1][0],large_reward,allSets[j][0])                    # 


	for i in range(4):
		myWindow.update()
		ajuste(lola,allSets[j][0][1+i],large_reward,allSets[j][0]) 

	conjunto_txt = visual.TextStim(myWindow,text= 'Da click para continuar con el siguiente conjunto.',
	height=tamano_letra,color=col_alter,colorSpace='rgb255', italic=True,wrapWidth=40)
	conjunto_txt.draw()
	myWindow.update()
	click()

### se hacen todas las cantidades en una sola lista
cantidades_ajustadas=set1[0]+set2[0]+set3[0]+set4[0]+set5[0]+set6[0]


print " --- "
print "Update list"
print cantidades
print choices

ensayos=range(len(cantidades))

"""Registro de datos """
salvadatos=('sujeto_adju_tiempo.csv')
with open(salvadatos,'wb') as csvfile:
	ensayo=csv.writer(csvfile,delimiter=',')
	ensayo.writerow(['trial','money_left','choices'])
	for i in range(len(cantidades)):
		ensayo.writerow([ensayos[i]+1,
			cantidades_ajustadas[i],
			choices[i]])


