from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base import Paises
import requests
import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()


# leer el archivo de datos

#archivo = open("data/data-personas-001.json", "r")
archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

#datos_json =  json.load(archivo) # paso los datos del archivo a json
doc = archivo.json()

#documentos = datos_json["docs"]

for d in doc:
    print(d)
    print(len(d.keys()))
    p = Paises(nombrePais=d['CLDR display name'], capital=d['Capital'], continente=d['Continente'], \
            dial=d['Dial'], geoname=['Geoname ID'], itu=['ITU'], lenguaje=['Languages'], \
            independiente=['is_independent'])
    session.add(d)

# confirmar transacciones

session.commit()
