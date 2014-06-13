#**Using Strings**

#if you don't want python to create a new line, add an r before the quotation marks
#this is a raw string, used when creating regular expressions

def main():
	s = r"This is an\string!"
	print(s) 

if __name__ == "__main__": main()


#python 3 way of formatting and replacing variables in a string
#.format is a method of the string object

def main():
	n = 42
	s = "This is a {} string!".format(n)
	print(s) 

if __name__ == "__main__": main()

#python 2 way of formatting and replacing variables in a string (which is going away)


def main():
	n = 42
	s = "This is a %s string!" % n
	print(s) 

if __name__ == "__main__": main()




#strings can be defined with single qutoes, doble quotes, or you can use three quotes to add a lot of lines

def main():
	n = 42
	s = '''\
this is a string
line after a line
of text and more
text.
'''
	print(s)

if __name__ == "__main__": main()
