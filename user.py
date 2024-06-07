from passlib.context import CryptContext
import mariadb
import sys

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User:
    username: str
    hashed_password: str

    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.hashed_password)


def authenticate_user(username: str, password: str) -> User:
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

    # Ejecutar consulta
    cur.execute("SELECT * from login WHERE user = %s", (username,))

    # Recuperar resultados
    resultados = cur.fetchall()
    encontrado = False
    for usuario, passw in resultados:
        if username == usuario and password == passw: encontrado = True

    # Cerrar la conexión
    conn.close()

    return encontrado
