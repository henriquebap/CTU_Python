import serial
import json
import time
from datetime import datetime
conexao=""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    dicionario={}
    cont=0
    while cont<10:
        resposta=conexao.readline()
        dicionario[str(datetime.now())]=[resposta.decode('utf-8')[0:3]]
        print(resposta.decode('utf-8')[0:3])
        cont+=1
    with open('Temperatura.json', "w") as arq:
        json.dump(dicionario, arq)
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")