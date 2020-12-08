from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink, Link


class Abilene(Topo):
	def __init__(self):
		Topo.__init__(self)
		H1 = self.addHost('H1', mac= '00:00:00:01:00:01', ip='192.168.0.1/24')
		H2 = self.addHost('H2', mac= '00:00:00:01:00:02', ip='192.168.0.2/24')
		H3 = self.addHost('H3', mac= '00:00:00:01:00:03', ip='192.168.0.3/24')
		H4 = self.addHost('H4', mac= '00:00:00:01:00:04', ip='192.168.0.4/24')
		H5 = self.addHost('H5', mac= '00:00:00:01:00:05', ip='192.168.0.5/24')
		H6 = self.addHost('H6', mac= '00:00:00:01:00:06', ip='192.168.0.6/24')
		H7 = self.addHost('H7', mac= '00:00:00:01:00:07', ip='192.168.0.7/24')
		H8 = self.addHost('H8', mac= '00:00:00:01:00:08', ip='192.168.0.8/24')
		
		S1 = self.addSwitch('S1', mac= '00:00:00:00:00:01')
		S2 = self.addSwitch('S2', mac= '00:00:00:00:00:02')
		S3 = self.addSwitch('S3', mac= '00:00:00:00:00:03')
		S4 = self.addSwitch('S4', mac= '00:00:00:00:00:04')
		S5 = self.addSwitch('S5', mac= '00:00:00:00:00:05')
		S6 = self.addSwitch('S6', mac= '00:00:00:00:00:06')
		S7 = self.addSwitch('S7', mac= '00:00:00:00:00:07')
	
		self.addLink(S1,S2)
		self.addLink(S1,S3)
		self.addLink(S2,S4)
		self.addLink(S2,S5)
		self.addLink(S3,S6)
		self.addLink(S3,S7)
		self.addLink(S4,H1)
		self.addLink(S4,H2)
		self.addLink(S5,H3)
		self.addLink(S5,H4)
		self.addLink(S6,H5)
		self.addLink(S6,H6)
		self.addLink(S7,H7)
		self.addLink(S7,H8)



topos ={'sdn':(lambda : Abilene())}






























