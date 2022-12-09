import pandas as pd
from twilio.rest import Client

account_sid = "ACafb26252d84b5132e6c0e54dc35edb60"
auth_token = "6edaabe58082ae95690342e7eb83260d"
client = Client(account_sid, auth_token)

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in meses:

    dados_vendas = pd.read_excel(f'{mes}.xlsx')

    if (dados_vendas['Vendas'] > 55000).any():
        vendedor = dados_vendas.loc[dados_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = dados_vendas.loc[dados_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguem bateu a meta.\n Vendedor: {vendedor}\n Valor: {vendas}')
         #code the twilio/ messenge smarthphone
        message = client.messages.create(
            to="+5542991586508",
            from_="+18176708142",
            body=f'No mês de {mes} alguem bateu a meta.\n Vendedor: {vendedor}\n Valor: {vendas}')
        print(message.sid)



