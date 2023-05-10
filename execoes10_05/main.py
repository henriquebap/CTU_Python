class UserEmptyError(Exception):
    pass

number = input("Digite um numero: ")
divisor = input("Digite o divisor: ")
try:
    result = int(number)/int(divisor)
    print(f"O resutlado da conta {result}")
except (TypeError ):
    print("Nao foi possivel executar")
except ValueError as exception:
    print(exception)
except ZeroDivisionError as exception:
    print("Impossivel dividir por zero", exception.__class__.__name__)
finally:
    print(f"Voce tentnou fazer a divisao {number} por {divisor}")
print("Fim do programa")


def users():
    if not isinstance(users, list):
        raise TypeError
    if not users:
        raise UserEmptyError("Lista vazia")
try:
    users("")
except TypeError:
    print("A lista nao pode ser vazia")
try:
    users([])
except UserEmptyError as ex:
    print(ex)