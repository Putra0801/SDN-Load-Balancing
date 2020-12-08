#!/usr/bin/env python
import random as rn
import numpy as np
from numpy.random import choice as np_choice
import requests
from requests.auth import HTTPBasicAuth
import json
import unicodedata
from subprocess import Popen, PIPE
import time
import networkx as nx
from sys import exit

# Method To Get REST Data In JSON Format
def getResponse(url,choice):

	response = requests.get(url, auth=HTTPBasicAuth('admin', 'admin'))

	if(response.ok):
		jData = json.loads(response.content)
		if(choice=="topology"):
			topologyInformation(jData)
		elif(choice=="statistics"):
			getStats(jData)
	else:
		response.raise_for_status()

def topologyInformation(data):
	global switch
	global deviceMAC
	global deviceIP
	global hostPorts
	global linkPorts
	global G
	global cost

	for i in data["network-topology"]["topology"]:
		
		if "node" in i:
			for j in i["node"]:
				# Device MAC and IP

				if "host-tracker-service:addresses" in j:
					for k in j["host-tracker-service:addresses"]:
						ip = k["ip"].encode('ascii','ignore')
						mac = k["mac"].encode('ascii','ignore')
						deviceMAC[ip] = mac
						deviceIP[mac] = ip

				# Device Switch Connection and Port

				if "host-tracker-service:attachment-points" in j:

					for k in j["host-tracker-service:attachment-points"]:
						mac = k["corresponding-tp"].encode('ascii','ignore')
						mac = mac.split(":",1)[1]
						ip = deviceIP[mac]
						temp = k["tp-id"].encode('ascii','ignore')
						switchID = temp.split(":")
						port = switchID[2]
						hostPorts[ip] = port
						switchID = switchID[0] + ":" + switchID[1]
						switch[ip] = switchID

	# Link Port Mapping
	for i in data["network-topology"]["topology"]:
		if "link" in i:
			for j in i["link"]:
				if "host" not in j['link-id']:
					src = j["link-id"].encode('ascii','ignore').split(":")
					srcPort = src[2]
					dst = j["destination"]["dest-tp"].encode('ascii','ignore').split(":")
					dstPort = dst[2]
					srcToDst = src[1] + "::" + dst[1]
					linkPorts[srcToDst] = srcPort + "::" + dstPort
					G.add_edge((int)(src[1]),(int)(dst[1]))

def getStats(data):
	print "\nCost Computation....\n"
	global cost
	txRate = 0
	for i in data["node-connector"]:
		tx = int(i["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["packets"]["transmitted"])
		rx = int(i["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["packets"]["received"])
		txRate = tx + rx
		#print txRate

	time.sleep(2)

	response = requests.get(stats, auth=HTTPBasicAuth('admin', 'admin'))
	tempJSON = ""
	if(response.ok):
		tempJSON = json.loads(response.content)

	for i in tempJSON["node-connector"]:
		tx = int(i["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["packets"]["transmitted"])
		rx = int(i["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["packets"]["received"])
		cost = cost + tx + rx - txRate

	#cost = cost + txRate
	#print cost

def systemCommand(cmd):
	terminalProcess = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
	terminalOutput, stderr = terminalProcess.communicate()
	print "\n*** Flow Pushed\n"
def pushFlowRules(bestPath):

	bestPath = bestPath.split("::")

	for currentNode in range(0, len(bestPath)-1):
		if (currentNode==0):
			inport = hostPorts[h2]
			srcNode = bestPath[currentNode]
			dstNode = bestPath[currentNode+1]
			outport = linkPorts[srcNode + "::" + dstNode]
			outport = outport[0]
		else:
			prevNode = bestPath[currentNode-1]
			#print prevNode
			srcNode = bestPath[currentNode]
			#print srcNode
			dstNode = bestPath[currentNode+1]
			inport = linkPorts[prevNode + "::" + srcNode]
			inport = inport.split("::")[1]
			outport = linkPorts[srcNode + "::" + dstNode]
			outport = outport.split("::")[0]

		xmlSrcToDst = '\'<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><flow xmlns=\"urn:opendaylight:flow:inventory\"><priority>32767</priority><flow-name>Load Balance 1</flow-name><match><in-port>' + str(inport) +'</in-port><ipv4-destination>10.0.0.1/32</ipv4-destination><ipv4-source>10.0.0.4/32</ipv4-source><ethernet-match><ethernet-type><type>2048</type></ethernet-type></ethernet-match></match><id>1</id><table_id>0</table_id><instructions><instruction><order>0</order><apply-actions><action><order>0</order><output-action><output-node-connector>' + str(outport) +'</output-node-connector></output-action></action></apply-actions></instruction></instructions></flow>\''

		xmlDstToSrc = '\'<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><flow xmlns=\"urn:opendaylight:flow:inventory\"><priority>32767</priority><flow-name>Load Balance 2</flow-name><match><in-port>' + str(outport) +'</in-port><ipv4-destination>10.0.0.4/32</ipv4-destination><ipv4-source>10.0.0.1/32</ipv4-source><ethernet-match><ethernet-type><type>2048</type></ethernet-type></ethernet-match></match><id>2</id><table_id>0</table_id><instructions><instruction><order>0</order><apply-actions><action><order>0</order><output-action><output-node-connector>' + str(inport) +'</output-node-connector></output-action></action></apply-actions></instruction></instructions></flow>\''

		flowURL = "http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:"+ bestPath[currentNode] +"/table/0/flow/1"

		command = 'curl --user "admin":"admin" -H "Accept: application/xml" -H "Content-type: application/xml" -X PUT ' + flowURL + ' -d ' + xmlSrcToDst

		systemCommand(command)

		flowURL = "http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:"+ bestPath[currentNode] +"/table/0/flow/2"

		command = 'curl --user "admin":"admin" -H "Accept: application/xml" -H "Content-type: application/xml" -X PUT ' + flowURL + ' -d ' + xmlDstToSrc

		systemCommand(command)

	srcNode = bestPath[-1]
	prevNode = bestPath[-2]
	inport = linkPorts[prevNode + "::" + srcNode]
	inport = inport.split("::")[1]
	outport = hostPorts[H1]

	xmlSrcToDst = '\'<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><flow xmlns=\"urn:opendaylight:flow:inventory\"><priority>32767</priority><flow-name>Load Balance 1</flow-name><match><in-port>' + str(inport) +'</in-port><ipv4-destination>10.0.0.1/32</ipv4-destination><ipv4-source>10.0.0.4/32</ipv4-source><ethernet-match><ethernet-type><type>2048</type></ethernet-type></ethernet-match></match><id>1</id><table_id>0</table_id><instructions><instruction><order>0</order><apply-actions><action><order>0</order><output-action><output-node-connector>' + str(outport) +'</output-node-connector></output-action></action></apply-actions></instruction></instructions></flow>\''

	xmlDstToSrc = '\'<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><flow xmlns=\"urn:opendaylight:flow:inventory\"><priority>32767</priority><flow-name>Load Balance 2</flow-name><match><in-port>' + str(outport) +'</in-port><ipv4-destination>10.0.0.4/32</ipv4-destination><ipv4-source>10.0.0.1/32</ipv4-source><ethernet-match><ethernet-type><type>2048</type></ethernet-type></ethernet-match></match><id>2</id><table_id>0</table_id><instructions><instruction><order>0</order><apply-actions><action><order>0</order><output-action><output-node-connector>' + str(inport) +'</output-node-connector></output-action></action></apply-actions></instruction></instructions></flow>\''

	flowURL = "http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:"+ bestPath[-1] +"/table/0/flow/1"

	command = 'curl --user \"admin\":\"admin\" -H \"Accept: application/xml\" -H \"Content-type: application/xml\" -X PUT ' + flowURL + ' -d ' + xmlSrcToDst

	systemCommand(command)

	flowURL = "http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:"+ bestPath[-1] +"/table/0/flow/2"

	command = 'curl --user "admin":"admin" -H "Accept: application/xml" -H "Content-type: application/xml" -X PUT ' + flowURL + ' -d ' + xmlDstToSrc

	systemCommand(command)


class AntColony(object) :
	def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
            self.distances = distances
            self.pheromone = np.ones(self.distances.shape) / len(distances)
            self.all_inds = range(len(distances))
            self.n_ants = n_ants
            self.n_best = n_best
            self.n_iterations = n_iterations
            self.decay = decay
            self.alpha = alpha
            self.beta = beta

        def run(self):
            shortest_path = None
            all_time_shortest_path = ("placeholder", np.inf)
            for i in range(self.n_iterations):
                all_paths = self.gen_all_paths()
                self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path)
                shortest_path = min(all_paths, key=lambda x: x[1])
                
                print shortest_path
                if shortest_path[1] < all_time_shortest_path[1]:
                    shortest_path = all_time_shortest_path
                    self.pheromone * self.decay
                    return all_time_shortest_path
        
        def spread_pheronome(self, all_paths, n_best, shortest_path):
            sorted_paths = sorted(all_paths, key=lambda x: x[1])
            for path, dist in sorted_paths[:n_best]:
            	for move in path:
           		self.pheromone[move] += 1.0 / self.distances[move]
        
        def gen_path_dist(self, path):
            total_dist = 0
            for ele in path:
                total_dist += self.distances[ele]
                return total_dist
        
        def pick_move(self, pheromone, dist, visited):
            pheromone = np.copy(pheromone)
            pheromone[list(visited)] = 0
            row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)
            norm_row = row / row.sum()
            move = np_choice(self.all_inds, 1, p=norm_row)[0]
            return move


print ("Load Balancing is running")
