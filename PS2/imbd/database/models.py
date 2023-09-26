from sqlalchemy import Column,Integer, String, CHAR
# from sqlalchemy.orm import relationship

from database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    cod_clie = Column(Integer, primary_key=True)
    nome_clie = Column(String, nullable=False)
    endereco = Column(String)
    cidade = Column(String)
    cep = Column(CHAR)
    uf = Column(CHAR)
    cnpj = Column(CHAR)
    ie = Column(CHAR)

    #produtos = relationship("produto", back_populates="cliente")

class Vendedor(Base):
    __tablename__ = "vendedor"

    cod_ven = Column(Integer,primary_key=True)
    nome_ven = Column(String, nullable=False)
    salario_fixo = Column(Integer)
    comissao = Column(CHAR)

# class Produto(Base):
#     __tablename__ = "produto"

#     cod_prod = Column(Integer, primary_key=True)
#     unidade = Column(String)
#     descricao = Column(String)
#     val_unit = Column(Integer)

# class Pedido(Base):
#     __tablename__ = "pedido"

#     num_pedido = Column(Integer,primary_key=True)
#     pr_entrega = Column(Integer, nullable=False)
#     cod_clie = Column(Integer, ForeignKey('cliente.cod_clie'))
#     cod_ven = Column(Integer, ForeignKey('vendedor.cod_ven'))

#     cliente = relationship('cliente', back_populates='pedidos')
#     vendedor = relationship('vendedor', back_populates='pedidos')

# class ItemPedido(Base):
#     __tablename__ = 'item_pedido'

#     num_pedido = Column(Integer,ForeignKey('pedido.num_pedido'))
#     cod_prod = Column(Integer, ForeignKey('produto.cod_prod'))
#     quant = Column(Integer)