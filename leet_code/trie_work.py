
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):        		
		index = 0
		node = self.root
		
		for character in string:
			index += 1
			if character in node.keys():
				if node[character] == self.endSymbol:
					pass
				else: 
					node = node[character]		
			elif index == len(string) -1:
				node[character] = self.endSymbol
			else:
				node[character] = {}
				node = node[character]
				        

    def contains(self, string):
		index = 0
		node = self.root
		
		for character in string:
			index += 1
			if character in node.keys():
				if node[character] == self.endSymbol:
					return True
				elif index == len(string) - 1:
					return False
				else:
					node = node[character]
			else:
				return False
					
				        
