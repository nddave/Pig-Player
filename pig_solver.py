# Assignment information
# ---
# Class : COSC 201 - Data structures and algorithms
# Assignment : Programming Project 3
# Student : Nirman Dave

# Program information
# ---
# Name : Implementation of dynamic programming
# Description : The program that uses dynamic programming to calculate the most optimal play in the game pig.
# 				Dynamic programming is used by storing each probability value calculated in a dictionary with it's
# 				corresponding game description. A game description is a list of n, x, y and t values. These probabilities
# 				are looked back into the dictionary when overlapping subproblems arise.
# Language : Python 3.0
# Requirements : pig_prob.py should be in the same directory as this file

# Importing modules and required methods
import pig_prob as pp
import sys
import time

myd = {}		# myd is a dictionary that stores data from pig_prob.py
myd2 = {}		# myd2 is another dictionary that will be used to memoize for the dynamic programming implementation
iterations = 0	# A counter to count the number of iterations

def probs(x, t):
	""" A function that uses the output from pig_prob.py
	and inserts all of them into the dictionary myd. This
	makes the probabilities easy to call when needed.
	"""
	turn_target = int(x)

	p = pp.PigProbabilities(t)
	myd["p(0)"] = float(p.p_end_at(turn_target, 0))

	for i in range(0, 6):
		myd[str("p(" + str(turn_target+i) + ")")] = float(p.p_end_at(turn_target, turn_target + i))

def calcwins_even(n, x, y, t):
	""" A function that uses the formula to count the max of
	probabilities for an even n. Where n is turns remaining,
	t is total needed to win, x is player 1 score and y is
	player 2 score.
	"""
	allprobs = []		# stores all items that need to be compated -- to find the max of all probabilities
	allsums = []		# stores all items that need to be totaled -- sumation of probabilities for varying s
	if (t - x) < 2:		# defines s as t-x. Where s the target roll.
		s = 2
	else:
		s = t - x
	while (s > 1):
		allsums = []	# clears allsums list
		probs(s, t)		# uses pig_prob.py to calculate probabilities for s
		winprob_zero = (float (wins(n-1, x, y, t) * float(myd["p(0)"]))) 						  # calculates: wins(n-1, x, y, t) * p(0)
		for i in range (6):
			z = s + i
			allsums.append(float ((wins(n-1, x+s, y, t)) * float(myd[str("p(" + str(z) + ")")]))) # calculates: wins(n-1, x+s, y, t) * p(total = s) and adds that to allsums list
		winprob_other = sum(allsums)			# sums allsums list
		prob = winprob_zero + winprob_other
		allprobs.append(prob)					# appends the probability to allprobs list
		s -= 1									# decriments s by 1 and repreats the loop
	nxyt = [n, x, y, t]							# nxyt is a list with values n, x, y, t
	nxyt_prob = (max (allprobs)) 				# nxyt_prob is the corresponding prob to certain values of n, x, y, t
	myd2[str(nxyt)] = nxyt_prob					# the n, x, y, t values are stored in a dictionary with its corresponding probability. this is the dynamic programming step, to infer back the value when needed.
	return (max (allprobs)) 					# returns the max of all probabilities

def calcwins_odd(n, x, y, t):
	""" A function that uses the formula to count the max of
	probabilities for an odd n. Where n is turns remaining,
	t is total needed to win, x is player 1 score and y is
	player 2 score.
	"""
	allprobs = []		# stores all items that need to be compated -- to find the max of all probabilities
	allsums = []		# stores all items that need to be totaled -- sumation of probabilities for varying s
	if (t - y) < 2:		# defines s as t-y. Where s the target roll.
		s = 2
	else:
		s = t - y
	while (s > 1):
		allsums = []	# clears allsums list
		probs(s, t)		# uses pig_prob.py to calculate probabilities for s
		winprob_zero = (float (wins(n-1, x, y, t) * float(myd["p(0)"])))							# calculates: wins(n-1, x, y, t) * p(0)
		for i in range (6):
			z = s + i
			allsums.append(float ((wins(n-1, x, y+s, t)) * float(myd[str("p(" + str(z) + ")")])))	# calculates: wins(n-1, x, y+s, t) * p(total = s) and adds that to allsums list
		winprob_other = sum(allsums)			# sums allsums list
		prob = winprob_zero + winprob_other		
		allprobs.append(prob)					# appends the probability to allprobs list
		s -= 1									# decriments s by 1 and repreats the loop
	nxyt = [n, x, y, t]							# nxyt is a list with values n, x, y, t
	nxyt_prob = (min (allprobs))				# nxyt_prob is the corresponding prob to certain values of n, x, y, t				
	myd2[str(nxyt)] = nxyt_prob					# the n, x, y, t values are stored in a dictionary with its corresponding probability. this is the dynamic programming step, to infer back the value when needed.
	return (min (allprobs))						# returns the min of all probabilities

def wins(n, x, y, t):
	""" Calculates the probability that player 1 will win 
	given the game has reached the situation described above.
	"""
	global iterations
	iterations += 1				# increments the counter to monitor the iterations done
	key = str([n, x, y, t])		# defines key as the str of the list [n, x, y, t]
	if key in myd2:				
		return float(myd2[key])	# return the probability if key is present -- makes the code dynamic
	else:						
		if x >= t:				# if x >= t return 1.0
			return 1.0
		elif y >= t:			# if y >= t return 0.0
			return 0.0
		elif n == 0:			# if n == 0 return 0.5
			return 0.5
		elif (n % 2 == 0):		# if n is even return calcwins_even
			return calcwins_even(n, x, y, t)
		else:					# else return calcwins_odd
			return calcwins_odd(n, x, y, t)

def main():
	""" Uses the arguemnts from the command line to output
	the chance of winning, iterations of the formula, turn total
	and time taken to complete the process. This takes first 3
	arguments from the command line.
	"""
	n = int(sys.argv[1])	# first argument is the value for n
	x = int(sys.argv[2])	# second argument is the value for x
	y = int(sys.argv[3])	# third argument is the value for y
	t = 100					# fourth argument is defined by the code. this is the total score required to win

	k = time.process_time()	# starts time process
	print ("\nChance of winning = %f" % wins(n, x, y, t))	# prints the chances of winning
	if (t - y) < 2:
		print ("Turn total = 2")
	else:
		print ("Turn total = %i" % int(t - y))				# prints the turn total
	print ("Iterations = %i" % int(iterations))				# prints the number of iterations
	print ("\nTime taken = %f seconds \n" % ((time.process_time()-k)))	# prints the time taken to complete the process
        
if __name__ == "__main__":
    main()						# initiates the program with the main function
