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
import config 
from DataStructures import arraylist as slt



def cmpfunction (element1, element2):
    if element1["vote_count"] == element2["vote_count"]:
        return 0
    elif element1["vote_count"] < element2["vote_count"]:
        return -1
    else:
        return 1


@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
def movies ():
    movies = []
    movies.append({'id': '2817', 'budget': '0', 'genres': 'Drama|Comedy|Romance', 'imdb_id': 'tt0119828', 'original_language': 'fr', 'original_title': 'On connaît la chanson', 'overview': "Odile is a business executive looking for a new, bigger apartment. Her younger sister Camille has just completed her doctoral thesis in history and is a Paris tour guide. Simon is a regular on Camille's tours because he's attracted to her. Camille has fallen for Marc, and they begin an affair. Nicolas is also looking for an apartment, since he hopes to eventually have his family join him in Paris.", 'popularity': '0.631543', 'production_companies': 'France 2 Cinéma', 'production_countries': 'Italy', 'release_date': '12/11/1997', 'revenue': '0', 'runtime': '120', 'spoken_languages': 'Français', 'status': 'Released', 'tagline': '', 'title': 'Same Old Song', 'vote_average': '6.8', 'vote_count': '13', 'production_companies_number': '4', 'production_countries_number': '4', 'spoken_languages_number': '1'})
    movies.append({'id': '2790', 'budget': '0', 'genres': 'Action|Thriller|Foreign', 'imdb_id': 'tt1232001', 'original_language': 'de', 'original_title': 'Der Abgrund - Eine Stadt stürzt ein', 'overview': 'A series of strange accidents plaguing a city located near the mine. Two people were pulled through the funnel, which formed after the collapse of tunnels under the lake. Geologist Nina Thiemann discovers that the mine tunnels are insecure and unstable. A woman with an expert in the field of explosions and a father, a former miner, descend into the ground, hoping that they will prevent catastrophe', 'popularity': '0.038584', 'production_companies': 'none', 'production_countries': 'Germany', 'release_date': '02/06/2008', 'revenue': '0', 'runtime': '90', 'spoken_languages': 'Deutsch', 'status': 'Released', 'tagline': '', 'title': "Below the Earth's Surface", 'vote_average': '5.7', 'vote_count': '3', 'production_companies_number': '0', 'production_countries_number': '1', 'spoken_languages_number': '1'})
    movies.append({'id': '2771', 'budget': '0', 'genres': 'Comedy|Drama', 'imdb_id': 'tt0305206', 'original_language': 'en', 'original_title': 'American Splendor', 'overview': 'An original mix of fiction and reality illuminates the life of comic book hero everyman Harvey Pekar.', 'popularity': '1.399058', 'production_companies': 'none', 'production_countries': 'United States of America', 'release_date': '15/08/2003', 'revenue': '6003587', 'runtime': '101', 'spoken_languages': 'English', 'status': 'Released', 'tagline': 'Ordinary life is pretty complex stuff', 'title': 'American Splendor', 'vote_average': '7.2', 'vote_count': '114', 'production_companies_number': '0', 'production_countries_number': '1', 'spoken_languages_number': '1'})
    movies.append({'id': '2904', 'budget': '85000', 'genres': 'Horror|Thriller', 'imdb_id': 'tt1597526', 'original_language': 'es', 'original_title': 'Colgado de la luna', 'overview': '', 'popularity': '0.002444', 'production_companies': 'none', 'production_countries': 'Spain', 'release_date': '30/10/2005', 'revenue': '4236', 'runtime': '87', 'spoken_languages': 'Español', 'status': 'Released', 'tagline': '', 'title': 'Colgado de la luna', 'vote_average': '0.0', 'vote_count': '0', 'production_companies_number': '0', 'production_countries_number': '1', 'spoken_languages_number': '1'})
    movies.append({'id': '2991', 'budget': '0', 'genres': 'Thriller', 'imdb_id': 'tt0070031', 'original_language': 'en', 'original_title': 'La Encadenada', 'overview': 'A beautiful young woman sets her sights on an aging millionaire. She seduces him, and moves into his mansion with him. She soon tires of him, though, and after she gets rid of him, she goes after his son.', 'popularity': '0.401887', 'production_companies': 'Emaus Films S.A.', 'production_countries': 'Italy', 'release_date': '04/05/1975', 'revenue': '0', 'runtime': '95', 'spoken_languages': 'English', 'status': 'Released', 'tagline': '', 'title': 'A Diary of a Murderess', 'vote_average': '8.5', 'vote_count': '1', 'production_companies_number': '1', 'production_countries_number': '2', 'spoken_languages_number': '1'})
    print (movies[0])
    return movies


@pytest.fixture
def lstmovies(movies):
    lst = slt.newList(cmpfunction)
    for i in range(0,5):    
        slt.addLast(lst,movies[i])    
    return lst



def test_empty (lst):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0



def test_addFirst (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, movies[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, movies[2])
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == movies[2]




def test_addLast (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, movies[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, movies[2])
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == movies[1]
    movie = slt.lastElement(lst)
    assert movie == movies[2]




def test_getElement(lstmovies, movies):
    movie = slt.getElement(lstmovies, 1)
    assert movie == movies[0]
    movie = slt.getElement(lstmovies, 5)
    assert movie == movies[4]





def test_removeFirst (lstmovies, movies):
    assert slt.size(lstmovies) == 5
    slt.removeFirst(lstmovies)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, 1)
    assert movie  == movies[1]



def test_removeLast (lstmovies, movies):
    assert slt.size(lstmovies) == 5
    slt.removeLast(lstmovies)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, 4)
    assert movie  == movies[3]



def test_insertElement (lst, movies):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, movies[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, movies[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, movies[2], 1)
    assert slt.size(lst) == 3
    movie = slt.getElement(lst, 1)
    assert movie == movies[2]
    movie = slt.getElement(lst, 2)
    assert movie == movies[0]



def test_isPresent (lstmovies, movies):
    movie = {'id': '2992', 'budget': '0', 'genres': 'Foreign|Horror|Thriller', 'imdb_id': 'tt0149698', 'original_language': 'en', 'original_title': 'Appetite', 'overview': '', 'popularity': '0.034221', 'production_companies': '101 Productions', 'production_countries': 'United Kingdom', 'release_date': '12/08/1998', 'revenue': '0', 'runtime': '97', 'spoken_languages': 'English', 'status': 'Released', 'tagline': '', 'title': 'Appetite', 'vote_average': '0.0', 'vote_count': '0', 'production_companies_number': '3', 'production_countries_number': '1', 'spoken_languages_number': '1'}
    print(slt.isPresent (lstmovies, movies[2]))
    assert slt.isPresent (lstmovies, movies[2]) > 0
    assert slt.isPresent (lstmovies, movie) >= 0
    


def test_deleteElement (lstmovies, movies):
    pos = slt.isPresent (lstmovies, movies[2])
    assert pos > 0
    movie = slt.getElement(lstmovies, pos)
    assert movie == movies[2]
    slt.deleteElement (lstmovies, pos)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, pos)
    assert movie == movies[3]


def test_changeInfo (lstmovies):
    movie10 = {'movie_id':'10', 'movie_title':'Title 10', 'author':'author 10'}
    slt.changeInfo (lstmovies, 1, movie10)
    movie = slt.getElement(lstmovies, 1)
    assert movie10 == movie


def test_exchange (lstmovies, movies):
    movie1 = slt.getElement(lstmovies, 1)
    movie5 = slt.getElement(lstmovies, 5)
    slt.exchange (lstmovies, 1, 5)
    assert slt.getElement(lstmovies, 1) == movie5
    assert slt.getElement(lstmovies, 5) == movie1