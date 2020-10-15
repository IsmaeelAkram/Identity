import os
from postgres import Postgres
import chalk

db = Postgres(url=os.getenv("postgres_connection_string"))
db.run("""
CREATE TABLE IF NOT EXISTS identities (
    user_id BIGINT PRIMARY KEY,
    name TEXT,
    socials TEXT,
    birthday TEXT
)
""")
print(chalk.green("Created identities table if doesn't exist."))

def get_user_identity(user_id):
    user_identity = db.one(f"SELECT * from identities WHERE user_id=%(userid)s", userid=user_id)
    return user_identity


def delete_identity(user_id):
    try:
        db.run(f"DELETE FROM identities WHERE user_id=%(userid)s", userid=user_id)
        return True
    except Exception as e:
        print(e)
        return e

def create_identity(user_id, name, socials, birthday):
    try:
        db.run(f"INSERT INTO identities VALUES (%(userid)s, %(name)s, %(socials)s, %(birthday)s)", userid=user_id, name=name, socials=socials, birthday=birthday)
        return True
    except Exception as e:
        print(e)
        return e