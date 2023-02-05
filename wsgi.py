
import os
from controller import create_app
from waitress import serve
from paste.translogger import TransLogger
import logging


if __name__ == '__main__':
    # HOST = "172.0.0.1"
    HOST = "0.0.0.0"
    port = int(os.environ.get('PORT', 5000))
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
    serve(TransLogger(create_app(), setup_console_handler=True, logging_level=logging.DEBUG), host=HOST, port=port)
    # serve(create_app(), host=HOST, port=port)

    # serve(create_app(), host=HOST, port=port)
