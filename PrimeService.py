_author__ = 'Anand Patel'

import rpyc


class PrimeService(rpyc.Service):

    def on_connect(self):
        pass
    
    def on_disconnect(self):
        pass
    
    def exposed_findPrimes(input):
        findPrimes(input("Enter the number you want to find primes up to: "))
        

#Finds all primes less than or equal to the input number.
def testPrime(t):
        for i in range(2, t):
            if i < t:
                if (t % i) == 0:
                    return False
        return True

 def findPrimes(n):
    for i in range(2, n+1):
        if testPrime(i):
            print(i),


    



