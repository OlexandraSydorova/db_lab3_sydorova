import psycopg2
import matplotlib.pyplot as plt

username = 'Sydorova_Olexandra'
password = '111'
database = 'Sydorova_Olexandra_lr2_DB'
host = 'localhost'
port = '5432'

query_1 = '''
create view FilmProceeds as
SELECT trim(film_name), proceeds FROM disney_film
'''
query_2 = '''
create view FrequencyOfGenres as
SELECT trim(genre_name), COUNT(script.genre_id) FROM genre LEFT JOIN script using(genre_id) GROUP BY genre_id
'''

query_3 = '''
create view Rating as
SELECT trim(film_name), grade FROM disney_film
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(con))

with con:

    cur = con.cursor()
    cur.execute('DROP VIEW IF EXISTS FilmProceeds')
    film_name = []
    proceeds = []
    cur.execute(query_1)
    cur.execute('SELECT * FROM FilmProceeds')
    for row in cur:
        proceeds.append(row[1])
        film_name.append(row[0])
    fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(5*3.13,2*3.13))
    ax1.bar(film_name, proceeds, width=0.5)
    ax1.set_title('Збір з фільмів')
    ax1.set_xticklabels(film_name, rotation=10)
    ax1.set_ylabel('Сума, $')

    cur.execute('DROP VIEW IF EXISTS FrequencyOfGenres')
    genre_name = []
    genre_count = []
    cur.execute(query_2)
    cur.execute('SELECT * FROM FrequencyOfGenres')
    for row in cur:
        genre_count.append(row[1])
        genre_name.append(row[0])
    ax2.pie(genre_count, labels = genre_name, autopct='%1.1f%%')
    ax2.set_title('Частота жанрів')

    cur.execute('DROP VIEW IF EXISTS Rating')
    film_name = []
    grade = []
    cur.execute(query_3)
    cur.execute('SELECT * FROM Rating')
    for row in cur:
        grade.append(row[1])
        film_name.append(row[0])
    ax3.bar(film_name, grade, width=0.5)
    ax3.set_title('Рейтинг')
    ax3.set_xticklabels(film_name, rotation=10)
    ax3.set_ylabel('Оцінка з 10')
    plt.show()
