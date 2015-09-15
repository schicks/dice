import random
import sys

def main():
	number = eval(sys.argv[1])
	sides = eval(sys.argv[2])
	roll = 0
	while number > 0:
		number-=1
		roll+= random.randint(1,sides)
	print(roll)
main()
