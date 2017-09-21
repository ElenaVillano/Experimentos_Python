#seleccionar cualquiera de tres matrices para sumar sus valores
from psychopy import visual, core, event, gui #el paquete gui crea cuadros de dialogo
#matris a seleccionar
matrix1={'a':0.84, 'b': -1.08, 'c':-0.94, 'd':0.96}
matrix2={'a':0.95, 'b':1.21, 'c':1.00, 'd':-0.91}
matrix3={'a':1.11, 'b':-0.92, 'c':-0.92, 'd':0.84}
matrixSel=0
matrices=[matrix1,matrix2,matrix3] #hace una matrix con todas las matrices
userSel=0
options ={'opcion': '1'}
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
		core.quit()
else:
	core.wait(0.1)

print 'Matrix selecionada:', matrixSel

myWindow = visual.Window(monitor="testMonitor",units="cm") 
myWindow.setColor([0,0,0], colorSpace='rgb255')
myWindow.update()
myWindow.setColor([0,0,0], colorSpace='rgb255')
myWindow.update()

options={'opcion':'a'}
counter=0

for i in range(5):
	validKeyPressed=False 
	while not validKeyPressed:
		for key in event.getKeys():
			if key in matrices[matrixSel].keys():
				validKeyPressed= True 
				userSel= key
			elif key=='escape':
				core.quit()

	counter=counter+matrices[matrixSel][userSel]
	txtCounter=visual.TextStim(myWindow,text=str(counter), height=3, color=(255,117,5), colorSpace='rgb255')
	txtCounter.pos=(0,0)
	txtCounter.draw()
	myWindow.update()

