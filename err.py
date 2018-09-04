import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except StandardError as e:
		print 'Error!'
		#logging.exception(e)
		raise ValueError('input error!')

main()

print 'END'