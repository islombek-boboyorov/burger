from django.db import connection
from contextlib import closing


def get_recipe():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from spicyo_recipes""")
        recipes = dict_fetchall(cursor)
        return recipes


def get_about():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from spicyo_about""")
        abouts = dict_fetchall(cursor)
        return abouts


def get_blog():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from spicyo_blog""")
        blogs = dict_fetchall(cursor)
        return blogs


def get_client():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from spicyo_client""")
        clients = dict_fetchall(cursor)
        return clients


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns,row))
            for row in cursor.fetchall()]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


