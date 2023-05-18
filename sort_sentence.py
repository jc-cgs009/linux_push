def sortSentence(s):
	s = s.split()
	res = ['']*len(s)
	for word in s:
		res[int(word[-1])-1] = word[:-1]
	return ' '.join(res)

result = sortSentence(input('Enter the string: '))
print(result)
