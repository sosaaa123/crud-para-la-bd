#La tabla que maneja este crud es Ventas
import psycopg2
from crudViajes import convertirDate, convertirHora



#Convertir a diccionario los datos de la Tabla Ventas
#Preguntar a santi porque ventas no tiene usuario id.
def convertirDatosVentas(respuesta):
    dicConvertido = []
    fecha = item[1]
    fecha = fecha.strftime("%Y-%m-%d")
    hora = item[2]
    hora = hora.strftime("%H:%M:%S")

    for item in respuesta:
        if(item[6]):#Si no esta vacia quiere decir que la venta es de un viaje simple(revisar orden de campos en la tabla clientes)
            codigo_de_viaje = item[6]
            tipo = "Viaje Simple"
        else:#Si item[6] esta vacio quiere decir que es un paquete de viaje(revisar orden de capos en la taba cliente)
            codigo_de_viaje = item[7]
            tipo = "Paquete de Viaje"
        #Consultar si es necesario agregar a la tabla venta un campo que indique si la venta es de un paquete de viajes o de un viaje simple
        dicConvertido.append({
            
                            "Id Venta": item[0],
                             "Fecha": fecha,
                             "Hora": hora,
                             "Medio de pago": item[3],
                             "Cuotas": item[4], 
                             "Cantidad": item[5], 
                             "Codigo de viaje": codigo_de_viaje, 
                             "Tipo": tipo, 
                             "Precio": item[8]})

        return = dicConvertido

def verVentas(respuesta):
    #En la tabla Ventas
    cursor.execute("SELECT * FROM ventas")
    respuesta = cursor.execute.fetchall()

    nrepuesta = convertirDatos(respuesta)

    return nrepuesta


def sumarVenta(id_viaje, cantidad):
    cursor.execute("INSERT INTO ventas (vtas_id, fecha, hora, medio_de_pago, cuotas, cantidad, codigo_pv, precio)")





    




