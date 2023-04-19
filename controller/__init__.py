from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

API_ROOT = '/api/'

app = Flask(__name__)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


CHUNK_SIZE = 8192
def read_file_chunks(path):
    with open(path, 'rb') as fd:
        while 1:
            buf = fd.read(CHUNK_SIZE)
            if buf:
                yield buf
            else:
                break
            

def create_app():
    import controller.test2
    import controller.test3
    import controller.healing_hostory_controller
    import controller.result_predict_controller
    import controller.train_model_controller
    return app
