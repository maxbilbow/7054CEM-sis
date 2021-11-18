from api_server import db
from core.model.user import User


class UserRepository:

    @staticmethod
    def insert_user(email: str, password_hash: str):
        con = db.connect()
        cur = con.cursor()
        try:
            cur.execute('INSERT INTO user (email, password_hash)VALUES( %s, %s)', (email, password_hash))
            con.commit()
            return User(id=cur.lastrowid, email=email, password_hash=password_hash)
        finally:
            cur.close()
            con.close()
