import pytest 
import config 
from DataStructures import arraylist as slt



def cmpfunction (element1, element2):
    if element1["id"] == element2["id"]:
        return 0
    elif element1["id"] < element2["id"]:
        return -1
    else:
        return 1


@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
def books ():
    books = []
    books.append({'id': '155', 'budget': '185000000', 'genres': 'Drama|Action|Crime|Thriller', 'imdb_id': 'tt0468569', 'original_language': 'en', 'original_title': 'The Dark Knight', 'overview': 'Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.', 'popularity': '14.074094', 'production_companies': 'DC Comics', 'production_countries': 'United Kingdom', 'release_date': '16/07/2008', 'revenue': '1004558444', 'runtime': '152', 'spoken_languages': 'English', 'status': 'Released', 'tagline': 'Why So Serious?', 'title': 'The Dark Knight', 'vote_average': '8.2', 'vote_count': '11168', 'production_companies_number': '5', 'production_countries_number': '2', 'spoken_languages_number': '2'})
    books.append({'id': '603', 'budget': '63000000', 'genres': 'Action|Science Fiction', 'imdb_id': 'tt0133093', 'original_language': 'en', 'original_title': 'The Matrix', 'overview': 'Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.', 'popularity': '12.016524', 'production_companies': 'Village Roadshow Pictures', 'production_countries': 'Australia', 'release_date': '30/03/1999', 'revenue': '463517383', 'runtime': '136', 'spoken_languages': 'English', 'status': 'Released', 'tagline': 'Welcome to the Real World.', 'title': 'The Matrix', 'vote_average': '7.9', 'vote_count': '8321', 'production_companies_number': '4', 'production_countries_number': '2', 'spoken_languages_number': '1'})
    books.append({'id': '120', 'budget': '93000000', 'genres': 'Adventure|Fantasy|Action', 'imdb_id': 'tt0120737', 'original_language': 'en', 'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 'overview': 'Young hobbit Frodo Baggins, after inheriting a mysterious ring from his uncle Bilbo, must leave his home in order to keep it from falling into the hands of its evil creator. Along the way, a fellowship is formed to protect the ringbearer and make sure that the ring arrives at its final destination: Mt. Doom, the only place where it can be destroyed.', 'popularity': '11.296176', 'production_companies': 'WingNut Films', 'production_countries': 'New Zealand', 'release_date': '18/12/2001', 'revenue': '871368364', 'runtime': '178', 'spoken_languages': 'English', 'status': 'Released', 'tagline': 'One ring to rule them all', 'title': 'The Lord of the Rings: The Fellowship of the Ring', 'vote_average': '8.0', 'vote_count': '8127', 'production_companies_number': '3', 'production_countries_number': '2', 'spoken_languages_number': '1'})
    books.append({'id': '278', 'budget': '25000000', 'genres': 'Drama|Crime', 'imdb_id': 'tt0111161', 'original_language': 'en', 'original_title': 'The Shawshank Redemption', 'overview': 'Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.', 'popularity': '10.7546', 'production_companies': 'Castle Rock Entertainment', 'production_countries': 'United States of America', 'release_date': '23/09/1994', 'revenue': '28341469', 'runtime': '142', 'spoken_languages': 'English', 'status': 'Released', 'tagline': 'Fear can hold you prisoner. Hope can set you free.', 'title': 'The Shawshank Redemption', 'vote_average': '8.5', 'vote_count': '7711', 'production_companies_number': '1', 'production_countries_number': '1', 'spoken_languages_number': '1'})
    books.append({'id':'122', 'budget': '94000000', 'genres': 'Adventure|Fantasy|Action', 'imdb_id': 'tt0167260', 'original_language': 'en', 'original_title': 'The Lord of the Rings: The Return of the King', 'overview': "Aragorn is revealed as the heir to the ancient kings as he, Gandalf and the other members of the broken fellowship struggle to save Gondor from Sauron's forces. Meanwhile, Frodo and Sam bring the ring closer to the heart of Mordor, the dark lord's realm.", 'popularity': '10.166865', 'production_companies': 'WingNut Films', 'production_countries': 'New Zealand', 'release_date': '01/12/2003', 'revenue': '1118888979', 'runtime': '201', 'spoken_languages': 'English', 'status': 'Released', 'tagline': 'The eye of the enemy is moving.', 'title': 'The Lord of the Rings: The Return of the King', 'vote_average': '8.1', 'vote_count': '7540', 'production_companies_number': '2', 'production_countries_number': '2', 'spoken_languages_number': '1'})
    print (books[0])
    return books


@pytest.fixture
def lstbooks(books):
    lst = slt.newList(cmpfunction)
    for i in range(0,5):    
        slt.addLast(lst,books[i])    
    return lst



def test_empty (lst):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0



def test_addFirst (lst, books):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, books[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, books[2])
    assert slt.size(lst) == 2
    book = slt.firstElement(lst)
    assert book == books[2]




def test_addLast (lst, books):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, books[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, books[2])
    assert slt.size(lst) == 2
    book = slt.firstElement(lst)
    assert book == books[1]
    book = slt.lastElement(lst)
    assert book == books[2]




def test_getElement(lstbooks, books):
    book = slt.getElement(lstbooks, 1)
    assert book == books[0]
    book = slt.getElement(lstbooks, 5)
    assert book == books[4]





def test_removeFirst (lstbooks, books):
    assert slt.size(lstbooks) == 5
    slt.removeFirst(lstbooks)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, 1)
    assert book  == books[1]



def test_removeLast (lstbooks, books):
    assert slt.size(lstbooks) == 5
    slt.removeLast(lstbooks)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, 4)
    assert book  == books[3]



def test_insertElement (lst, books):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, books[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, books[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, books[2], 1)
    assert slt.size(lst) == 3
    book = slt.getElement(lst, 1)
    assert book == books[2]
    book = slt.getElement(lst, 2)
    assert book == books[0]



def test_isPresent (lstbooks, books):
    book = {'id':'10', 'book_title':'Title 10', 'author':'author 10'}
    print(slt.isPresent (lstbooks, books[2]))
    assert slt.isPresent (lstbooks, books[2]) > 0
    assert slt.isPresent (lstbooks, book) == 0
    


def test_deleteElement (lstbooks, books):
    pos = slt.isPresent (lstbooks, books[2])
    assert pos > 0
    book = slt.getElement(lstbooks, pos)
    assert book == books[2]
    slt.deleteElement (lstbooks, pos)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, pos)
    assert book == books[3]


def test_changeInfo (lstbooks):
    book10 = {'id': '155', 'budget': '185000000', 'genres': 'Drama|Action|Crime|Thriller'}
    slt.changeInfo (lstbooks, 1, book10)
    book = slt.getElement(lstbooks, 1)
    assert book10 == book


def test_exchange (lstbooks, books):
    book1 = slt.getElement(lstbooks, 1)
    book5 = slt.getElement(lstbooks, 5)
    slt.exchange (lstbooks, 1, 5)
    assert slt.getElement(lstbooks, 1) == book5
    assert slt.getElement(lstbooks, 5) == book1