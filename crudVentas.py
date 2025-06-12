#La tabla que maneja este crud es Ventas
import psycopg2
from crudViajes import convertirDate, convertirHora

dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns) 
cursor = conexionViajes.cursor()

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

        return dicConvertido

def verVentas(respuesta):
    #En la tabla Ventas
    cursor.execute("SELECT * FROM ventas")
    respuesta = cursor.execute.fetchall()

    nrepuesta = convertirDatos(respuesta)

    return nrepuesta


def sumarVenta(vtas_id, fecha, hora, medio_de_pago, cuotas, cantidad, codigo_vs, codigo_pv, precio):
        fecha = convertirDate(fecha)
        hora = convertirHora(hora)
        cursor.execute("INSERT INTO ventas (vtas_id, fecha, hora, medio_de_pago, cuotas, cantidad, codigo_vs, codigo_pv, precio) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (vtas_id, fecha, hora, medio_de_pago, cuotas, cantidad,codigo_vs, codigo_pv, precio))
        conexionViajes.commit()

        return {"Mensaje":"Venta sumada"}


print(sumarVenta(1,"27/10/25","10:10","Transferncia", False, 2, 679848, None, 56000))




    




