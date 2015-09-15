import random
import sys

def main():
	number = 4
	if sys.argv[1]=="help":
		print "Syntax\n"
		print "froll; rolls four fate dice and prints the outcome with the associated adjective."
		print "froll (number); rolls four fate dice and adds the number to the result, then prints the outcome with the associated adjective. May give unpredictable results for non integer bonuses."
		print "froll help; displays this message."
		print "\nProbabilities\n"
		print "Fate dice can be either -1, 0, or 1. That means that the standard roll of four dice has the following possible outcomes."
		print "\tResult\tOdds\tOdds of this or better"
		print "\t-4\t1.23%\t100%"
		print "\t-3\t4.94%\t98.77%"
		print "\t-2\t12.35%\t93.83%"
		print "\t-1\t19.75%\t81.48%"
		print "\t+0\t23.46%\t61.73%"
		print "\t+1\t19.75%\t38.27%"
		print "\t+2\t12.35%\t18.52%"
		print "\t+3\t4.94%\t6.17%"
		print "\t+4\t1.23%\t1.23%"
		sys.exit(0)
	elif sys.argv[1]=='':
		bonus = 0
	else:
		try:
			bonus = int(sys.argv[1])
		except ValueError:
			print "Your bonus is not a number. Jerk."
			sys.exit(1)
	roll = 0
	while number > 0:
		number-=1
		die = random.randint(1,3)-2
		roll+=die
	roll+=bonus
	adjectives = {-1:"Poor", 0:"Mediocre", 1:"Average", 2:"Fair", 3:"Good", 4:"Great", 5:"Superb", 6:"Fantastic", 7:"Epic"}
	if roll <=-2:
		adjective = "Terrible"
	elif roll >= 8:
		adjective = "Legendary"
	else:
		adjective = adjectives[roll]
	print("{}; {}".format(roll, adjective))
main()
