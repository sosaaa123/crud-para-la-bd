import psycopg2
import datetime #Para convertir variables a tipo date para postgre
from datetime import datetime


#Van a haber dos conexiones por las 2 bd que existen



#Preguntar a santi por una funcion que verifique la cantidad de cupos de cada viaje y en caso de que sea 0 (eliminar viaje? dar de baja?)
#Eliminar de la base de datos cuando llegue a 0

#Si se quisiera actualizar o modificar algun viaje (hacer metodo para cada campo?)

dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns) 
cursor = conexionViajes.cursor()


#Funcion para transformar los datos de la consulta en Json para enviar.
#Convierte la respuesta de la tabla viaje simple (TVS) a diccionario
def convertirDatosTVS(respuesta):
    dicConvertido = []
    for item in respuesta:
        dicConvertido.append({"Nombre": item[0], "Descripcion": item[1],"Precio":item[2] ,"Origen": item[3],"Destino": item[4], "Transporte": item[5], "Fecha": item[6], "Hora": item[7], "Cupos": item[8], "Duracion": item[9], "Tipo_de_viaje": item[10]})

        return dicConvertido

#Convierte la respuesta de la tabla paquete de viajes (TVS) a diccionario
def convertirDatosTPV(respuesta):
    dicConvertido = []
    for item in respuesta:
        dicConvertido.append({"Nombre": item[0], "Precio": item[1], "Origen": item[2],"Destino": item[3], "Estadia": item[4], "Tipo": item[5], "Descripcion": item[6], "Cupos": item[7], "Duracion": item[8], "Tipo_de_viaje": item[9], "Hora": item[10]})

        return  dicConvertido





#-------- SANTIAGO ATENTO #f9ed32 -------------
#Funcion para traer todos los datos visibles para el Frontened 1

def verViajesSimples():
    #falta el precio revisar cuando santi actualice
    cursor.execute("SELECT nombre, descripcion, precio, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje FROM viaje_simple")
    respuesta = cursor.execute.fetchall()

    nrepuesta = convertirDatos(respuesta)

    return nrepuesta


def verPaquetedeViajes():
    #En la tabla paquete de viaje falta descripcion.
    cursor.execute("SELECT nombre, precio, origen, destino, estadia, tipo, descripcion, cupos, duracion_aprox, hora tipo FROM paquete_de_viajes")
    respuesta = cursor.execute.fetchall()

    nrepuesta = convertirDatos(respuesta)

    return nrepuesta


#Funcion especifica ver excursiones dw un viaje en especifico
def verExcursiones(codigoViaje):
    cursor.execute("SELECT * FROM excursiones WHERE ID")



#Supongamos que se quiera hacer una compra de boleto
#Primero se debe hacer una verificacion si existe ese usuario
#Recibe el codigo de viaje que ha seleccionado el usuario.
#Para tabla de viajes simple



def restarCupoTVS(codigoViaje, cantidad):
    cursor.execute("SELECT cupo FROM viaje_simple WHERE codigo = %s", (codigoViaje))
    ncupos = cursor.fetchall()

    #----------------- Aca tendria que revisar que valor me trae ncupos ------------
    if (codigoViaje > ncupos or codigoDeViaje == ncupos):
        cursor.execute("UPDATE viaje_simple SET cupos = cupos - %s WHERE codigo = %s",(cantidad, codigoViaje))
        conexionViajes.commit()

        return {"Mensaje": "Cupo decrementado exitosamente"}

    else:
        return {"Mensaje": "No quedan cupos disponibles, no se puede realizar la compra"}


#Para tabla de paquetes de viajes
def restarCupoTPV(codigoViaje, cantidad):
    cursor.execute("UPDATE paquete_de_viajes SET cupos = cupos - %s WHERE codigo = %s",(cantidad, codigoViaje))
    conexionViajes.commit()

    return {"Mensaje": "Cupo decrementado"}



#Metodo que solo aplicaria para el frontened del admin
def agregarViajeSimple(nombre, descripcion, precio, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje):
    cursor.execute("INSERT INTO viaje_simple (codigo, nombre, descripcion, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (codigo, nombre, descripcion, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje) )
    conexionViajes.commit()

    return {"Mensaje": "Nuevo viaje simple agregado"}


#Metodo que solo aplicaria para el frontened del admin
def agregarPaquetedeViaje(codigo, nombre, precio, origen, destino, estadia, tipo, hora, descripcion, cupos, duracion_aprox, hora):
    cursor.execute("INSERT INTO paquete_de_viajes (codigo, nombre, precio, origen, destino, estadia, tipo, hora, cupos, duracion_aprox) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", () )
    conexionViajes.commit()
    #--------- Revisar porque esta incopleta hay que ver que metodos usar para ingresar excursiones -------- 

    return {"Mensaje": "Nuevo viaje simple agregado"}


def quitarViajesimple(codigoDeViaje):
    cursor.execute("DELETE * FROM viaje_simple WHERE codigo = %s", (codigoDeViaje))
    conexionViajes.commit()

    return {"Mensaje":"Viaje borrado exitosamente"}



def quitarPaquetedeViaje(codigoDeViaje):
    cursor.execute("DELETE * FROM paquete_de_viaje WHERE codigo = %s", (codigoDeViaje))
    conexionViajes.commit()

    return {"Mensaje":"Viaje borrado exitosamente"}



#Hacer una funcion que verifique constantemente que los viajes no tenga 0 cupos porque si es 0 eliminamos el registro de la bd, siempre se ejuctaria i guess
def consultarCuposTVS(codigoViaje):
    cursor.execute("SELECT cupo FROM viaje_simple WHERE codigo = %s", (codigoViaje) )
    ncupos = cursor.fetchall()

    if (ncupos == 0):
        quitarViajesimple(codigoViaje)
    else:
        return {"Mensaje":"Sigue con cupos disponibles."}

#Lo mismo para la tabla paquetes_de_viajes
def consultarCuposTPV(codigoViaje):
    cursor.execute("SELECT cupo FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje) )
    ncupos = cursor.fetchall()

    if (ncupos == 0):
        quitarPaquetedeViaje(codigoViaje)
    else:
        return {"Mensaje":"Sigue con cupos disponibles."}

#Funcion Para hacer tipo dae
def convertirDate(fecha):
    #24/10/2006
    nfecha = datetime.strptime( fecha, "%d/%m/%y").date()
    nfecha = nfecha.strftime("%d/%m/%Y")#La pongo en notacion nuestra
    return nfecha 

def convertirHora(hora):
    #La hora debe estar pasada de esta manera "10:00" como un string.
    nhora = datetime.strptime(hora, "%H:%M").time()
    return  nhora

#agregarViajeSimple("3444Neuquen","Neuquen", "Viaje de junio a Neuquen", 28000, "Buenos Aires, Aeropuerto", "Neuquen", "Avion", convertirDate("24/10/2025"), convertirHora("10:00") , 30, , "Ida y Vuelta")



print(convertirHora("10:00"))
print(convertirDate("24/10/06"))






















