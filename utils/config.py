import os
import chalk
import mysql.connector

db = mysql.connector.connect(
    user=os.getenv("mysql_user"),
    password=os.getenv("mysql_pass"),
    host=os.getenv("mysql_host"),
    database='identity'
)
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS identities (
    user_id BIGINT PRIMARY KEY,
    name TEXT,
    socials TEXT,
    birthday TEXT
)
""")
print(chalk.green("Created identities table if doesn't exist."))

def get_user_identity(user_id):
    cursor.execute(f"SELECT * from identities WHERE user_id=(%s)", (user_id,))
    user_identity = cursor.fetchone()
    return user_identity


def delete_identity(user_id):
    try:
        cursor.execute(f"DELETE FROM identities WHERE user_id=(%s)", (user_id,))
        db.commit()
        return True
    except Exception as e:
        print(e)
        return e

def create_identity(user_id, name, socials, birthday):
    try:
        cursor.execute(f"INSERT INTO identities VALUES (%s, %s, %s, %s)", (user_id, name, socials, birthday))
        db.commit()
        return True
    except Exception as e:
        print(e)
        return e