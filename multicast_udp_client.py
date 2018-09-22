from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingClient(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("228.0.0.5")
        # Send to 228.0.0.5:8005 - all listeners on the multicast address
        # (including us) will receive this message.
        b = "Client: Ping"	
        self.transport.write(b.encode(), ("228.0.0.5", 8008))

    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (repr(datagram.decode()), repr(address)))


reactor.listenMulticast(8008, MulticastPingClient(), listenMultiple=True)
reactor.run()
