import csv

MAX_COL = 785
MAX_FILAS = 42001
MAX_PIXEL_VALUE = 256
CANT_CLASES = 10

# Carga los datos del archivo de entrenamiento (train.csv) a un TDA
# diccionario que va a tener como claves los indices de filas de ese 
# train,y como valor una lista donde el primer elemento va a ser el 
# label (el numero que esta dibujado) y los demas elementos van a ser 
# los valores del pixel correspondiente (pixeles --0 a 785-- con valores
# de 0 a 255 inclusive)
def cargarDatos(nombreArchivo):

	dicDatos = {} 

	for i in range(0,MAX_FILAS):
		dicDatos[i] = []
	
	with open(nombreArchivo) as entrenamiento:
		reader = csv.reader(entrenamiento, delimiter=',')
		
		indiceFila = 0;
		
		for linea in reader:
			if(linea[0]) == "label": # No considero la primera linea
				continue
				
			label = int(linea[0])
			
			if not esLabelValido(label):
				continue
				
			dicDatos[indiceFila].append(label)

			for p in range(1,MAX_COL):
				pixelValue = int(linea[p])
				
				if not esPixelValueValido(pixelValue):
					continue
				
				dicDatos[indiceFila].append(pixelValue)
			
			++indiceFila
		
	return dicDatos


# Validaciones

def esLabelValido(unLabel):
	if unLabel in range(0,CANT_CLASES):
		return True
	return False

def esPixelValueValido(unPixelValue):
	if unPixelValue in range (0,MAX_PIXEL_VALUE):
		return True
	return False


# Getters (?)

def obtenerLabelDelIndice(dicDatos,indiceLabel):
	return dicDatos[indiceLabel][0]
	

def obtenerPromedioLabelDelIndice(dicDatos,indiceLabel):
	filaLabel = dicDatos[indiceLabel]
	
	sumatoriaDePixelValues = 0;
	
	for i in range(1,MAX_COL):
		sumatoriaDePixelValues = sumatoriaDePixelValues + filaLabel[i]
	
	promedio = float(sumatoriaDePixelValues / MAX_COL)
	
	return promedio
	
	
	
# -------------------------------------------



dicDatos = cargarDatos('train.csv')
print dicDatos[0]
print "hola"
