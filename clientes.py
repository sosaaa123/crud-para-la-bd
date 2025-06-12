import psycopg2

dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns) 
cursor = conexionViajes.cursor()

#Es nueva, terminada
def crearCliente(uc_id, nombre, apellido,contraseña, correo_electronico):
    cursor.execute("INSERT INTO usuario_comun (uc_id, nombre, apellido, contraseña, correo_electronico) VALUES(%s,%s,%s,%s,%s)",(uc_id, nombre, apellido,contraseña, correo_electronico))
    conexionViajes.commit()

    return {"Mensaje": "Se ha cargado un nuevo cliente"}


""""print(crearCliente(3, "Mariano", "Eseiza", "ok1244" , "marinaanoa@gmail.com"))
print(crearCliente(4, "Ezequiel", "Gutierrez", "344sdfa" , "oezee33@gmail.com"))W
print(crearCliente(5, "Jaime", "Arias", "jaimelepro12" , "jaime123@gmail.com"))""""


#No esta hecha
def verClientes():
    cursor.execute("SELECT * FROM clientes")
    respuesta = cursor.fetchall()
    dicConvertido = []

    
