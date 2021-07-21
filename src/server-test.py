from twisted.internet import protocol, reactor, endpoints
from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet.endpoints import TCP4ClientEndpoint

class Server(Protocol):
    def connectionMade(self):
        print(self.transport.getHost())
        self.transport.write("Hello from le server".encode("utf-8"))
        self.transport.loseConnection()

class ServerFactory(ServerFactory):
    def buildProtocol(self, addr):
        return Server

def init():
    endpoint = TCP4ClientEndpoint(reactor, "localhost",2000)
    endpoint.listen(ServerFactory)

if __name__ == '__main__':
    init()

reactor.run()
