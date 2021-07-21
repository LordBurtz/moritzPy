from twisted.internet.protocol import Protocol
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol

class WelcomeMessage(Protocol):
    def connectionMade(self):
        self.transport.write("hablo espanol?")

class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write("i luv u baby")

def gotProtocol(p):
    p.sendMessage(" H e l o ")
    reactor.callLater(1, p.sendMessage, "This gon' be sent in a hot minute")
    reactor.callLater(2, p.transport.loseConnection)

point = TCP4ClientEndpoint(reactor, "localhost", 1717)
d = connectProtocol(point, Greeter)
d.addCallback(gotProtocol)
reactor.run()
