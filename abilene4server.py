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
		H9 = self.addHost('H9', mac= '00:00:00:01:00:09', ip='192.168.0.9/24')
		H10 = self.addHost('H10', mac= '00:00:00:01:00:10', ip='192.168.0.10/24')
		H11 = self.addHost('H11', mac= '00:00:00:01:00:11', ip='192.168.0.11/24')
		H12 = self.addHost('H12', mac= '00:00:00:01:00:12', ip='192.168.0.12/24')
		H13 = self.addHost('H13', mac= '00:00:00:01:00:13', ip='192.168.0.13/24')
		H14 = self.addHost('H14', mac= '00:00:00:01:00:14', ip='192.168.0.14/24')
		H15 = self.addHost('H15', mac= '00:00:00:01:00:15', ip='192.168.0.15/24')
		Server1 = self.addHost('Server1', mac= '00:00:00:01:00:100', ip='192.168.0.100/24')
		Server2 = self.addHost('Server2', mac= '00:00:00:01:00:101', ip='192.168.0.101/24')
		Server3 = self.addHost('Server3', mac= '00:00:00:01:00:102', ip='192.168.0.102/24')
		Server4 = self.addHost('Server4', mac= '00:00:00:01:00:103', ip='192.168.0.103/24')


		S1 = self.addSwitch('S1', mac= '00:00:00:00:00:01')
		S2 = self.addSwitch('S2', mac= '00:00:00:00:00:02')
		S3 = self.addSwitch('S3', mac= '00:00:00:00:00:03')
		S4 = self.addSwitch('S4', mac= '00:00:00:00:00:04')
		S5 = self.addSwitch('S5', mac= '00:00:00:00:00:05')
		S6 = self.addSwitch('S6', mac= '00:00:00:00:00:06')
		S7 = self.addSwitch('S7', mac= '00:00:00:00:00:07')
		S8 = self.addSwitch('S8', mac= '00:00:00:00:00:08')
		S9 = self.addSwitch('S9', mac= '00:00:00:00:00:09')
		S10 = self.addSwitch('S10', mac= '00:00:00:00:00:10')
		S11 = self.addSwitch('S11', mac= '00:00:00:00:00:11')
	
	
		self.addLink(S1,S2)
		self.addLink(S1,S3)
		self.addLink(S1,S4)
		self.addLink(S2,S4)
		self.addLink(S4,S6)
		self.addLink(S6,S8)
		self.addLink(S8,S9)
		self.addLink(S8,S7)
		self.addLink(S9,S11)
		self.addLink(S11,S10)
		self.addLink(S10,S7)
		self.addLink(S7,S5)
		self.addLink(S5,S3)
		self.addLink(S5,S6)
	
		self.addLink(H1,S1)
		self.addLink(H2,S1)
		self.addLink(H3,S2)
		self.addLink(H4,S2) 
		self.addLink(H5,S3)
		self.addLink(H6,S3)
		self.addLink(H7,S4)
		self.addLink(H8,S4)
		self.addLink(H9,S5)
		self.addLink(H10,S6)
		self.addLink(H11,S8)
		self.addLink(H12,S7)
		self.addLink(H13,S9)
		self.addLink(H14,S10)
		self.addLink(H15,S11)

		self.addLink(Server1, S1)
		self.addLink(Server1, S2)
		self.addLink(Server1, S3)
		self.addLink(Server1, S4)
		self.addLink(Server1, S5)
		self.addLink(Server1, S6)
		self.addLink(Server1, S7)
		self.addLink(Server1, S8)
		self.addLink(Server1, S9)
		self.addLink(Server1, S10)
		self.addLink(Server1, S11)

		self.addLink(Server2, S1)
		self.addLink(Server2, S2)
		self.addLink(Server2, S3)
		self.addLink(Server2, S4)
		self.addLink(Server2, S5)
		self.addLink(Server2, S6)
		self.addLink(Server2, S7)
		self.addLink(Server2, S8)
		self.addLink(Server2, S9)
		self.addLink(Server2, S10)
		self.addLink(Server2, S11)

		self.addLink(Server3, S1)
		self.addLink(Server3, S2)
		self.addLink(Server3, S3)
		self.addLink(Server3, S4)
		self.addLink(Server3, S5)
		self.addLink(Server3, S6)
		self.addLink(Server3, S7)
		self.addLink(Server3, S8)
		self.addLink(Server3, S9)
		self.addLink(Server3, S10)
		self.addLink(Server3, S11)

		self.addLink(Server4, S1)
		self.addLink(Server4, S2)
		self.addLink(Server4, S3)
		self.addLink(Server4, S4)
		self.addLink(Server4, S5)
		self.addLink(Server4, S6)
		self.addLink(Server4, S7)
		self.addLink(Server4, S8)
		self.addLink(Server4, S9)
		self.addLink(Server4, S10)
		self.addLink(Server4, S11)


topos ={'sdn':(lambda : Abilene())}






























