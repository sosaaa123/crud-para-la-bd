import psycopg2

dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns) 
cursor = conexionViajes.cursor()


def crearCliente():
    cursor.execute("INSERT INTO clientes () VALUES()",())
    cursor.commit()

    return {"Mensaje": "Se ha cargado un nuevo cliente"}


def verClientes():
    cursor.execute("SELECT * FROM clientes")