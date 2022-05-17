from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Paises

from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de
# la entidad docentes
paises = session.query(Paises).all() # [docente1, docente2, docente3]

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de todos los países del continete Americano")
for s in paises:
    print("%s" % (s))
    print("---------")

pais = session.query(Paises).filter(Paises.continente=='SA').all()

