# Funciones y datastore

## Objetivos

- Aplicar los conocimientos y conceptos de aplicaciones serverless vistos en clase.
- Crear y publicar aplicaciones Cloud Function en GCP
- Aprender el manejo básico del servicio de datastore y como integrarlo a funciones en el cloud function

## Estructura de carpetas

En el proyecto encontrará tres carpetas principales:

- La carpeta `collections` en donde se encuentra la colección de Postman para poder realizar pruebas sobre las funciones publicadas
- La carpeta `crear` en donde se encuentra la implementación de la función que nos permitirá crear nuevos heroes 
- La carpeta `listar` en donde se encuentra la implementación de la función que nos dará la lista de los identificadores de héroes 

## Publicacion de la funciones 

Debe tener presente que las funciones se conectarán al Cloud Storage previamente creado. Para ello se configurará una variable de entorno con el nombre del bucket. Es importante que remplace el nombre en el comando antes de publicarlo.

### Crear

Para poder publicar la función, debe abrir una consola de comandos en la ubicación donde descargamos el repositorio. Posteriormente, debe ejecutar los sigioentes comandos:

```console
cd crear
gcloud functions deploy funcion-heroes-datastore-crear --entry-point crear --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1
cd ..
```

En la consola deberá observar un mensaje de confirmación de creación de la función

### Listar

Para poder publicar la función, debe abrir una consola de comandos en la ubicación donde descargamos el repositorio. Posteriormente, debe ejecutar los sigioentes comandos:

```console
cd listar
gcloud functions deploy funcion-heroes-datastore-listar --entry-point listar --runtime python39 --trigger-http --allow-unauthenticated --memory 128MB --region us-central1 --timeout 60 --min-instances 0 --max-instances 1 
cd ..
```

En la consola deberá observar un mensaje de confirmación de creación de la función

