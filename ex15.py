from sys import argv

script, file_name = argv

txt = open(file_name)

print "Here's your file %r:" % file_name
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
