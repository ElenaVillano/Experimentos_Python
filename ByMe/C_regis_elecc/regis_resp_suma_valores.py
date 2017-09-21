#seleccionar cualquiera de tres matrices para sumar sus valores y registras en un csv
#la letra el
from psychopy import visual, core, event, gui #el paquete gui crea cuadros de dialogo
import time 

#matriz a seleccionar
matrix1={'a':0.84, 'b': -1.08, 'c':-0.94, 'd':0.96}
matrix2={'a':0.95, 'b':1.21, 'c':1.00, 'd':-0.91}
matrix3={'a':1.11, 'b':-0.92, 'c':-0.92, 'd':0.84}
matrixSel=0
matrices=[matrix1,matrix2,matrix3] #hace una matrix con todas las matrices
userSel=0

options ={'opcion': '1', 'Nombre': 'Usuario'}
myDlg=gui.DlgFromDict(dictionary=options, title='Suma de Valores') 
#crea una variable con un cuadro de dialogo
if myDlg.OK:
	if options['opcion']=='1':
		matrixSel=0
	elif options['opcion']=='2':
		matrixSel=1
	elif options['opcion']=='3':
		matrixSel=2
	else:
		print 'Matrix incorrecta'
else:
	core.wait()
print 'Matrix selecionada:', matrixSel


myWindow = visual.Window(monitor="testMonitor",units="cm") 
myWindow.setColor([0,0,0], colorSpace='rgb255')
myWindow.update()

myfile=open (options['Nombre']+ time.strftime('%Y-%m-%d')+time.strftime('%H.%M.%S')
	+'_results.csv', 'w')
#abre un archivo y fija que es lo que quieres donde
#w para write, a para append que agrega y myfile es para abrir un documento

option={'opcion':'a'}
counter=0
myfile.write('ensayo, seleccion, pago, total \n') #etiqueta

for i in range(10):
	validKeyPressed=False 
	while not validKeyPressed:
		for key in event.getKeys():
			if key in matrices[matrixSel].keys():
				validKeyPressed= True 
				userSel= key
			elif key=='escape':
				core.quit()

	counter=counter+matrices[matrixSel][userSel]
	txtCounter=visual.TextStim(myWindow,text=str(counter), height=3, 
		color=(255,117,5), colorSpace='rgb255')
	txtCounter.pos=(0,0)
	txtCounter.draw()
	myWindow.update()
	myfile.write(str(i+1)+','+str(userSel)+ ','+ 
		str(matrices[matrixSel][userSel])+','+str(counter)+'\n') #hace tu lista de datos

myfile.close() #cierra el documento