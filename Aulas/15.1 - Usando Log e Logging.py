# Logging

import logging
import datetime

agora = datetime.datetime.now()

logging.basicConfig(level=logging.DEBUG, filename='app.log',encoding='utf-8',filemode='a',format='%(levelname)s - %(message)s') # Setar o nível
email = input('Digite seu email: ')
while True:
    try:
            
        senha = int(input('Digite sua senha: '))
        if senha == 123456:
            print('Acesso Concedido')
            logging.info(f'{email} entrou em sua conta bancária {agora.strftime("%Y-%m-%d %H:%M:%S")}')
            break
        else:
            print('Senha incorreta, digite novamente')
            logging.info(f'{email} errou a senha {agora.strftime("%Y-%m-%d %H:%M:%S")}')
    except ValueError as erro:
        print(f'Digite apenas números')
        logging.info(f'Não digitou números inteiros às {agora.strftime("%Y-%m-%d %H:%M:%S")}')