# Python program to print prime factors in pairs.

# Test Cases
def testCases():
    n = 1
    arr = {38585507, 1963, 1271}
    for t in arr:
        print('Test case ' + str(n) + ' ::')
        print('Input number :: ' + str(t))
        printPFsInPairs(t)
        n+=1
        
def checkPrime(num):
    for i in range(2, num):
       if (num % i) == 0:
           return False
           break
    else:
       return True
    
def printPFsInPairs(k):
    for i in range(1, int(pow(k, 1 / 2))+1):
        if k % i == 0:
            j = int(k / i)
            prime1 = checkPrime(i)
            if prime1 is True:
                prime2 = checkPrime(j)
                if prime2 is True:
                    print('Result Prime factors')
                    print(str(i) + " " + str(j) + "\n")
  
# Driver code
testCases()