import sqlite3


class Database():
    """Handles everything concerning the database.

    Attributes:
        db_name (string): name of the SQLite database.
    """

    def __init__(self, db_name="newspaper_db"):
        self.db_name = db_name
        self._create_db()

    def _create_db(self):
        """Creates database and articles' table if they don't exist."""
        db = sqlite3.connect(self.db_name)
        cursor = db.cursor()

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS articles(id_art INTEGER
                       PRIMARY KEY AUTOINCREMENT UNIQUE, url TEXT, source TEXT,
                       author TEXT, title TEXT, theme TEXT, description TEXT,
                       date_published DATE, body TEXT)
                       ''')

        cursor.close()
        db.commit()
        db.close()

    def insert_article(self, url, source, author, title, theme, description,
                       date_published, body):
        """Inserts an article in the database."""
        db = sqlite3.connect(self.db_name)
        cursor = db.cursor()

        cursor.execute('''
                       INSERT INTO articles(url, source, author, title, theme,
                       description, date_published, body)
                       VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                       ''', [url, source, author, title, theme, description,
                       date_published, body])
        cursor.close()
        db.commit()
        db.close()
