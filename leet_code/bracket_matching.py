def balancedBrackets(string):
    bracketStack = string.split()
	bracketMap = {'(': 0, '[': 0, '{': 0 }
	
	while bracketStack:
		currentBracket = bracketStack.pop()
		
		if currentBracket == '(':
			bracketMap['('] = bracketMap['('] + 1			
		elif currentBracket == ')':
			if bracketMap['('] == 0:
				return False
			bracketMap['('] = bracketMap['('] - 1			
		elif currentBracket == '[':
			bracketMap['['] = bracketMap['['] + 1			
		elif currentBracket == ']':
			if bracketMap['['] == 0:
				return False
			bracketMap['['] = bracketMap['['] - 1			
		elif currentBracket == '{':
			bracketMap['{'] = bracketMap['{'] + 1			
		elif currentBracket == '}':
			if bracketMap['{'] == 0:
				return False
			bracketMap['{'] = bracketMap['{'] - 1	
			
	balance = sum(bracketMap[key] for key in bracketMap.keys())
			
	return True if balance == 0 else False