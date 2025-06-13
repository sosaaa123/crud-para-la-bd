import psycopg2

dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns) 
cursor = conexionViajes.cursor()

def crearAdminsitradores(ua_id, nombre, apellido, contraseña, correo_electronico):
    cursor.execute("INSERT INTO usuario_administrativo (ua_id, nombre, apellido, contraseña, correo_electronico) VALUES(%s,%s,%s,%s,%s)", (ua_id, nombre, apellido, contraseña, correo_electronico))
    conexionViajes.commit()
    
    return {"Mensaje":"Se ha creado un nuevo administrador"}


def borrarAdmin(ua_id):
    cursor.execute("DELETE FROM usuario_administrativo WHERE ua_id = %s",(ua_id,))
    conexionViajes.commit()

    return {"Mensaje": "Se ha eliminado un administrador"}


