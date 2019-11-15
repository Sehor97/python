class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

class nodo:
    def __init__(self,i,j,clave):
        self.i = i
        self.j = j
        self.id = clave
        self.predecesor = None
        self.distancia = 0
        self.color = 'blanco'
        self.conectadoA = {}

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def asignarPredecesor(self, prede):
        self.predecesor = prede

    def asignarDistancia(self, num):
        self.distancia = num

    def asignarColor(self,color):
        self.color = color

    def __str__(self):
        return str(self.i)+ str(self.j) + str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerColor(self):
        return self.color

    def obtenerDistancia(self):
        return self.distancia

    def obtenerPredecesor(self):
        return self.predecesor

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]


class Matriz:

    def __init__(self):
        self.matriz = {}
        self.fila = 4
        self.columna = self.fila
        self.con = True

    def __iter__(self):
        return iter(self.matriz.values())

    def poblar(self):
        for i in range(int(self.fila)):

            for j in range(int(self.columna)):
                nuevoNodo = nodo(i,j,1)
                self.matriz[str(i)+str(j)]=nuevoNodo

    def obstaculos(self):
        obstaculo1 = nodo(1, 2, 0)
        obstaculo2 = nodo(2, 2, 0)
        obstaculo3 = nodo(2, 1, 0)

        self.matriz["12"] = obstaculo1
        self.matriz["22"] = obstaculo2
        self.matriz["21"] = obstaculo3

    def imprimir(self):
        imprimir = ""
        for i in range(self.fila):
            for j in range(self.columna):
                imprimir += str("[")
                imprimir += str(self.matriz[str(i)+str(j)].id)
                imprimir += str("]")
            imprimir += "\n"
        print(imprimir)

    def premio(self):
        validate = True
        while validate:
            i = int(input('ingrese la posicion i del cereza'))
            j = int(input('ingrese la posicion j del cereza'))
            if 0 <= i <= 3 and 0 <= j <= 3:
                if prueba.matriz[str(i)+str(j)] != 0:
                    premio = nodo(i, j, 3)
                    self.matriz[str(i)+str(j)] = premio
                    validate = False
                else:
                    print('la posicion que esta ingresando esta bloqueada')

    def agregarArista(self,de,a,costo=0):
        self.matriz[de].agregarVecino(self.matriz[a], costo)

    def derecha(self,clave):
        temp = self.matriz[clave]
        i = temp.i
        j = temp.j
        if j + 1 < self.fila:
            claveVesino= str(i)+str(j + 1)
            if self.matriz[claveVesino].id != 0:
                self.agregarArista(clave,claveVesino,1)

    def izquierda(self, clave):
        temp = self.matriz[clave]
        i = temp.i
        j = temp.j
        if j - 1 >= 0:
            claveVesino= str(i)+str(j - 1)
            if self.matriz[claveVesino].id != 0:
                self.agregarArista(clave,claveVesino,1)

    def inferior(self, clave):
        temp = self.matriz[clave]
        i = temp.i
        j = temp.j
        if i + 1 < self.columna:
            claveVesino= str(i + 1)+str(j)
            if self.matriz[claveVesino].id != 0:
                self.agregarArista(clave,claveVesino,1)

    def superior(self, clave):
        temp = self.matriz[clave]
        i = temp.i
        j = temp.j
        if i - 1 >= 0:
            claveVesino= str(i - 1)+str(j)
            if self.matriz[claveVesino].id != 0:
                self.agregarArista(clave,claveVesino,1)

    def pacman(self):
        inicial = ''
        validatepac = True
        while validatepac:
            i = int(input('ingrese la posicion i del pacman'))
            j = int(input('ingrese la posicion j del pacman'))
            if 0 <= i <= 3 and 0 <= j <= 3:
                clave= str(i)+str(j)
                if self.matriz[clave].id != 0:
                    inicial=clave
                    validatepac = False
                else:
                    print('la posicion que esta ingresando esta bloqueada')
        return inicial

    def construir(self):
        for k in self.matriz.keys():
            self.derecha(k)
            self.izquierda(k)
            self.superior(k)
            self.inferior(k)

    def bea(self, inicio):
        continuar = True
        inicio.asignarDistancia(0)
        inicio.asignarPredecesor(None)
        colaNodos = Cola()
        colaNodos.agregar(inicio)
        while (colaNodos.tamano() > 0 and continuar):
            nodoActual = colaNodos.avanzar()
            for vecino in nodoActual.obtenerConexiones():
                print(vecino.id)
                if (vecino.obtenerColor() == 'blanco'):
                    vecino.asignarColor('gris')
                    vecino.asignarDistancia(nodoActual.obtenerDistancia() + 1)
                    vecino.asignarPredecesor(nodoActual)
                    colaNodos.agregar(vecino)
                    if vecino.obtenerId() == 3:
                        temp = prueba.obtenerNodo(str(vecino.i)+str(vecino.j))
                        prueba.recorrer(temp)
                        print('la distancia recorrida fue de: '+str(temp.obtenerDistancia()))
                        continuar=False
            nodoActual.asignarColor('negro')

    def obtenerNodo(self,n):
        if n in self.matriz:
            return self.matriz[n]
        else:
            return None

    def recorrer(self,y):
        x = y
        while (x.obtenerPredecesor()):
            print(str(x.i)+str(x.j))
            x = x.obtenerPredecesor()
        print(str(x.i)+str(x.j))


prueba = Matriz()
prueba.poblar()
prueba.imprimir()
prueba.obstaculos()
prueba.imprimir()
prueba.premio()
prueba.imprimir()
prueba.construir()
prueba.imprimir()
inicio = prueba.pacman()
prueba.bea(prueba.matriz[inicio])
