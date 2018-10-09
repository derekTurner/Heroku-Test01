import os
from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor, endpoints

PORT = int(os.environ.get('PORT', 8080))

resource = File('/tmp')
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, PORT)
endpoint.listen(factory)
reactor.run()

# https://twistedmatrix.com/documents/current/web/howto/web-in-60/static-content.html
# gonae wirk
