
class Directory:
	def __init__(self, name, parent=None):
		self.name = name
		self.children = {}
		self.size = -1
		self.parent = parent
	
	def isDirectory(self):
		return True

	def isFile(self):
		return False
	
	def getSize(self):
		size = 0
		for name, item in self.children.items():
			size += item.getSize()
		self.size = size
		return size

class File:
	def __init__(self, name, size, parent):
		self.name = name
		self.size = size
		self.parent = parent

	def isDirectory(self):
		return False

	def isFile(self):
		return True
	
	def getSize(self):
		return self.size


def problems(lines):
	root = Directory('/')
	root.parent = root
	cwd = root

	directories = [root]
	files = []

	for aline in lines:
		tokens = aline.split()

		if tokens[0] == '$':

			command = tokens[1]
			if command == 'ls':
				# no need to loop here, files lines starts with a number and directory with a 'dir'
				pass

			elif command == 'cd':
				dst = tokens[2]
				if dst == '/':
					cwd = root
				elif dst == '..':
					cwd = cwd.parent
				else:
					if dst in cwd.children and cwd.children[dst].isDirectory():
						cwd = cwd.children[dst]
					else:
						print(f"CD invalid : {aline}")
						return 

			else:
				print(f"Command invalid : {aline}")
				return
		else:
			size = tokens[0]
			name = tokens[1]

			if size == 'dir':
				newdir = Directory(name, cwd)
				directories.append(newdir)
				cwd.children[name] = newdir
			else:
				newfile = File(name, int(size), cwd)
				files.append(newfile) 
				cwd.children[name] = newfile

	root.getSize()

	atMost100000 = 0
	for d in directories:
		if d.size <= 100000:
			atMost100000 += d.size
	print(f"Problem 1 total size of directories with at most 100000 size is : {atMost100000}")

	totalDiskSize = 70000000
	currentFreeSpace = totalDiskSize - root.size
	freeSpaceNeeded = 30000000
	toFree = freeSpaceNeeded - currentFreeSpace

	smallestOverToFree = 70000000
	smallestOverToFreeName = ''

	for d in directories:
		if d.size >= toFree and d.size < smallestOverToFree:
				smallestOverToFree = d.size
				smallestOverToFreeName = d.name

	print(f"Problem 2 smallest dir to free {toFree} is dir [{smallestOverToFreeName}] with size {smallestOverToFree}")
	

day = '07'
# filename = f"day{day}test01.txt"
filename = f"day{day}data01.txt"
lines = [aline.strip() for aline in open(filename).readlines()]

print(f"2022 Day {day} using file [{filename}]")
problems(lines)