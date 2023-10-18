def preencherInventario(lista):
  resp="S"
  while resp == "S":
    equipamento=[input("Equipamento: "),
              float(input("Valor: ")),
              int(input("Número Serial: ")),
              input("Departamento: ")]
    lista.append(equipamento)
    resp = input("Digite S para continuar: ").upper()

def preencherInventario(lista):
  resp="S"
  while resp == "S":
    equipamento=[input("Equipamento: "),
              float(input("Valor: ")),
              int(input("Número Serial: ")),
              input("Departamento: ")]
    lista.append(equipamento)
    resp = input("Digite S para continuar: ").upper()

def localizarPorNome(lista):
  busca=input("Digite o nome do equipamento que deseja buscar: ")
  for elemento in lista:
    if busca==elemento[0]:
      print("Valor..: ", elemento[1])
      print("Serial.:", elemento[2])

def exibirInventario(lista):
  for elemento in lista:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

def depreciarPorNome(lista, porc):
  depreciacao=input("Digite o nome do equipamento que será depreciado: ")
  for elemento in lista:
    if depreciacao==elemento[0]:
      print("Valor antigo: ", elemento[1])
      elemento[1] = elemento[1] * (1-porc/100)
      print("Novo valor: ", elemento[1])

def excluirPorSerial(lista):
  serial=int(input("Digite o serial do equipamento que será excluido: "))
  for elemento in lista:
    if elemento[2]==serial:
      lista.remove(elemento)
  return "Itens excluídos."

def resumirValores(lista):
  valores=[]
  for elemento in lista:
    valores.append(elemento[1])
  if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))

def perguntar():
    resposta = input("""O que deseja realizar?
" +
                  "<I> - Para Inserir um usuário
" +
                  "<P> - Para Pesquisar um usuário
" +
                  "<E> - Para Excluir um usuário
" +
                  "<L> - Para Listar um usuário: """).upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                          input("Digite a última data de acesso: "),
                                          input("Qual a última estação acessada: ").upper()]
    
def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!= None:
        print("Nome......."+ lista[0])
        print("Ultimo Acesso......"+ lista[1])
        print("Ultima Estacao...."+ lista[2])
    
def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.....")
        print("Login: ", chave)
        print("Dados: ", valor)

