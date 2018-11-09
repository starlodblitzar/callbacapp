from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.httputil import HTTPServerRequest

from logging import getLogger, Formatter, DEBUG
from logging.handlers import TimedRotatingFileHandler

# setup logger
LOG = getLogger(__name__)
LOG.setLevel(DEBUG)
file_handler = TimedRotatingFileHandler('log.log', when="midnight")
file_handler.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(name)-5s - %(levelname)-5s - %(message)s')
file_handler.setFormatter(formatter)
LOG.addHandler(file_handler)

class Handler(RequestHandler):
    '''Handles request by logging it'''

    def __init__(self, application: Application, request: HTTPServerRequest):
        super().__init__(application, request)

        LOG.info('Got the following callback: {request}'.format(request=request.__dict__))


    def get(self, *args, **kwargs):

        self.set_status(200)
        self.flush()

    def post(self, *args, **kwargs):
        self.set_status(200)
        self.flush()

APP: Application = Application([
    (r'/', Handler)
])

if __name__ == "__main__":
    APP.listen(port=9002, address='0.0.0.0')
    LOG.info('App inited.')
    IOLoop.current().start()