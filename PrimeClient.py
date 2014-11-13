__author__ = 'anand'

import rpyc

# replace 'localhost' with ip
c = rpyc.connect("localhost", 12345)
n = int(input("Enter a number: "))
c.root
print(c.root.findprimes(n))

