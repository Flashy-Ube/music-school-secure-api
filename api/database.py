#api/database.py

import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
            host="localhost",
            database="music_school",
            user="postgres",
            password="SL95cut!"
            cursor_factory=RealDictCursor
    )

