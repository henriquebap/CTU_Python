print("#########################################")
print("##### Bemvindo a calculadora de IMC #####")
print("#########################################")

name = input("Olá, qual é o sue nome? ")
sex = input("Informe o seu sexo (M/F): ")
peso  = int(input("Informe quantos kilos voce esta: "))
altura = float(input("Informe a sua altura: "))

masculino = sex == "M"
feminine = sex == "F"

print("#################################")
print("##### Calculando o seu IMC #####")
print("#################################")


IMC = peso/altura** 2

print(f"Seu IMC é {IMC}")

if masculino: 
    if (IMC <= 16 and IMC < 18):
        print(f"{name}, Voce está com 'Magreza'")
    elif(IMC > 18 and IMC < 29.9):
        print(f"{name}, CUIDADO! Voce esta com 'Eutrofia'; seu IMC está normal")
    elif(IMC > 30.9 and IMC < 34.4):
        print(f"{name}, Voce está muito gordo (Sobre peso)")
    else:
        print(f"{name}, Voce esta com Obesidade")

if(feminine):
    if (IMC <= 18 and IMC < 18.1):
        print(f"{name}, Voce está com 'Magreza'")
    elif(IMC <= 18.2 and IMC < 33.7):
        print(f"{name}, CUIDADO! Voce esta com 'Eutrofia'; seu IMC está normal")
    elif(IMC <= 33.8 and IMC < 36):
        print(f"{name}, Voce está muito gordo (Sobre peso)")
    else:
        print(f"{name}, Voce esta com Obesidade")
