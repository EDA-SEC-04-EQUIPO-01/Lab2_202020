"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 *
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


import pytest
import config as cf
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv

#list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'

lst_books = lt.newList(list_type)
file = cf.data_dir + 'theMoviesdb/SmallMoviesDetailsCleaned.csv'

def setUp():
    print('Loading movies')
    loadCSVFile(file, lst_books)
    print(lst_books['size'])


def tearDown():
       pass

def loadCSVFile(file, lst_books):
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst_books,row)
    except:
        print("Hubo un error con la carga del archivo")
    


def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element['vote_count'])
    

def less(element1, element2):
    if int(element1['vote_count']) < int(element2['vote_count']):
        return True
    return False

def greater(element1, element2):
    if int(element1['vote_count']) > int(element2['vote_count']):
        return True
    return False


def test_less_sort():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.insertionSort(lst_books, less)


def test_greater_sort():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.insertionSort(lst_books, greater)


def test_loading_CSV_y_ordenamiento():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.insertionSort(lst_books,less)
    while not (lt.isEmpty(lst_books)):
        x = int(lt.removeLast(lst_books)['vote_count'])
        if not (lt.isEmpty(lst_books)):
            y = int(lt.lastElement(lst_books)['vote_count'])
        else:
            break
        assert x >= y

