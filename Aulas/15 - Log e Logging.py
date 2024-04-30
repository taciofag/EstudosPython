# Logging

import logging
'''
debug
info
warning
error
critical
'''

logging.basicConfig(level=logging.DEBUG,filename='app.log',filemode='a',format='%(levelname)s - %(message)s') # Setar o nível
logging.debug('Logging nivel debug')
logging.info('Logging nivel info')
logging.warning('Logging nivel warning')
logging.error('Logging nivel error')
logging.critical('Logging nivel critico')

# guardar informações no log

