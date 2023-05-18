class solution:
	def balancedSplitString(self, string):
		res = 0
		count = 0
		for i in string:
			if i == 'R':
				count += 1
			else:
				count -= 1
			if count == 0:
				res += 1
		return res

obj = solution()
result = obj.balancedSplitString(input("Enter the string :"))
print(result)
