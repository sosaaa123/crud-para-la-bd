import psycopg2


dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns) 
cursor = conexionViajes.cursor()



#Preguntar si la excursiones ya vienen incluidas en el paquete de viaje o hay que comprar.

def agregarExcursiones(excursion_id, nombre, inicio, final, descripcion, lugar):
    cursor.execute("INSERT INTO excursiones (excursion_id, nombre, inicio, final, descripcion, lugar) VALUES(%s,%s,%s,%s,%s,%s)", (excursion_id, nombre, inicio, final, descripcion, lugar))
    conexionViajes.commit()

    return {"Mensaje": "Se ha agregado la excursion exitosamente"}

def eliminarExcursion(excursion_id):
    cursor.execute("DELETE FROM excursiones WHERE excursion_id = %s", (excursion_id,))
    conexionViajes.commit()

    return {"Mensaje": "Borrado exitosamente"}







"""print(agregarExcursiones(2, "Excursion a Parque de Diversiones", "8:00", "20:00", "Todo el dia, excursion y dia de familia en los asombrosos juegos del parque de diversion ChasquiBoom.", "ChasquiBoom"))
print(agregarExcursiones(3, "Excursion Lago El Nahuelito", "9:00", "12:00", "Excursion corta, vamos a la hermosa laguna EL Nahuelito, ideal para toda la familia.", "Laguna El Nauelito"))
print(agregarExcursiones(4, "Museo Historico de la Nouvelle Vage", "8:00", "16:00", "Recorrido guiado por el museo de la Nouvelle Vague, durante mañana y tarde.", "Museo Nouvelle Vague"))
print(agregarExcursiones(5, "Reserva Natural Euroean", "8:00", "19:00", "Paseamos por la nueva reserva natural Euroean. Visita guiada y completa.", "Reserva Natural Euroean"))
print(agregarExcursiones(6, "Monumentos y Peculiaridades", "8:00", "13:00", "Tour touristico por la ciudad recorriendo monumenots, esculturas y lugares unicos de la ciudad, charlando con nativos.", "Ciudad"))"""