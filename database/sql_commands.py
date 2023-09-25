import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("telegram_users.sqlite3")
        self.cursor = self.connection.cursor()


    def sql_create_table(self):
        if self.connection:
            print('Connected')
        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_FORM_TABLE_QUERY)

    def sql_insert_user_command(self, telegram_id, username, first_name,
                                last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name)
        )
        self.connection.commit()

    def sql_insert_user_form_command(self, telegram_id, nickname, bio,
                                     age, occupation, married, photo):
        self.cursor.execute(
            sql_queries.INSERT_USER_FORM_QUERY,
            (None, telegram_id, nickname, bio, age, occupation, married, photo,)
        )
        self.connection.commit()

    def sql_select_user_form_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "occupation": row[5],
            "married": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_select_id(self, username):
        return self.cursor.execute(sql_queries.SELECT_ID, (username,)).fetchall()