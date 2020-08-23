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
from Sorting import shellsort as shells
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 

def compare(element1,element2):
    if int(element1['vote_count']) > int(element2['vote_count']):
        return True
    return False

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
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
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
    print("4- Consultar elementos a partir de dos listas")
    print("5- Crear un ranking con las mejores o las peores películas según el vote average o el vote count")
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

def countElementsByCriteria(criteria, lst, lst2, type="id"):
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

def orderElementsByCriteria(lst, count_average, best_worst, number):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if lst["size"]<10 or number <10:
        return 0
    else:
        shells.shellSort(lst, compare)
        lista = [{}]
        if count_average == "COUNT":
            objeto = "vote_count"
        else:
            objeto = "vote_average"
        if best_worst == "BEST":
            for i in range(1,number+1):
                fila =lt.getElement(lst,i)
                lista[0][fila["original_title"]]=fila[objeto]
        else:
            for i in range(lst["size"]-number, lst["size"]+1):
                fila = lt.getElement(lst,i)
                lista[0][fila["original_title"]]=fila[objeto]
    return lista

            
        
    

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
                lista = loadCSVFile("Data/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                lista2 = loadCSVFile("MoviesCastingRaw-small.csv")
                print("Datos cargados, ",lista['size']," elementos cargados")
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
            elif int(inputs[0])==5:
                best_worst = input("Escriba BEST si quiere que la lista se ordene en orden ascendente o WORST si quiere que se ordene en orden descendente:\n")
                average_count = input("Escriba COUNT si quiere que se organice por el vote count o AVERAGE si quiere que se organice por el vote average:\n")
                number = int(input("Escribe un numero mayor o igual a diez para el ranking:\n"))
                print("El ranking se organiza de la siguiente manera: \n", orderElementsByCriteria(lista,average_count,best_worst,number))
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()