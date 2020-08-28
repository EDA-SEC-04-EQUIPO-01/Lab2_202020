"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import insertionsort as insort
from Sorting import selectionsort as selsort
from Sorting import shellsort as shsort



from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Conocer el trabajo de un director")
    print("5- Conocer los rankings de las películas")
    print("6-")
    print("7- Conocer un genero")
    print("8-")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, lst, lst2, type):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    t1_start = process_time()
    counter = 0
    iterator = it.newIterator(lst)
    pel_id = []
    while it.hasNext(iterator):
        element = it.next(iterator)
        if criteria.lower() == element["director_name"].lower():
            pel_id.append(element["id"])
            counter +=1
    
    iterator = it.newIterator(lst2)
    lst_pel=[]
    suma = 0
    div = 0
    promedio = 0
    while it.hasNext(iterator):
        element = it.next(iterator)
        if element[type] in pel_id:
            lst_pel.append(element["original_title"])
            suma+=float(element["vote_average"])
            div +=1
    
    try:
        promedio = suma/div
    except:
        print("Este director no tiene películas en el registro")

    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    
    return (lst_pel,counter,promedio)

def less_count(element1, element2):
    if float(element1['vote_count']) < float(element2['vote_count']):
        return True
    return False

def less_average(element1, element2):
    if float(element1['vote_average']) < float(element2['vote_average']):
        return True
    return False

def greater_count(element1, element2):
    if float(element1['vote_count']) > float(element2['vote_count']):
        return True
    return False

def greater_average(element1, element2):
    if float(element1['vote_average']) > float(element2['vote_average']):
        return True
    return False

def orderElementsByCriteria(lst,tipo,gb,cant):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    t1_start = process_time()
    if tipo == 1:
        print("Filtrando listas...")
        shsort.shellSort(lst,greater_count)
        if gb == 1:
            bestcount = []
            for a in list(range(1,cant+1)):
                element = lt.getElement(lst,a)
                bestcount.append({element["original_title"]:element["vote_count"]})
            print("Top",cant, "películas con mayor cantidad de votos: \n",bestcount)

        elif gb == 2:
            worstcount = []
            for a in list(range(lt.size(lst)-(cant),lt.size(lst))):
                element = lt.getElement(lst,a)
                worstcount.append({element["original_title"]:element["vote_count"]})
            print("Top",cant, "películas con menor cantidad de votos: \n",worstcount)

    if tipo == 2:
        print("Filtrando listas...")
        shsort.shellSort(lst,greater_average)
        if gb ==1:
            bestaverage = []
            for a in list(range(1,cant+1)):
                element = lt.getElement(lst,a)
                bestaverage.append({element["original_title"]:element["vote_average"]})
            print("Top",cant,"películas con mejor promedio de votos: \n",bestaverage)

        elif gb ==2:
            worstaverage = []
            for a in list(range(lt.size(lst)-(cant),lt.size(lst))):
                element = lt.getElement(lst,a)
                worstaverage.insert(0,{element["original_title"]:element["vote_average"]})
            print("Top",cant, "películas con peor promedio de votos: \n",worstaverage)

    t1_stop = process_time()
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

    return "Acción realizada con éxito"

def conocerUnGenero(lst,genero):
    t1_start = process_time()
    iterator = it.newIterator(lst)
    pelis = []
    sumpr = 0
    counter = 0
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        while it.hasNext(iterator):
            element = it.next(iterator)
            if genero.lower() in element["genres"].lower():
                pelis.append(element["original_title"])
                sumpr += float(element["vote_average"])
                counter+=1
    try:
        promedio = sumpr/counter
    except:
        promedio = 0

    print("El género",genero,"tiene un total de",counter,"películas con un promedio acumulado de",round(promedio,3))
    print(pelis)

    return "Acción realizada con éxito"



def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    lista2 = lt.newList()
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/theMoviesdb/AllMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                print("Datos de películas cargados, ",lista['size']," elementos cargados")
                lista2 = loadCSVFile("Data/theMoviesdb/AllMoviesCastingRaw.csv")
                print("Datos del elenco cargados, ",lista2['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    if lt.size(lista)>2000:
                        type = "\ufeffid"
                    else:
                        type = "id"
                    criteria =input('Ingrese el nombre del director\n')
                    counter=countElementsByCriteria(criteria,lista2,lista,type)
                    print("El director",criteria,"tiene un total de",counter[1],"películas con una calificación promedio de",counter[2],"\n",counter[0])
            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    tipo = int(input("Ingrese si quiere ver la cantidad de votos o el promedio de votos (1 o 2): "))
                    guba = int(input("Ingrese si quiere ver las mejores o las peores (1 o 2): "))
                    cant = int(input("Ingrese la cantidad de películas que desea ver en el top: "))
                    orderElementsByCriteria(lista, tipo, guba, cant)
            elif int(inputs[0])==6: #opcion 6
                pass
            elif int(inputs[0])==7: #opcion 7
                genero = input("Ingrese el género que desea conocer: ")
                conocerUnGenero(lista,genero)

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()