from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor, endpoints

resource = File('/tmp')
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 80)
endpoint.listen(factory)
reactor.run()

# https://twistedmatrix.com/documents/current/web/howto/web-in-60/static-content.html
