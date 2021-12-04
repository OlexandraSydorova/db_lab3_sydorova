import csv
import decimal
import psycopg2
import random

username = 'Sydorova_Olexandra'
password = '111'
database = 'Sydorova_Olexandra_lr2_DB'

INPUT_CSV_FILE = 'disney_movies.csv'

query_1 = '''
DELETE FROM disney_film
'''
query_2 = '''
INSERT INTO disney_film (film_id, film_name, film_date, proceeds, grade) VALUES (%s, %s, %s, %s, %s)
'''
query_3 = '''
DELETE FROM genre
'''
query_4 = '''
INSERT INTO genre (genre_id, genre_name) VALUES (%s, %s)
'''
query_5 = '''
DELETE FROM script
'''
query_6 = '''
INSERT INTO script (script_id, scene, script_text, film_id, genre_id) VALUES (%s, %s, %s, %s, %s)
'''
conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_1)
    cur.execute(query_3)
    cur.execute(query_5)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            values1 = (idx+201, row['movie_title'], row['release_date'], row['total_gross'], round(random.uniform(1,10),1))
            cur.execute(query_2, values1)
            values2 = (idx+500001, row['genre'])
            cur.execute(query_4, values2)
            values3 = (idx, "scene" + str(idx), "text" + str(idx), idx + 201, idx + 500001)
            cur.execute(query_6, values3)

    conn.commit()