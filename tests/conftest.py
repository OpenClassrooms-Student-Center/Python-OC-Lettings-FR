import sqlite3
import pytest

from django.test import Client


@pytest.fixture
def client():
    return Client()


# 1 Create a new fixture
# 2 Use sqlite3 from standard library and connect to in memory database
# 3 Use DB cursor to create a table
# 4 Create the table
# 5 Create some datas
# 6 Put datas in the table
# 7 yield splits our fixture in 2 parts

@pytest.fixture  # 1
def session():
    '''Set up dtatabase for session with datas return the database session.'''
    connection = sqlite3.connect(':memory:')  # 2
    db_session = connection.cursor()  # 3
    db_session.execute('''CREATE TABLE IF NOT EXISTS address
                          (id INTEGER PRIMARY KEY, number int, street str, city str, state str,
                           zip_code int, country_iso_code str )''')  # 4
    db_session.execute('''CREATE TABLE IF NOT EXISTS letting
                          (id INTEGER PRIMARY KEY, title str, adress int)''')  # 4
    db_session.execute('''CREATE TABLE IF NOT EXISTS profile
                          (id INTEGER PRIMARY KEY, user str, favorite_city str )''')  # 4

    address_sample_datas = [
        (1, 7217, 'Bedford Street', 'Brunswick', 'GA', 31525, 'USA'),  # 5
        (2, 4, 'Military Street', 'Willoughby', 'OH', 44094, 'USA'),
    ]
    letting_sample_datas = [
        (1, "Joshua Tree Green Haus /w Hot Tub", 1),
        (2, "Oceanview Retreat", 2),
        (3, "'Silo Studio' Cottage", 3),
        (4, "Pirates of the Caribbean Getaway", 4)
    ]
    profile_sample_datas = [
        (1, "HeadlinesGazer", "Buenos Aires"),
        (2, "DavWin", "Barcelona"),
        (3, "AirWow", "Budapest"),
    ]
    db_session.executemany(
        'INSERT INTO address VALUES(?, ?, ?, ?, ?, ?, ?)', address_sample_datas)  # 6
    db_session.executemany(
        'INSERT INTO letting VALUES(?, ?, ?)', letting_sample_datas)  # 6
    db_session.executemany(
        'INSERT INTO profile VALUES(?, ?, ?)', profile_sample_datas)  # 6
    connection.commit()
    yield db_session  # 7
    connection.close()


@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    settings.DATABASES['default'] = {

        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test-db.sqlite3',
        "ATOMIC_REQUESTS": False,

    }
