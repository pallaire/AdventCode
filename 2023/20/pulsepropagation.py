import re
import math

def readData(filename):
	with open(filename) as inputfile:
		lines = inputfile.readlines()
		res = []
		for aline in lines:
			aline = aline.strip()
			if len(aline) > 0:
				res.append(aline)
	return res

kLowPulse = 0
kHighPulse = 1

class Broadcaster:
	def __init__(self, destinations):
		self.name = "broadcaster"
		self.destinations = destinations
		self.lowCount = 0
		self.highCount = 0
		
	def receivePulse(self, pulse, source, idx):
		res = []
		for d in self.destinations:
			self.lowCount += 1
			res.append({'dest':d, 'source':self.name, 'pulse':kLowPulse})
		return res
	
	
class FlipFlop:
	def __init__(self, name, destinations):
		self.name = name
		self.destinations = destinations
		self.state = False
		self.lowCount = 0
		self.highCount = 0
		
	def receivePulse(self, pulse, source, idx):
		if pulse == kHighPulse:
			return []
		
		sendPulse = kLowPulse
		if self.state == False:
			sendPulse = kHighPulse
			
		self.state = not self.state
	
		res = []
		for d in self.destinations:
			if sendPulse == kLowPulse:
				self.lowCount += 1
			else:
				self.highCount += 1
				
			res.append({'dest':d, 'source':self.name, 'pulse':sendPulse})
		return res
	

class Conjunction:
	def __init__(self, name, destinations):
		self.name = name
		self.destinations = destinations
		self.state = {}
		self.lowCount = 0
		self.highCount = 0

		self.lastSentPulse = -1
		self.sendLowPulseIdx = -1
		self.receivedLowPulseIdx = -1
		
	def receivePulse(self, pulse, source, idx):

		if pulse==kLowPulse and self.receivedLowPulseIdx == -1:
			self.receivedLowPulseIdx = idx

		self.state[source] = pulse
		
		allHigh = True
		for s in self.state.values():
			if s == kLowPulse:
				allHigh = False
				break
				
		sendPulse = kHighPulse
		if allHigh:
			sendPulse = kLowPulse
			if self.sendLowPulseIdx == -1: 
				self.sendLowPulseIdx = idx

		self.lastSentPulse=sendPulse
	
		res = []
		for d in self.destinations:
			if sendPulse == kLowPulse:
				self.lowCount += 1
			else:
				self.highCount += 1
				
			res.append({'dest':d, 'source':self.name, 'pulse':sendPulse})
		return res
	
	def setupInputs(self, inputs):
		for i in inputs:
			self.state[i] = kLowPulse

class RecieverOnly:
	def __init__(self, name):
		self.name = name
		self.lowCount = 0
		self.highCount = 0
		self.destinations = []
		
	def receivePulse(self, pulse, source, idx):
		return []
	

def createModules(data):
	modules = {}
	conjunctions = []
	
	broadcaster = None
	
	for aline in data:
		tokens = re.match(r"([%&\w]+) -> (.*)", aline)
		(source, destinations) = tokens.groups()
		destinations = destinations.replace(' ', '')
		destinations = destinations.split(",")
		
		if source == "broadcaster":
			broadcaster = Broadcaster(destinations)
			modules['broadcaster'] = broadcaster
			
		elif source[0] == '%':
			name = source[1:].strip()
			obj = FlipFlop(name, destinations)
			modules[name] = obj
			
		elif source[0] == '&':
			name = source[1:].strip()
			obj = Conjunction(name, destinations)
			modules[name] = obj
			conjunctions.append(obj)

	# Setup conjunctions 
	for c in conjunctions:
		inputs = []
		for moduleName in modules:
			m = modules[moduleName]
			if c.name in m.destinations:
				inputs.append(m.name)
		c.setupInputs(inputs)

	return modules


def pulseManager(data):
	queue = []
	modules = createModules(data)
	
	for idx in range(1000):
		queue.append({'dest':'broadcaster', 'source':'button', 'pulse':kLowPulse})
		
		while len(queue) > 0:
			task = queue.pop(0)

			if task['dest'] not in modules:
				modules[task['dest']] = RecieverOnly(task['dest'])

			obj = modules[task['dest']]
			nextitems = obj.receivePulse(task['pulse'], task['source'], idx)
			queue = queue + nextitems
			
	lows = 0
	highs = 0
	for m in modules.values():
		lows += m.lowCount
		highs += m.highCount
		
	return (lows+1000)*highs
			
			
def computeButtonPressToActivation(data):
	queue = []
	modules = createModules(data)

	# see dataflow in the folder
	controlFlow = ['jn', 'zp', 'ph', 'mf']

	idx = 0
	while True:
		idx += 1
		queue.append({'dest':'broadcaster', 'source':'button', 'pulse':kLowPulse})
		
		while len(queue) > 0:
			task = queue.pop(0)

			if task['dest'] not in modules:
				modules[task['dest']] = RecieverOnly(task['dest'])

			obj = modules[task['dest']]
			nextitems = obj.receivePulse(task['pulse'], task['source'], idx)
			queue = queue + nextitems

		freqFoundCount = 0
		for check in controlFlow:
			if modules[check].sendLowPulseIdx != -1:
				freqFoundCount += 1
		if freqFoundCount == len(controlFlow):
			break

	freqs = []
	for check in controlFlow:
		freqs.append(modules[check].sendLowPulseIdx)

	return math.lcm(*freqs)
			
			
data = readData("large.data")
print(f"Problem 1: {pulseManager(data)}")
print(f"Problem 2: {computeButtonPressToActivation(data)}")
