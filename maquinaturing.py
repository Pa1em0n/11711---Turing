
#creamos el diccionario de estado de tamano 1000
dic1 = {}
for e in range(1000):
	dic1[e] ='0'	

#Metodo que crea una lista de reglas que se desde la lee desde la linea de comandos
def entrada(reglas):
	lfinal = [reglas[0],reglas[1]]
	ls = reglas[2:reglas[0]+2]
	for k in ls:
		r = k.split(' ')
		lr = [int(r[0]),r[1],int(r[2]),r[3],r[4]]
		lfinal.append(lr)

	li = reglas[reglas[0]+2:]
	for i in li:
		iterraciones = i.split(' ')
		rango = [int(iterraciones[0]),int(iterraciones[1])]
		lfinal.append(rango)
	return(lfinal)

#Metodo de entrada, que asigna unos en la cinta dada el valor de X donde  1<=X
def entrada_programa(x):
	for i in range(x):
		dic1[i] = '1'
	return 0
	
#Metodo que regresa el valor esperado, dada la cinda llena de unos, y recorrore la cinta en  Y<=1000
def valor_esperado(de,y):
	c2 = de
	for i in range(0,y):
		if(c2[i] == '0'):
			return False
	for j in range(y,1000):
		if(c2[i] == '1'):
			return False
	return True

#Metodo que aplica las reglas dadar por el usuario, regresa  'MLe','TLE','AC','WA'				
def turing(fin):
	lf = entrada(fin)	
	for j in lf[lf[0]+2:-1]:
		x = j[0]
		y = j[1]
		entrada_programa(x)
		edo_actual = 0
		indice_actual = 0
		iteracion_total = 0
		numero_reglas = lf[0]
		resultado = 'Ninguno'
		while((lf[0]<=1000) and iteracion_total<=1000):
			for i in range(2,lf[0]+2):
				edo_actual = lf[i][2]
				dic1[indice_actual] = lf[i][3]
				if(lf[i][4] == 'R'):
					indice_actual += 1
				elif(lf[i][4] == 'L'):
					indice_actual -= 1

				if ((indice_actual<0)or(indice_actual==1000)):
					resultado = 'MLE'
					break
				num_reglas = lf[0]
				iteracion_total +=1

		if(iteracion_total>10000):
			resultado = 'TLE'
		if(resultado == 'Ninguno'):
			if(valor_esperado(dic1,y)==True):
					resultado = "AC"	
			else:
					resultado = 'WA'

		if(resultado == 'TLE'):
			print('TLE\n')
		elif(resultado =='MLE'):
			print('MLE\n')
		elif(resultado=='WA'):
			print('WA\n')
		elif(resultado=='AC'):
			print('AC\n')

	return 0

print('\n\n\t"Maquina de turing"\n')
print ('escribe la entrada en el siguiente formato:\n\tejemplo.\n6 2\n0 1 1 0 R\n0 0 0 0 R\n1 1 1 1 R\n1 0 2 1 L\n2 1 2 1 L\n2 0 900 1 R\n1 3\n300 301\n0 0\n')
print('\n\tEscribe la entrada:\n')
#Leemos en la linea de comandos las reglas.
linea1 = raw_input()
num_reglas = linea1.split(' ')
n1 = int(num_reglas[0])
n2 = int(num_reglas[1])
reglas = [n1,n2]
for x in range(n1+n2+1):
	e = raw_input()
	reglas.append(e)
print('\n')
turing(reglas)
