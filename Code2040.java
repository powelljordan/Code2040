// Code 2040 Challenge

// Reverse a string
// n is the number of letters in the input string
// O(n) time complexity is optimal
// O(n) space complexity is also optimal although it may be possible to do it in place
// instead of requiring a second array

public String reversedString(String string){
	String reversedString = "";
	for (char letter : string){
		reversedString = letter + reversedString;
	}
	return reversedString
}
// n is the number of needles in the haystack	
// O(n) time complexity is optimal for an unordered array of needles
// O(n) space complexity is also optimal as the algorithm is in place
public int needleInHaystack(String needle, String haystack){
	if (String needle : haystack){
		return haystack.indexOf(needle)
	}
}

// n is the number of strings in the string array
// O(n) overall time complexity including helper function
// O(n) space complexity though it is in fact possible to do this in place by
// instead removing the elements of the string array that don't contain the 
// prefix. This seems like a bad idea generally speaking 
// though because you would be losing information.
public List<String> stringsThatContainPrefix(String prefix, List<String> stringArray){
	List<String> matchedStringArray = new ArrayList<String>();
	for (String string : stringArray){
		if (string.length() >= prefix.length() && stringContainsPrefix(prefix, string)){
			matchedStringArray.add(string);
		}
	}
	return matcheStringsArray;
}
// O(1) time complexity assuming java does not create a new array to look at a subarray
public stringContainsPrefix(String prefix, String string){
	return string.subList(0, prefix.length()).equals(prefix);
}


