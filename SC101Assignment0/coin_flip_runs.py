"""
File: coin_flip_runs.py
Name: James
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""
import random
import random as r


def main():
	print('Let\'s flip a coin!')
	num_run = int(input('Number of runs: '))
	string = random_coin_flip()
	count = 0
	can_add = True
	while True:
		if count == num_run:
			break
		new_flip = random_coin_flip()
		if string[-1] == new_flip:
			#  Avoid consecutive occurrences that continuously increment by one.
			if can_add:
				count += 1
				can_add = False
		else:
			can_add = True
		string += new_flip
	print(string)


def random_coin_flip():
	result = random.randint(0, 1)
	if result == 1:
		return 'H'
	else:
		return 'T'


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
