_author__ = 'Anand Patel'

import rpyc


def testprime(t):
    for i in range(2, t):
        if i < t:
            if (t % i) == 0:
                return False
    return True


def findprimes(n):
    ret = ""
    for i in range(2, n):
        if testprime(i):
            #print(i),
            ret = ret + str(i) + " "
    return ret

class PrimeService(rpyc.Service):

    ALIASES = ["prime"]

    def on_connect(self):
        pass
    
    def on_disconnect(self):
        pass
    
    def exposed_findprimes(self, n):
        return findprimes(n)

    def exposed_test(self):
        return "it works."

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(PrimeService, port=12345)
    t.start()



    



