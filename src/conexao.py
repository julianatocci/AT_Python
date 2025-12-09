from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from caminhos_constantes import BANCO

engine = create_engine(f"sqlite:///{BANCO}", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
