﻿
from sys import argv

script,user_name,adress = argv
prompt= '--------'

print ("Hi %s, I'm the %s script." % (user_name,script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" %  adress)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("""
Alright,so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives , computer))
