#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC
#unit 12 ex. 7

class inclusive_range:
	def __init__(self, *args):
		numargs = len(args)
		if numargs < 1: raise TypeError('requires at least one argument')
		elif numargs == 1:
			self.stop = args[0]
			self.start = 0
			self.step = 1

		elif numargs == 2:
			(self.start, self.stop) = args
			self.step = 1
			

		elif numargs == 3:
			(self.start, self.stop, self.step) = args
			

		else: raise TypeError('expected at most 3 arguments. Got {}'.format(numargs))

#iter method makes object iterable

	def __iter__(self):
		i = self.start
		while i <= self.stop:
			yield i
			i += self.step

def main():
   o = inclusive_range(1, 25)
   for i in o: 
   		print i, 

if __name__ == "__main__": main()

#in the original exercise, the instructor had (print i, end=' ') which gave me an error ('invalid syntax')
#after some Googling, I found out that's the way you insert an empty space on Python 3, but it's not supported in earlier versions
#(which is what I have). The way to insert a space is just adding a comma after i.
#http://stackoverflow.com/questions/15018875/end-python-syntax-error
