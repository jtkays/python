#!/usr/bin/python
#
import sys
import funcs

def readListOfNumbersFromFile(filename) :
    print "Reading ", filename
    with open(filename) as f :
        lines = f.read().splitlines()

    f.close()
    listOfNums = [int(str) for str in lines]

    return listOfNums


print "Hello, world"
if (len(sys.argv) != 3) :
    print "Wrong number of arguments"
    print "Usage: ", sys.argv[0], " <number> <fileName of numbers>"
    sys.exit(1)

if (not sys.argv[1].isdigit()) :
    print "Argument 1 must be numeric!"
    sys.exit(1)

num = int(sys.argv[1])
numbers = readListOfNumbersFromFile(sys.argv[2])
print "Looking for ", num, " from ", numbers
#al = funcs.findit2(num, [400, 300, 250, 100, 60, 53, 20, 11, 10, 4, 3])
al = funcs.findit2(num, numbers)
print "Answer for %d: %s" % (num, al)
#print "Answer for ",num,": ",al
print "Goodbye"

