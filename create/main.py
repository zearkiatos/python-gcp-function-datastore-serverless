# Importar las librerías del cliente de Google Cloud 
from google.cloud import datastore
from flask import jsonify


# Instanciación del cliente de conexión
datastore_client = datastore.Client()

# Tipo de la entidad que se trabaja
kind = "Heroe"

def create(request):
    """Definición de la función invocada por la Cloud Function. 
    La función crea a un nuevo héroe con la información especificada en el cuerpo
    
    Args:
        request (flask.Request): Objeto con la infromación de la petición.
    Returns:
        Representación en formato JSON de la información del nuevo héroe
        Retorna código http 400 en caso de no poder crear el héroe
        Para la respuesta se utiliza `flask.jsonify`
    """
    data = request.get_json(force=True)
    if data == None: #Si el objeto está vácio se retorna error
        return "No se recibe información", 400
    try:
        # Asignación de una llave para la entidad en Datastore
        task_key = datastore_client.key(kind)

        # Crear los valores de la nueva entidad
        new_heroe = datastore.Entity(key=task_key)
        new_heroe["Name"] = try_get_value(data, 'Name')
        new_heroe["Gender"] = try_get_value(data, 'Gender')
        new_heroe["Eye color"] = try_get_value(data, 'Eye color')
        new_heroe["Race"] = try_get_value(data, 'Race')
        new_heroe["Hair color"] = try_get_value(data, 'Hair color')
        new_heroe["Height"] = try_get_value(data, 'Height')
        new_heroe["Publisher"] = try_get_value(data, 'Publisher')
        new_heroe["Skin color"] = try_get_value(data, 'Skin color')
        new_heroe["Alignment"] = try_get_value(data, 'Alignment')
        new_heroe["Weight"] = try_get_value(data, 'Weight')

        # Guarda la nueva entidad en datastore
        datastore_client.put(new_heroe)

        return jsonify(new_heroe)
    except Exception as e: #Si el objeto no tiene todas las propiedades esperadas se retorna error
        return str(e), 400

def try_get_value(data, key):
    """Obtiene el valor de una propiedad especificada de un objeto JSON
    
    Args:
        data (dict): Objeto JSON de donde se obtiene las propiedades
        key (str): Nombre de la propiedad a obtener
    Returns:
        Retorna el valor de la propiedad especificada.
    Exception:
        Si la propiedad no existe en el objeto especificado
    """
    if key in data:
        return data[key]
    else:
        raise Exception('No se recibe la propiedad: '+key)