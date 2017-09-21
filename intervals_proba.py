#Tarea de eleccion temporal y probabilistica
# -*- coding: utf-8 -*-
from psychopy import visual, core, event
import csv
import random
import time

sujeto= raw_input('Participante: ')

myWindow = visual.Window(monitor="testMonitor", units="cm", fullscr=True)#False,size=(1500,1000))
myWindow.setColor([255,255,255], colorSpace="rgb255")
myWindow.update()
myMouse = event.Mouse(myWindow)

#modifica el experimento para cuantos ensayos
veces=10 #variable para decir por cuantas veces quiero que se repita
total_ensayos=240 #1=24, 2=48, 3=72, 4=96, 5=120


#Definicion de variables para tipografia
tamano_letra = 1.3 #Tamano letra de opciones
col_alter=(120,120,120) #color de opciones 
#Funcion para click y tecla de escape
def click():
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

#Instrucciones tiempo
def instruccionesproba():
	#primera plantilla introduccion
	txt_instruc1 = visual.TextStim(myWindow,text="INSTRUCCIONES:",
		height=1.5, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,5),alignHoriz='center')
	txt_instruc1_2 = visual.TextStim(myWindow,text=u"A continuación se te presentarán una serie de pares de alternativas de las cuales debes de elegir una de acuerdo a tu preferencia. Cada una de las alternativas es diferente en cantidad de dinero y probabilidad de entrega, por ejemplo:",
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
	#segunda plantilla ejemplo 
	eleccion = visual.RatingScale(myWindow, choices=['A','B'], 
	marker='hover', size=1.2, stretch=0.5, pos=(0,0.06))
	txt_instruc2 = visual.TextStim(myWindow,text=u"¿Cuál alternativa prefieres?",
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,6),alignHoriz='center',wrapWidth = 40)
	txt_instruc2_1 = visual.TextStim(myWindow,text=u"300 pesos con 80% de probabilidad ó 600 pesos con 40% de probabilidad",
		height=1, 
		color=col_alter, colorSpace="rgb255",  italic=True,
		pos=(0,4),alignHoriz='center',wrapWidth = 40)
	txt_instruc2_2 = visual.TextStim(myWindow,text=u'Si eliges la letra A implica que recibirías 300 pesos con 80% de probabilidad y habría un 20% de probabilidad de no recibir nada. Si eliges la letra B recibirías 600 pesos con 40% de probabilidad y habría 60% de probabilidad de no recibir nada.',
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,-5),alignHoriz='center',wrapWidth = 40)	
	txt_instruc2_3 = visual.TextStim(myWindow,text=u'Da click en la pantalla para ver cómo elegir entre las alternativas...',
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,-9),alignHoriz='center',wrapWidth = 40)	
	txt_instruc2.draw()
	txt_instruc2_1.draw()
	txt_instruc2_2.draw()
	txt_instruc2_3.draw()
	eleccion.draw()
	myWindow.update()
	click()

	#tercera plantilla como elegir entre las alternativas
	imgnar=visual.ImageStim(myWindow, image='letras.png',pos=(0,-4))
	txt_instruc3 = visual.TextStim(myWindow,text=u"¿Cuál alternativa prefieres?",
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,2),alignHoriz='center',wrapWidth = 40)
	txt_instruc3_1 = visual.TextStim(myWindow,text=u"300 pesos con 80% de probabilidad         ó         600 pesos con 40% de probabilidad",
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


	txt_instruc6 = visual.TextStim(myWindow,text=u"Después de que hayas elegido tu alternativa dando click en la letra, la pantalla te mostrará cuál fue la alternativa que elegiste. Para continuar con la siguiente pregunta tendrás que dar click en el centro de la pantalla. En esta siguiente pregunta se te presentará otro par de alternativas con diferentes cantidades de dinero y probabilidad y deberás de elegir entre ellas de nuevo.",
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,5),alignHoriz='center',wrapWidth = 40)
	txt_instruc7 = visual.TextStim(myWindow,text=u"Este experimento tiene como finalidad investigar la manera en que la gente toma decisiones por lo tanto no existen respuestas correctas o incorrectas, solo estamos interesados en cuál opción eligirías tu. Cada una de las preguntas es importante, ELIGE CUIDADOSAMENTE.",
		height=1, 
		color=col_alter, colorSpace="rgb255", bold=True,
		pos=(0,0),alignHoriz='center',wrapWidth = 40)
	txt_instruc8 = visual.TextStim(myWindow,text=u"Sí estás listo, da click para comenzar con el experimento...",
		height=1, 
		color=col_alter, colorSpace="rgb255", 
		pos=(0,-11),alignHoriz='center')
	txt_instruc6.draw()
	txt_instruc7.draw()
	txt_instruc8.draw()
	myWindow.update()
	click()

# Alternativas de Proba
a=[5150,100]
b=[5300,90]
c=[5450,80]
d=[5600,70]
e=[6050,40]
f=[6200,30]
g=[6350,20]
h=[6500,10]
i=[1150,100]
j=[1250,70]
k=[1350,40]
l=[1450,10]

#Grupo short delays
a_txt = visual.TextStim(myWindow,text= str(a[0])+' pesos con '+str(a[1])+ '% de probabilidad',
		height=tamano_letra, 
		color=col_alter,colorSpace='rgb255')
b_txt = visual.TextStim(myWindow,text= str(b[0])+' pesos con '+str(b[1])+ '% de probabilidad',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")
c_txt = visual.TextStim(myWindow,text= str(c[0])+' pesos con '+str(c[1])+ '% de probabilidad',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")
d_txt = visual.TextStim(myWindow,text= str(d[0])+' pesos con '+str(d[1])+ '% de probabilidad',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")
#Grupo long delays
e_txt = visual.TextStim(myWindow,text=str(e[0])+' pesos con '+str(e[1])+'% de probabilidad',
		height=tamano_letra, 
		color=col_alter,colorSpace='rgb255')
f_txt = visual.TextStim(myWindow,text=str(f[0])+' pesos con '+str(f[1])+'% de probabilidad',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")
g_txt = visual.TextStim(myWindow,text=str(g[0])+' pesos con '+str(g[1])+'% de probabilidad',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")
h_txt = visual.TextStim(myWindow,text=str(h[0])+' pesos con '+str(h[1])+'% de probabilidad',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")
#Grupo short outcomes
i_txt = visual.TextStim(myWindow,text=str(i[0])+' pesos con '+str(i[1])+'% de probabilidad',
		height=tamano_letra, 
		color=col_alter,colorSpace='rgb255')
j_txt = visual.TextStim(myWindow,text=str(j[0])+' pesos con '+str(j[1])+'% de probabilidad',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")
k_txt = visual.TextStim(myWindow,text=str(k[0])+' pesos con '+str(k[1])+'% de probabilidad',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")
l_txt = visual.TextStim(myWindow,text=str(l[0])+' pesos con '+str(l[1])+'% de probabilidad',
		height=tamano_letra, 
		color=col_alter, colorSpace="rgb255")

#Conjunto de pares de preguntas, columna por grupo
SetProba =[[(a_txt,b_txt),(a,b),1],[(b_txt,c_txt),(b,c),2],[(c_txt,d_txt),(c,d),3],[(a_txt,c_txt),(a,c),4],[(b_txt,d_txt),(b,d),5],[(a_txt,d_txt),(a,d),6],
	[(e_txt,f_txt),(e,f),7],[(f_txt,g_txt),(f,g),8],[(g_txt,h_txt),(g,h),9],[(e_txt,g_txt),(e,g),10],[(f_txt,h_txt),(f,h),11],[(e_txt,h_txt),(e,h),12], 
	[(b_txt,f_txt),(b,f),13],[(d_txt,e_txt),(d,e),14],[(c_txt,g_txt),(c,g),15],[(a_txt,e_txt),(a,e),16],[(d_txt,h_txt),(d,h),17],[(a_txt,h_txt),(a,h),18],#se sustituyeron los pares (a,d) y (e,h) porque se repiten de los otros conjuntos, se sustituyo por un par [b,f] y [c,g]
	[(i_txt,j_txt),(i,j),19],[(j_txt,k_txt),(j,k),20],[(k_txt,l_txt),(k,l),21],[(i_txt,k_txt),(i,k),22],[(j_txt,l_txt),(j,l),23],[(i_txt,l_txt),(i,l),24]]


SetProbaRep=SetProba*veces 
SetProbaAle=random.sample(SetProbaRep,len(SetProbaRep))
valores=range(total_ensayos)#para ensayos
AorB=[] #registra A o B
orden_izq_der=[] #registra posicion izquierda o derecha
dates=[]
tiempos=[]
seleccion=[]

def seleccionletra(cual_a,cual_b):
	txt_pregunta = visual.TextStim(myWindow,text=u'¿Cuál alternativa prefieres?',
		height=1, 
		color=col_alter, colorSpace="rgb255",
		pos=(0,8))
	txt_o = visual.TextStim(myWindow,text=u'ó',
		height=1, 
		color=col_alter, colorSpace="rgb255",
		pos=(0,1))	
	#RatingScale el que A y B a seleccionar, minTime= restriccion temporal 
	eleccion = visual.RatingScale(myWindow, choices=['A','B'], 
	marker='hover', size=2, stretch=0.8)

	global y #y es una variable global 
	y=random.randint(0,1) #genera 0 o 1 y estos valores controlan la posicion derecha o izquierda de la pequena cercana y demorada grande
	if y == 0:
		cual_a.pos=(12,1) #si y=0 posicion derecha de la pequena cercana
	else:
   		cual_a.pos=(-12,1) #si y=1 poscion izquierda de la pequena cercana
	if y == 1:
		cual_b.pos=(12,1) #si y=1 posicion derecha de la grande demorada
	else:
		cual_b.pos=(-12,1) #si y=0 posicion izquierda de la grande demorada

	#lugaralternativa.append(y) #registra si la posicion era inversa o no

	while eleccion.noResponse: 	#si no registra respuesta dibujar texto y eleccion
		txt_pregunta.draw() 
		txt_o.draw()
		cual_a.draw()
		cual_b.draw()
		eleccion.draw()
		myWindow.flip()
	choices=eleccion.getRating() #adquiere la eleccion de A o B del sujeto
	
	tiempo=eleccion.getRT()
	tiempos.append(tiempo)

	#a es izquierda y b es derecha
	if choices=='A': # si elige A=1, si B=0
		o='left'
	else:
		o='right'
	AorB.append(o) # registra A o B

	#condicional para mostrar la opcion elegida
	elegiste_txt = visual.TextStim(myWindow,text=u'Elegiste:',
		height=1, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,5))
	sig_txt = visual.TextStim(myWindow,text=u'Da click aquí para la siguiente pregunta',
		height=0.8, 
		color=col_alter, colorSpace="rgb255", italic=True,
		pos=(0,-3))
	
	if y==1: #posicion rss izquierda y rll derecha
		if choices=='A':
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
	else: #posicion rll izquierda y rss derecha
		if choices=='A':
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

	#condicional para ver si eligio la grande o la pequena
	if y==1: #posicion correcta entonces pequena,cercana,izquierda,A,0 y grande,demorada,derecha,B,1
		if choices == 'A':
			x=0
		else:
			x=1
	else: #posicion contraria(incorrecta) entonces grande,demorada,izquierda,A,1 y cercana,pequena,derecha,B,0
		if choices=='A':
			x=1
		else:
			x=0
    	seleccion.append(x) #registra pequena,cercana=0 y grande,demorada=1

def swap(t1,t2): #funcion que cambia de posicion pares de variables
	return t2,t1

#Comienzo experimento
instruccionesproba()
myWindow.update()

for i in range(len(SetProbaAle)): #ciclo que permite que se repitan los ensayos con diferentes valores
	myMouse=event.Mouse(win=myWindow,newPos=(0,-3))	
	seleccionletra(SetProbaAle[(i)][(0)][(0)],SetProbaAle[(i)][(0)][(1)])
	myWindow.update()
	#condicional que permite registrar si las alternativas estaban en la izquierda o derecha
	if y==1: #si y=1 entonces la posicion normal
		u=SetProbaAle[(i)][(1)][(0)],SetProbaAle[(i)][(1)][(1)]
	else: #si y=0 entonces se invierte la posicion
		u=swap(SetProbaAle[(i)][(1)][(0)],SetProbaAle[(i)][(1)][(1)])
	orden_izq_der.append(u) #se agrega en variable

	date=time.ctime()
	dates.append(date)

termino = visual.TextStim(myWindow,text="El experimento ha terminado...",
	height=1.1, 
	color=col_alter, colorSpace="rgb255", 
	pos=(0,3),alignHoriz='center')
termino1 = visual.TextStim(myWindow,text=u"Gracias por tu participación.",
	height=1.2, 
	color=col_alter, colorSpace="rgb255", 
	pos=(0,-4),alignHoriz='center')

termino.draw()
termino1.draw()
myWindow.update()
click()

salvadatos=('sujeto_'+str(sujeto)+'_proba.csv')
with open(salvadatos,'wb') as csvfile:
	ensayo=csv.writer(csvfile,delimiter=',')
	ensayo.writerow(['trial','money_left','proba_left','money_right','proba_right','choiceP','biggerchosenP','pairP','time','date'])
	for i in range(len(SetProbaAle)):
		ensayo.writerow([valores[i]+1,
			orden_izq_der[i][0][0],
			orden_izq_der[i][0][1],
			orden_izq_der[i][1][0],
			orden_izq_der[i][1][1],
			AorB[i],
			seleccion[i],
			SetProbaAle[(i)][(2)],
			tiempos[i],
			dates[i]])


