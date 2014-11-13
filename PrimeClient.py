__author__ = 'Anand Patel and Jeffrey Creighton'

import rpyc


# replace 'localhost' with ip of the computer you are connecting to
c = rpyc.connect("localhost", 12345)
c.root
# place method calls after this line.
print(c.root.findprimes(int(input("Enter a number: "))))

