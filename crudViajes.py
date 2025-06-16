import psycopg2
import datetime #Para convertir variables a tipo date para postgre
from crudExcursiones import paqueteViajesExcursion
from datetime import datetime


dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns) 
cursor = conexionViajes.cursor()

#Convierte la respuesta de la tabla viaje simple (TVS) a diccionario

def convertirDatosTVS(respuesta):
    
    registroListas = []
    for item in respuesta:
        dicConvertido = []
        fecha = item[7]
        fecha = fecha.strftime("%Y-%m-%d")
        hora = item[8]
        hora = hora.strftime("%H:%M:%S")
           

        dicConvertido.append({"Codigo": item[0],
                              "Nombre": item[1],
                              "Descripcion": item[2],
                              "Precio":item[3] ,
                              "Origen": item[4],
                              "Destino": item[5],
                              "Transporte": item[6], 
                               "Fecha": fecha,
                               "Hora": hora,
                               "Cupos": item[9],
                               "Duracion": item[10],
                               "Tipo_de_viaje": item[11],
                               "Estado": item[12]})

        #dicConvertido.append()
        registroListas.append(dicConvertido)

    return registroListas
    


#Convierte la respuesta de la tabla paquete de viajes (TVS) a diccionario
def convertirDatosTPV(respuesta):
    registroListas = []
    for item in respuesta:
        dicConvertido = []
        fecha = item[12]
        fecha = fecha.strftime("%Y-%m-%d")
        hora = item[11]
        hora = hora.strftime("%H:%M:%S")
        dicConvertido.append({
                              "Codigo": item[0],
                              "Nombre": item[1],
                              "Precio": item[2],
                              "Origen": item[3],
                              "Destino": item[4],
                              "Estadia": item[5],
                              "Tipo": item[6],
                              "Descripcion": item[7],
                              "Cupos": item[8], 
                              "Duracion": item[9],
                              "Tipo_de_viaje": item[10],
                              "Hora": hora,
                              "Fecha": fecha,
                              "Estado": item[13]

                              })

        registroListas.append(dicConvertido)
    return registroListas



def verViajesSimples():

    cursor.execute("SELECT * FROM viaje_simple")
    respuesta = cursor.fetchall()
    nrepuesta = convertirDatosTVS(respuesta)

    return nrepuesta


def verPaquetedeViajes():
    cursor.execute("SELECT * FROM paquete_de_viajes")
    respuesta = cursor.fetchall()

    nrepuesta = convertirDatosTPV(respuesta)

    return nrepuesta


#Supongamos que se quiera hacer una compra de boleto
#Primero se debe hacer una verificacion si existe ese usuario
#Recibe el codigo de viaje que ha seleccionado el usuario.
#Para tabla de viajes simple

def restarCupoTVS(codigoViaje, cantidad):
    cursor.execute("SELECT cupos FROM viaje_simple WHERE codigo = %s", (codigoViaje,))
    ncupos = cursor.fetchall()

    if (cantidad < ncupos[0][0] or cantidad == ncupos[0][0]):
        cursor.execute("UPDATE viaje_simple SET cupos = cupos - %s WHERE codigo = %s",(cantidad, codigoViaje))
        conexionViajes.commit()

        return {"Mensaje": "Cupo decrementado exitosamente"}

    else:
        return {"Mensaje": "No quedan cupos disponibles, no se puede realizar la compra"}




#Para tabla de paquetes de viajes
def restarCupoTPV(codigoViaje, cantidad):

    cursor.execute("SELECT cupos FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje,))
    ncupos = cursor.fetchall()

    if (cantidad < ncupos[0][0] or cantidad == ncupos[0][0]):
        cursor.execute("UPDATE paquete_de_viajes SET cupos = cupos - %s WHERE codigo = %s",(cantidad, codigoViaje))
        conexionViajes.commit()

        return {"Mensaje": "Cupo decrementado exitosamente"}

    else:
        return {"Mensaje": "No quedan cupos disponibles o no hay para esa cantidad, no se puede realizar la compra"}


#Funcion Para hacer tipo date
def convertirDate(fecha):
    #La fecha debe estar pasada de esta manera 24/10/06
    nfecha = datetime.strptime( fecha, "%d/%m/%y").date()
    return nfecha 

def convertirHora(hora):
    #La hora debe estar pasada de esta manera "10:00" como un string.
    nhora = datetime.strptime(hora, "%H:%M").time()
    return  nhora



#Metodo que solo aplicaria para el frontened del admin

def agregarViajeSimple(codigo, nombre, descripcion, precio, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje, estado):
    hora = convertirHora(hora)
    fecha = convertirDate(fecha)
    cursor.execute("INSERT INTO viaje_simple (codigo, nombre, descripcion, precio, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje, estado) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (codigo, nombre, descripcion, precio, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje, estado))
    
    conexionViajes.commit()

    return {"Mensaje": "Nuevo viaje simple agregado"}



#Metodo que solo aplicaria para el frontened del admin
#Santi no me mates, 01:01hrs!!!
def agregarPaquetedeViaje(codigo, nombre, precio, origen, destino, estadia, tipo, descripcion, cupos, duracion, tipo_de_viaje, hora, fecha, estado):
    hora = convertirHora(hora)
    fecha = convertirDate(fecha)
    cursor.execute("INSERT INTO paquete_de_viajes (codigo, nombre, precio, origen, destino, estadia, tipo, descripcion, cupos, duracion, tipo_de_viaje, hora, fecha, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (codigo, nombre, precio, origen, destino, estadia, tipo, descripcion, cupos, duracion, tipo_de_viaje, hora, fecha, estado) )
    conexionViajes.commit()
    

    return {"Mensaje": "Nuevo paquete de viaje"}


def quitarViajesimple(codigoDeViaje):
    cursor.execute("DELETE FROM viaje_simple WHERE codigo = %s", (codigoDeViaje,))
    conexionViajes.commit()

    return {"Mensaje":"Viaje borrado exitosamente"}



def quitarPaquetedeViaje(codigoDeViaje):
    cursor.execute("DELETE FROM paquete_de_viajes WHERE codigo = %s", (codigoDeViaje,))
    conexionViajes.commit()

    return {"Mensaje":"Viaje borrado exitosamente"}


#Hacer una funcion que verifique constantemente que los viajes no tenga 0 cupos porque si es 0 eliminamos el registro de la bd, siempre se ejuctaria i guess
#Podriamos agregar un campo que sea "Estado" y pongo si esta disponible o no
#Sirve asi no tendriamos que eliminar los viajes cuando cupos llegue a 0 si no que simplemente lo pasamos aa un estado no disponible.


#Ya anda 22:55hrs!!!
def consultarCuposTVS(codigoViaje):
    cursor.execute("SELECT cupos FROM viaje_simple WHERE codigo = %s", (codigoViaje,) )
    resultado = cursor.fetchone()
    cupos = resultado[0]

    if (cupos == 0):
        cursor.execute("UPDATE viaje_simple SET estado = %s WHERE codigo = %s",("No disponible", codigoViaje))
        conexionViajes.commit()
        return {"Mensaje":"Ya no tiene cupos disponibles."}
    else:
        cursor.execute("UPDATE paquete_de_viajes SET estado = %s WHERE codigo = %s",("disponible", codigoViaje))
        return {"Mensaje":"Sigue con cupos disponibles."}


#Ya anda 22:55hrs!!!
def consultarCuposTPV(codigoViaje):
    cursor.execute("SELECT cupos FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje,) )
    resultado = cursor.fetchone()
    cupos = resultado[0]

    if (cupos == 0):
        cursor.execute("UPDATE paquete_de_viajes SET estado = %s WHERE codigo = %s",("No disponible", codigoViaje))
        conexionViajes.commit()
        return {"Mensaje":"Ya no tiene cupos disponibles."}
    else:
        cursor.execute("UPDATE paquete_de_viajes SET estado = %s WHERE codigo = %s",("disponible", codigoViaje))
        return {"Mensaje":"Sigue con cupos disponibles."}




