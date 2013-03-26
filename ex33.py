numbers = []

def while_func(total, increments):
    i = 0
    while i < total:
         print "At the top i is %d" % i
         numbers.append(i)

         i += increments
         print "Numbers now:", numbers
         print "At the bottom i is %d" % i

while_func(16, 4)

print "The numbers: "

for num in numbers:
    print num,
