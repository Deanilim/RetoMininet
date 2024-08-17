from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI

class TreeTopo(Topo):
    def build(self):
        # Crear switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Crear hosts (nodos)
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Conectar switches
        self.addLink(s1, s2)
        self.addLink(s1, s3)

        # Conectar hosts a switches
        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s3)

if __name__ == '__main__':
    topo = TreeTopo()
    net = Mininet(topo=topo, controller=Controller, switch=OVSKernelSwitch, link=TCLink)
    net.start()
    CLI(net)
    net.stop()
