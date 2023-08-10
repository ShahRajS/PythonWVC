import logging

logging.basicConfig(filename='LoggingPrac.log', filemode='w', level=logging.DEBUG)
logging.debug('Debugging statement')
logging.info('Information statement')
logging.warning('Warning statement')
logging.error('Error statement')

rate = 5
percent = 0

try:
    (rate / percent)
except Exception as Argument:
    logging.exception('Error occurred while dividing rate / percent')
