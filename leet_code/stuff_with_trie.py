def multiStringSearch(bigString, smallStrings):
	
	trie = populate_trie(bigString)
	words_found = []	
	
	
	print(trie.children)
	print(bigString)
		
	
    for string in smallStrings:
		words_found.append(is_word_in_trie(trie, string))
		
	return words_found
	
	
def populate_trie(string):		
	root = TrieNode()
	node = root
	for character in string:		
		if character in node.children:
			node = node.children[character]		
		else:			
			node.children[character] = TrieNode()
			node = node.children[character]	
			
	return root
			
	
def is_word_in_trie(trie, word):			
	node = trie
	word_index = 0	
	character_in_trie = True
	
	while character_in_trie and not node.is_complete_word and word_index < len(word):			
		character_in_trie = True if word[word_index] in node.children else False

		if character_in_trie:				
			node = node.children[word[word_index]]						
			word_index += 1
			
	return node.is_complete_word
					
	
class TrieNode:
	
	def __init__(self, is_complete_word=False):		
		self.children = {}
		self.is_complete_word = is_complete_word
			