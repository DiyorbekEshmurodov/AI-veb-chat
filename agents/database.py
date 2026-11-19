import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    return connection

if __name__ == "__main__":
    try:
        with get_connection() as conn:
            print("Connection is activate with PosterSql!")

            result = conn.execute(
                "SELECT current_database();"
            )

            print("Connection DB: ", result.fetchone()[0])

    except Exception as error:
        print("DB error: ", error)