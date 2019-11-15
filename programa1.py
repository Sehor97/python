class nodo:
    def __init__(self):
        self.i = None
        self.j = None
        self.value = None
        self.revisado = ''


class Matriz:

    def __init__(self):
        self.matriz = {}
        self.fila = 4
        self.columna = self.fila
        self.hijos = []
        self.con = True

    def poblar(self):
        for i in range(int(self.fila)):
            self.matriz.append([])
            for j in range(int(self.columna)):
                self.matriz[i].append(1)

    def obstaculos(self):
        self.matriz[1][2] = 0
        self.matriz[2][2] = 0
        self.matriz[2][1] = 0

    def premio(self):
        validate = True
        while validate:
            i = int(input('ingrese la posicion i del cereza'))
            j = int(input('ingrese la posicion j del cereza'))
            if 0 < i <= 3 and 0 < j <= 3:
                if prueba.matriz[i][j] != 0:
                    self.matriz[i][j] = 3
                    validate = False
                else:
                    print('la posicion que esta ingresando esta bloqueada')

    def imprimir(self):
        imprimir = ""
        for i in range(self.fila):
            for j in range(self.fila):
                imprimir += str("[")
                imprimir += str(self.matriz[i][j])
                imprimir += str("]")
            imprimir += "\n"
        print(imprimir)

    def derecha(self, nodoent):
        nodosal = None
        if nodoent.j + 1 < self.fila:
            if self.matriz[nodoent.i][nodoent.j + 1] != 0 and nodoent.revisado is not True:
                nodosal = nodo()
                itemd = self.matriz[nodoent.i][nodoent.j + 1]
                nodosal.i = nodoent.i
                nodosal.j = nodoent.j + 1
                nodosal.value = itemd
                nodosal.revisado = 'der'
                print('----derecha-----')
                print('---entrada')
                print(nodoent.i, nodoent.j, nodoent.value, nodoent.revisado)
                print('----salida----')
                print(nodosal.i, nodosal.j, nodosal.value, nodosal.revisado)

        return nodosal

    def izquierda(self, nodoent):
        nodosal = None
        if nodoent.j - 1 >= 0:
            if self.matriz[nodoent.i][nodoent.j - 1] != 0 and nodoent.revisado is not True:
                nodosal = nodo()
                itemi = self.matriz[nodoent.i][nodoent.j - 1]
                nodosal.i = nodoent.i
                nodosal.j = nodoent.j - 1
                nodosal.value = itemi
                nodosal.revisado = 'izq'
                print('----izquierda-----')
                print('---entrada')
                print(nodoent.i, nodoent.j, nodoent.value, nodoent.revisado)
                print('----salida----')
                print(nodosal.i, nodosal.j, nodosal.value, nodosal.revisado)

        return nodosal

    def inferior(self, nodoent):
        nodosal = None
        if nodoent.i + 1 < self.columna:
            if self.matriz[nodoent.i + 1][nodoent.j] != 0 and nodoent.revisado is not True:
                nodosal = nodo()
                items = self.matriz[nodoent.i + 1][nodoent.j]
                nodosal.i = nodoent.i + 1
                nodosal.j = nodoent.j
                nodosal.value = items
                nodosal.revisado = 'inf'
                print('----inferior-----')
                print('---entrada')
                print(nodoent.i, nodoent.j, nodoent.value, nodoent.revisado)
                print('----salida----')
                print(nodosal.i, nodosal.j, nodosal.value, nodosal.revisado)

        return nodosal

    def superior(self, nodoent):
        nodosal = None
        if nodoent.i - 1 >= 0:
            if self.matriz[nodoent.i - 1][nodoent.j] != 0 and nodoent.revisado is not True:
                nodosal = nodo()
                itemsup = self.matriz[nodoent.i - 1][nodoent.j]
                nodosal.i = nodoent.i - 1
                nodosal.j = nodoent.j
                nodosal.value = itemsup
                nodosal.revisado = 'sup'
                print('----superior-----')
                print('---entrada')
                print(nodoent.i, nodoent.j, nodoent.value, nodoent.revisado)
                print('----salida----')
                print(nodosal.i, nodosal.j, nodosal.value, nodosal.revisado)

        return nodosal

    def find(self, nodo):
        self.hijos.append(nodo)
        continuar = self.con
        colas = []
        der = None
        inf = None
        sup = None
        izq = None

        if nodo.revisado == '':
            inf = self.inferior(nodo)
            der = self.derecha(nodo)
            sup = self.superior(nodo)
            izq = self.izquierda(nodo)
        if nodo.revisado == 'izq':
            izq = self.izquierda(nodo)
            inf = self.inferior(nodo)
            sup = self.superior(nodo)
        if nodo.revisado == 'sup':
            sup = self.superior(nodo)
            der = self.derecha(nodo)
            izq = self.izquierda(nodo)
        if nodo.revisado == 'inf':
            inf = self.inferior(nodo)
            der = self.derecha(nodo)
            izq = self.izquierda(nodo)
        if nodo.revisado == 'der':
            der = self.derecha(nodo)
            inf = self.inferior(nodo)
            sup = self.superior(nodo)

        if inf is not None:
            colas.append(inf)
        if der is not None:
            colas.append(der)
        if izq is not None:
            colas.append(izq)
        if sup is not None:
            colas.append(sup)

        for i in range(len(colas)):
            if colas[i].value == 3:
                print(colas[i].value)
                print('---fin---')
                continuar = False
                break

        if continuar is True:
            for i in range(len(colas)):
                print(colas[i].value)
                print('------')
                self.find(colas[i])
        else:
            breakpoint()
            print("ENCONTRADO")


prueba = Matriz()
prueba.poblar()
prueba.obstaculos()
prueba.imprimir()
prueba.premio()
prueba.imprimir()
inicial = nodo()
validatepac = True
while validatepac:
    inicial.i = int(input('ingrese la posicion i del pacman'))
    inicial.j = int(input('ingrese la posicion j del pacman'))
    if 0 <= inicial.i <= 3 and 0 <= inicial.j <= 3:
        if prueba.matriz[inicial.i][inicial.j] != 0 :
            validatepac = False
        else:
            print('la posicion que esta ingresando esta bloqueada')

inicial.value = prueba.matriz[inicial.i][inicial.j]
inicial.revisado = ''
prueba.find(inicial)
