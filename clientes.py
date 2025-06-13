import psycopg2

dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns) 
cursor = conexionViajes.cursor()

#Es nueva, terminada
def crearCliente(uc_id, nombre, apellido,contraseña, correo_electronico):
    cursor.execute("INSERT INTO usuario_comun (uc_id, nombre, apellido, contraseña, correo_electronico) VALUES(%s,%s,%s,%s,%s)",(uc_id, nombre, apellido,contraseña, correo_electronico))
    conexionViajes.commit()

    return {"Mensaje": "Se ha cargado un nuevo cliente"}


"""print(crearCliente(3, "Mariano", "Eseiza", "ok1244" , "marinaanoa@gmail.com"))
print(crearCliente(4, "Ezequiel", "Gutierrez", "344sdfa" , "oezee33@gmail.com"))W
print(crearCliente(5, "Jaime", "Arias", "jaimelepro12" , "jaime123@gmail.com"))"""


#Hecha, anda
def verClientes():
    cursor.execute("SELECT * FROM usuario_comun")
    respuesta = cursor.fetchall()
    usuarios = []
    for usuario in respuesta:
        dicConvertido = []
        dicConvertido.append(
            {
                "Usuario id": usuario[0],
                "Nombre": usuario[1],
                "Apellido": usuario[2],
                "Contraseña": usuario[3],
                "Email": usuario[4]
                
                
            }
        )

        usuarios.append(dicConvertido)

    return usuarios

#Nueva, anda
def verClienteId(uc_id):
    cursor.execute("SELECT * FROM usuario_comun WHERE uc_id = %s", (uc_id,))
    respuesta = cursor.fetchall()
    dicConvertido = []
    dicConvertido.append({

                "Usuario id": respuesta[0][0],
                "Nombre": respuesta[0][1],
                "Apellido": respuesta[0][2],
                "Contraseña": respuesta[0][3],
                "Email": respuesta[0][4]
        
    })

    return dicConvertido

#Nueva, anda
def eliminarUsuario(uc_id):
    cursor.execute("DELETE FROM usuario_comun WHERE uc_Id = %s", (uc_id,))
    conexionViajes.commit()

    return {"Mensaje":"Se ha eliminado un usuario correctamente"}









    
