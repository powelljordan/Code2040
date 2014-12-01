##Code 2040 Challenge

#Reverse a string
#n is the number of letters in the input string
#O(n) time complexity is optimal
#O(n) space complexity is also optimal although it may be possible to do it in place
#instead of requiring a second array
def reverseString(string):
	reversedString = ""
	for letter in string:
		reversedString.append(letter)
	return reversedString

# n is the number of needles in the haystack	
# O(n) time complexity is optimal for an unordered array of needles
# O(n) space complexity is also optimal as the algorithm is in place
def needleInHaystack(needle, haystack):
	if needle in haystack:
		return haystack.index(needle)

#n is the number of strings in the string array
#O(n) overall time complexity including helper function
#O(n) space complexity though it is in fact possible to do this in place by
#instead removing the elements of the string array that don't contain the 
#prefix. This seems like a bad idea generally speaking 
#though because you would be losing information.
def stringsThatContainPrefix(prefix, stringArray):
	matchedStringsArray = []
	for string in stringArray:
		if len(string) >= len(prefix) and stringContainsPrefix(prefix, string):
			matchedStringsArray.append(string)
	return matchedStringsArray

#O(1) time complexity assuming python does not create a new array to look at a subarray
def stringContainsPrefix(prefix, string):
	return string[0:len(prefix)] == prefix

#I need to google date stuff for python
