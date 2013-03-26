# -- coding: utf-8 --

my_name = '曾勁'
my_age = 25 # not a lie
my_height = 168 # cm
my_weight = 60 # kg
my_eyes = '黑色'
my_teeth = '白色'
my_hair = '黑色'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
my_word = "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
print "I said: %r." % my_word
