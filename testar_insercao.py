from database import SessionLocal
from models import Categoria, Transacao
from datetime import date

db = SessionLocal()

# Criar uma categoria de teste
categoria_salario = Categoria(nome="Salário", tipo="receita")
db.add(categoria_salario)
db.commit()  # salva no banco de verdade
db.refresh(categoria_salario)  # atualiza o objeto com o ID gerado pelo banco

# Criar uma transação ligada a essa categoria
transacao_teste = Transacao(
    descricao="Salário de Agosto",
    valor=3000.00,
    data=date(2026, 8, 27),
    categoria_id=categoria_salario.id
)
db.add(transacao_teste)
db.commit()

print(f"Categoria criada com ID: {categoria_salario.id}")
print(f"Transação criada com ID: {transacao_teste.id}")

db.close()