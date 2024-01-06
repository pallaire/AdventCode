import re

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
		
	def receivePulse(self, pulse, source):
		res = []
		for d in self.destinations:
			self.lowCount += 1
			res.append({'dest':d, 'source':self.name, 'pulse':kLowPulse})
		print(f"Module:{self.name} received pulse:{pulse} from:{source}")
		print(f"     sending: {res}")
		return res
	
	
class FlipFlop:
	def __init__(self, name, destinations):
		self.name = name
		self.destinations = destinations
		self.state = False
		self.lowCount = 0
		self.highCount = 0
		
	def receivePulse(self, pulse, source):
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
		print(f"Module:{self.name} received pulse:{pulse} from:{source}")
		print(f"     sending: {res}")	
		return res
	

class Conjunction:
	def __init__(self, name, destinations):
		self.name = name
		self.destinations = destinations
		self.state = {}
		self.lowCount = 0
		self.highCount = 0
		
	def receivePulse(self, pulse, source):
		self.state[source] = pulse
		
		allHigh = True
		for s in self.state.values():
			if s == kLowPulse:
				allHigh = False
				break
				
		sendPulse = kHighPulse
		if allHigh:
			sendPulse = kLowPulse
	
		res = []
		for d in self.destinations:
			if sendPulse == kLowPulse:
				self.lowCount += 1
			else:
				self.highCount += 1
				
			res.append({'dest':d, 'source':self.name, 'pulse':sendPulse})
		print(f"Module:{self.name} received pulse:{pulse} from:{source}")
		print(f"     sending: {res}")	
		return res
	
	def setupInputs(self, inputs):
		for i in inputs:
			self.state[i] = kLowPulse

class RecieverOnly:
	def __init__(self, name):
		self.name = name
		self.lowCount = 0
		self.highCount = 0
		
	def receivePulse(self, pulse, source):
		print(f"Module:{self.name} received pulse:{pulse} from:{source}")
		print(f"     sending: {[]}")	
		return []
	


def pulseManager(data):
	
	modules = {}
	queue = []
	conjunctions = []
	
	broadcaster = None
	
	for aline in data:
		print(aline)
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


		
	print(f"Modules: {modules.keys()}")
	print()
	
	for k in modules.keys():
		print(f"module key name >>{k}<<")
		
	
	for _ in range(1000):
			
		queue.append({'dest':'broadcaster', 'source':'button', 'pulse':kLowPulse})
		
		while len(queue) > 0:
			task = queue.pop(0)
			# print(f"Working on task: {task}")

			if task['dest'] not in modules:
				modules[task['dest']] = RecieverOnly(task['dest'])

			obj = modules[task['dest']]
			
			nextitems = obj.receivePulse(task['pulse'], task['source'])
			
			queue = queue + nextitems
			
	lows = 0
	highs = 0
	for m in modules.values():
		lows += m.lowCount
		highs += m.highCount
		
	print(f"Finales lows:{lows} highs:{highs}")
	# + 1000 is for the initial button sending to the broadcaster
	return (lows+1000)*highs
			
			
			
			
			
			
data = readData("large.data")
print(f"Problem 1: {pulseManager(data)}")
