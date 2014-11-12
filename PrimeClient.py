__author__ = 'anand'

import rpyc

c = rpyc.connect("localhost", 12345)
c.root
print(c.root.test())

