import argparse

def main():
	parser = argparse.ArgumentParser(description="test")
	parser.add_argument('thelist', type = int, nargs = '+')
	args = parser.parse_args()	
	print(args.thelist)
main()