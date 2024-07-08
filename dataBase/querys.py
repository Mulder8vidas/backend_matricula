import hashlib

import mysql.connector
config = {
    'user': 'Usuario',
    'password': 'admin1',
    'host': '127.0.0.1',
    'database': 'matriculaDB',
    'raise_on_warnings': True
}
def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register(username, password):
    """Registrar un nuevo usuario."""
    hashed_password = hash_password(password)
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False

def registrarAlumno(nombres, apellidos,fecha,dni,sexo,apoderado,telefono,direccion,nivel,grado):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alumnos (Nombres, Apellidos, FechaNacimiento, DNI, Sexo, Apoderado, NroTelefono, Direccion,Nivel,Grado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",params=(nombres,apellidos,fecha,dni,sexo,apoderado,telefono,direccion,nivel,grado))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False

def editarAlumno(id,nombres, apellidos,dni,sexo,apoderado,telefono,direccion,nivel,grado):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("UPDATE alumnos SET Nombres=%s, Apellidos=%s, DNI=%s, Sexo=%s, Apoderado=%s, NroTelefono=%s, Direccion=%s,Nivel=%s,Grado=%s WHERE id=%s",params=(nombres,apellidos,dni,sexo,apoderado,telefono,direccion,nivel,grado,id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False

def eliminarAlumno(id):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False
def eliminarAula(id):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM aulas WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False




def obtenerAlumnosxAula(id):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select al.* from alumnos as al inner join aulas as a on a.grado=al.Grado and a.Nivel=al.nivel where a.id=%s" , (id,))
        alumnos=cursor.fetchall()
        return alumnos


    except mysql.connector.Error as err:
        print("Error:", err)


def obtenerAlumnos():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ALUMNOS")
        alumnos=cursor.fetchall()
        return alumnos


    except mysql.connector.Error as err:
        print("Error:", err)

def obtenerAulas():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT a.*,(select count(*) from alumnos as al where al.Grado=a.grado and al.Nivel=a.nivel) as cantidad FROM aulas as a;")
        aulas=cursor.fetchall()
        return aulas
    except mysql.connector.Error as err:
        print("ta mal",err)

def login(username, password):
    """Autenticar un usuario."""
    hashed_password = hash_password(password)
    print(hashed_password)
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, hashed_password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return user
        else:
            return None
    except mysql.connector.Error as err:
        print("Error:", err)
        return None
