from database import SessionLocal
from database.models import Cliente, Vendedor #, Produto, Pedido, ItemPedido
# from functions import get_int

def create_cliente():
    #Cod_clie deve ser gerado automatico, verificar esse erro(Criando o input apenas para o codigo funcionar agora)
    cod_clie = input("Digite o Codigo: ")
    nome = input("Digite o seu nome: ")
    endereco = input("Digite o seu endereco: ")
    cidade = input("Digite a sua cidade: ")
    cep = input("Digite o seu cep: ")
    uf = input("Digite o estado (UF): ")
    cnpj = input("Digite um CNPJ: ")
    ie = input("Digite um IE: ")

    db = SessionLocal()
    try:
        cliente = Cliente()
        cliente.nome_clie = nome
        cliente.cep = endereco
        cliente.cidade = cidade
        cliente.cep = cep
        cliente.uf = uf
        cliente.cnpj = cnpj
        cliente.ie = ie

        db.add(cliente)
        db.commit()
    finally:
        db.close()

    print(f"Ola {cliente.nome_clie}, CNPJ: {cliente.cnpj}, Seu registro no sistema: {cliente.cod_clie}")

def get_cliente(cod_clie):
    db = SessionLocal()
    try:
        cliente = db.query(Cliente).filter(Cliente.cod_clie == cod_clie).first()
        return cliente
    finally:
        db.close()

    
def create_vendedor():
    nome_ven = input("Digite o seu nome: ")
    db = SessionLocal()
    try:
        vendedor = Vendedor()
        vendedor.nome_ven = nome_ven
        vendedor.salario_fixo = None
        
        db.add(vendedor)
        db.commit()

    finally:
        db.close()

    print(f"Ola {vendedor.nome_ven}, Seu salario ainda e {vendedor.salario_fixo}, e a sua comissao e {vendedor.comissao}")


def get_vendedor(cod_ven):
    db = SessionLocal()
    try:
        vendedor = db.query(Vendedor).filter(Vendedor.cod_ven == cod_ven).first()
        return vendedor
    finally:
        db.close()


def coloca_salario_comissao(cod_ven):
    salario_fixo = input("Digite o Valor do salario: ")
    comissao = input("Digite a categoria da comissao: ")

    db = SessionLocal()

    try:
        vendedor = db.query(Vendedor).filter(Vendedor.cod_ven == cod_ven).first()

        if vendedor:
            vendedor.salario_fixo = salario_fixo
            vendedor.comissao = comissao

            db.add(vendedor)
            db.commit()
            print(f"Salário e comissão atualizados com sucesso para {vendedor.nome_ven}")
        else:
            print("Vendedor nao encontrado")
    finally:
        db.close()

    print(f"Espero que deu certo KKK{vendedor.nome_ven} , {vendedor.salario_fixo}, {vendedor.comissao}")

