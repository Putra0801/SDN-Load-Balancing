#!/usr/bin/python

from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo


class Abilene(Topo):
	def __init__(self):
		Topo.__init__(self)
		H1 = self.addHost('H1',cls=Host, ip='192.168.0.1/24',defaultRoute=None)
		H2 = self.addHost('H2',cls=Host, ip='192.168.0.2/24',defaultRoute=None)
		H3 = self.addHost('H3',cls=Host, ip='192.168.0.3/24',defaultRoute=None)
		H4 = self.addHost('H4',cls=Host, ip='192.168.0.4/24',defaultRoute=None)
		H5 = self.addHost('H5',cls=Host, ip='192.168.0.5/24',defaultRoute=None)
		H6 = self.addHost('H6',cls=Host, ip='192.168.0.6/24',defaultRoute=None)
		H7 = self.addHost('H7',cls=Host, ip='192.168.0.7/24',defaultRoute=None)
		H8 = self.addHost('H8',cls=Host, ip='192.168.0.8/24',defaultRoute=None)
		H9 = self.addHost('H9',cls=Host, ip='192.168.0.9/24',defaultRoute=None)
		H10 = self.addHost('H10',cls=Host, ip='192.168.0.10/24',defaultRoute=None)
		H11 = self.addHost('H11',cls=Host, ip='192.168.0.11/24',defaultRoute=None)
		H12 = self.addHost('H12',cls=Host, ip='192.168.0.12/24',defaultRoute=None)
		H13 = self.addHost('H13',cls=Host, ip='192.168.0.13/24',defaultRoute=None)
		H14 = self.addHost('H14',cls=Host, ip='192.168.0.14/24',defaultRoute=None)
		H15 = self.addHost('H15',cls=Host, ip='192.168.0.15/24',defaultRoute=None)
		Server1 = self.addHost('Server1',cls=Host, ip='192.168.0.100/24',defaultRoute=None)
		Server2 = self.addHost('Server2',cls=Host, ip='192.168.0.101/24',defaultRoute=None)
		


		S1 = self.addSwitch('S1', cls=OVSKernelSwitch)
		S2 = self.addSwitch('S2', cls=OVSKernelSwitch)
		S3 = self.addSwitch('S3', cls=OVSKernelSwitch)
		S4 = self.addSwitch('S4', cls=OVSKernelSwitch)
		S5 = self.addSwitch('S5', cls=OVSKernelSwitch)
		S6 = self.addSwitch('S6', cls=OVSKernelSwitch)
		S7 = self.addSwitch('S7', cls=OVSKernelSwitch)
		S8 = self.addSwitch('S8', cls=OVSKernelSwitch)
		S9 = self.addSwitch('S9', cls=OVSKernelSwitch)
		S10 = self.addSwitch('S10', cls=OVSKernelSwitch)
		S11 = self.addSwitch('S11', cls=OVSKernelSwitch)
	
	
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

topos ={'sdn':(lambda : Abilene())}






























