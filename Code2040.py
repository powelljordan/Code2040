import urllib2,json, datetime, requests

##Code 2040 Challenge


'''Problem 1'''
#Reverse a string
#n is the number of letters in the input string
#O(n) time complexity is optimal
#O(n) space complexity is also optimal although it may be possible to do it in place
#instead of requiring a second array

url = 'http://challenge.code2040.org/api/register'
postdata = {'email':'powellj@mit.edu', 'github':'https://github.com/powelljordan/Code2040'}
keyToken = {'token': 'KEUjKRaWvT'}


def post(url, postdata):
    req = urllib2.Request(url)
    req.add_header('Content-Type','application/json')
    data = json.dumps(postdata)
    response = urllib2.urlopen(req,data).readline()
    return json.loads(response)['result']

##Uncomment code below to get initial token
##print post(url, postdata)



#Alternative way to post that takes advantage of this Requests library. I didn't know I could do it this way.
def postUsingRequests(url, postdata):
    return requests.post(url, json = postdata).json()
##Uncomment code below to get initial token using cleaner post method.
##print postUsingRequests(url, postdata)

'''Problem 2'''

# n is the number of needles in the haystack    
# O(n) time complexity is optimal for an unordered array of needles
# O(n) space complexity is also optimal as the algorithm is in place

urlString = 'http://challenge.code2040.org/api/getstring'
urlValidateString = "http://challenge.code2040.org/api/validatestring"

def reverseString(string):
    reversedString = ""
    for letter in string:
        reversedString = letter + reversedString
    return reversedString

string = post(urlString, keyToken)
reversedString = reverseString(string)

##Uncomment line below to run stage1 solution
##print post(urlValidateString, {'token':'KEUjKRaWvT', 'string':reversedString})

urlHaystack = 'http://challenge.code2040.org/api/haystack'
urlValidateNeedle = 'http://challenge.code2040.org/api/validateneedle'

def needleInHaystack(needle, haystack):
    if needle in haystack:
        return haystack.index(needle)

needleHaystackDict = post(urlHaystack, keyToken)
needle = needleHaystackDict['needle']
haystack = needleHaystackDict['haystack']
needleIndex = needleInHaystack(needle, haystack)

##Uncomment line below to run stage2 solution
##print post(urlValidateNeedle, {'token':'KEUjKRaWvT', 'needle': needleIndex})

'''Problem 3'''

##n is the number of strings in the string array
##O(n) overall time complexity including helper function
##O(n) space complexity though it is in fact possible to do this in place by
##instead removing the elements of the string array that don't contain the 
##prefix. This seems like a bad idea generally speaking 
##though because you would be losing information.

urlPrefix = 'http://challenge.code2040.org/api/prefix'
urlValidatePrefix = 'http://challenge.code2040.org/api/validateprefix'

def stringsThatContainPrefix(prefix, stringArray):
    matchedStringsArray = []
    for string in stringArray:
        if len(string) >= len(prefix) and string[0:len(prefix)] != prefix:
            matchedStringsArray.append(string)
    return matchedStringsArray


prefixDict = post(urlPrefix, keyToken)
prefix = prefixDict['prefix']
array = prefixDict['array']
resultArray = stringsThatContainPrefix(prefix, array)
##Uncomment line below to run stage3 solution
##print post(urlValidatePrefix, {'token':'KEUjKRaWvT', 'array': resultArray})


'''Problem 4'''

urlTime = 'http://challenge.code2040.org/api/time'
urlValidateTime = 'http://challenge.code2040.org/api/validatetime'

def dateMath(date, interval):
    newDate = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(0, interval)
    resultDate = newDate.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    return resultDate

timeDict = post(urlTime, keyToken)
date = timeDict['datestamp']
interval = timeDict['interval']
resultDate = dateMath(date, interval)

##Uncomment line below to run stage4 solution
##print post(urlValidateTime, {'token':'KEUjKRaWvT', 'datestamp': resultDate})


def runChallenges():
    print post(urlValidateString, {'token':'KEUjKRaWvT', 'string':reversedString})
    print post(urlValidateNeedle, {'token':'KEUjKRaWvT', 'needle': needleIndex})
    print post(urlValidatePrefix, {'token':'KEUjKRaWvT', 'array': resultArray})
    print post(urlValidateTime, {'token':'KEUjKRaWvT', 'datestamp': resultDate})

##Uncomment line below to run all 4 challenges
##runChallenges()

    
