
import os
from controller import create_app
from waitress import serve
from paste.translogger import TransLogger
import logging
from model import model

if __name__ == '__main__':

    if not os.path.exists('data_base'):
        os.mkdir('data_base')
    if not os.path.exists('data_base/db.db'):
        model.init_db()
    # HOST = "172.0.0.1"
    HOST = "0.0.0.0"
    port = int(os.environ.get('PORT', 8080))
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
    serve(TransLogger(create_app(), setup_console_handler=True, logging_level=logging.DEBUG), host=HOST, port=port)
    # serve(create_app(), host=HOST, port=port)

    # serve(create_app(), host=HOST, port=port)
