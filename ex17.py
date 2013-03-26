from sys import argv
from os.path import exists

script, from_file, to_file = argv

if exists(to_file) == False:
    print "The output file does not exist."

open(to_file, 'w').write(open(from_file).read())

print "Copied from %s to %s (%d bytes)" % (from_file, to_file, len(open(from_file).read()))
