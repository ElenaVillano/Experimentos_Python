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


##### Preguntas            1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17  18  19  20  21  22  23  24  25  26
magnitude_adjusted    = [2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,2000,200,200,200,200,200,200,200,200,200,200]
time_fixed_small      = [   2,   4,   6,   2,   4,   2,  14,  16,  18,  14,  16,  14,   8,   2,   8,   2,  2,  4,  6,  2, 14, 16, 18, 14, 8 ,  2]
magnitude_fixed_large = [4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,400,400,400,400,400,400,400,400,400,400]
time_fixed_large      = [   4,   6,   8,   6,   8,   8,  16,  18,  20,  18,  20,  20,  14,  14,  20,  20,  4,  6,  8,  8, 16, 18, 20, 20, 14, 20]




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
	txt_instruc6 = visual.TextStim(myWindow,text=u"Después de que hayas elegido tu alternativa dando click en la letra, la pantalla te mostrará cuál fue la alternativa que elegiste. Para continuar con la siguiente pregunta tendrás que dar click en el centro de la pantalla. \n \n \nEn esta siguiente pregunta se te presentará otro par de alternativas que pueden contener diferentes cantidades de dinero y/o demoras, y deberás elegir de entre ellas de nuevo.",
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,5),alignHoriz='center',wrapWidth = 40)
	txt_instruc6_2 = visual.TextStim(myWindow,text=u"Toma en cuenta que el dinero de las demoras más cortas cambia de pregunta a pregunta mientras que el dinero de las demoras largas, así como las demoras de las dos alternativas, cambian cada cierto número de preguntas.",
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,-2),alignHoriz='center',wrapWidth = 40)
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
		marker='hover', size=2, stretch=0.8)                         # minTime= restriccion temporal 

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

			small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(time_fixed_small[j]) + ' semana',
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

			small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(time_fixed_small[j]) + ' semanas',
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
			lola = ajustada - abs((ajuste2 - ajustada)/2)

			small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(time_fixed_small[j]) + ' semana',
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
			lola = ajustada + abs((ajuste2-ajustada)/2)

			small_reward_ad = visual.TextStim(myWindow,text= str(lola) +' pesos en '+ str(time_fixed_small[j]) + ' semanas',
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
for j in (range(len(magnitude_adjusted))):
	small_reward = visual.TextStim(myWindow,text= str(magnitude_adjusted[j]) +' pesos en '+ str(time_fixed_small[j]) + ' semanas',
		height=tamano_letra, 
		color=col_alter,colorSpace='rgb255')
	large_reward = visual.TextStim(myWindow,text= str(magnitude_fixed_large[j]) +' pesos en '+ str(time_fixed_large[j]) + ' semanas',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")

	seleccionletra(small_reward,large_reward)
	myWindow.update()
	ajuste(magnitude_adjusted[j],magnitude_fixed_large[j],large_reward,allSets[j])
	myWindow.update()
	ajuste(lola,magnitude_adjusted[j],large_reward,allSets[j])


	for i in range(4):
		myWindow.update()
		ajuste(lola,allSets[j][1+i],large_reward,allSets[j])

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


