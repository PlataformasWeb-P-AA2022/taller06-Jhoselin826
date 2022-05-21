from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Paises
engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

pais = session.query(Paises).filter(or_(Paises.cldr_display_name.like('%uador%'), Paises.capital.like('%ito'))).all()
print(pais)
