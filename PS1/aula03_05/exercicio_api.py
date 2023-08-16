import requests


nome = input("Digite o seu nome: ").strip()
response = requests.get(f'http://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')

all_data = response.json()

data = all_data[0]
result = data['res']
total = 0
for item in result:
    periodo = item['periodo']
    periodo = periodo.strip("[").replace(",", " até ")
    frquencia = item['frequencia']
    total += frquencia
    print(f'Durante o periodo {periodo} a frequencia foi {frquencia}')
print(f'O nome {nome} existe um total de {total} ate 2010')




#[
 ##      nome:   string
   #     localidade:	string  
    #    sexo:   string
     #   res:	
      #      [
       #         {
        #            periodo:    string
         #           frequencia:	number
          #      }
           # ]
    #}
#]