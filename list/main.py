# Importar las librerías del cliente de Google Cloud 
from google.cloud import datastore
from flask import jsonify


# Instanciación del cliente de conexión
datastore_client = datastore.Client()

# Tipo de la entidad que se trabaja
kind = "Heroe"

def list(request):
    """Definición de la función invocada por la Cloud Function. 
    Muestra la infromación de todos los héroes registrados en el sistema
    
    Args:
        request (flask.Request): Objeto con la infromación de la petición.
    Returns:
        Lista con la información de los héroes registrados en el sistema
        Para la respuesta se utiliza `flask.jsonify`
    """

    # Creación de un objeto para consumo de de la entidad a trabajar
    query = datastore_client.query(kind=kind)
    results = list(query.fetch())

    return jsonify(results)
