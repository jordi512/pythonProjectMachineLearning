import pymongo
from passlib.context import CryptContext
import mariadb
import sys

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#DEPRECATED
class User:
    username: str
    hashed_password: str

    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.hashed_password)


#DEPRECATED
def authenticate_user_mariadb(username: str, password: str) -> User:
    # Implement user database lookup and password verification using 'verify_password'

    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="root",
            password="nueva_contraseña",
            host="localhost",
            port=3306,
            database="python"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()

    #Execute SQL
    cur.execute("SELECT * from login WHERE user = %s", (username,))

    #See results
    resultados = cur.fetchall()
    encontrado = False
    for usuario, passw in resultados:
        if username == usuario and password == passw: encontrado = True

    #Close connection
    conn.close()

    return encontrado


def authenticate_user(username: str, password: str) -> bool:
    # Connect and access to mongodb database
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["python"]
    collection = db["user"]

    #Find in the database
    documento = collection.find_one({"username": username, "password": password})

    # Verify if the user exists
    if documento is not None:
        return True
    else:
        return False