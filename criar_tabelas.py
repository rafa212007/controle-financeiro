from database import engine, Base
from models import Transacao, Usuario

Base.metadata.create_all(engine)

print("Tabelas criadas com sucesso!")