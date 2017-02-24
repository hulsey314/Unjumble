# Word unscrambler, used to solve scramble 'colisa' in TN newspaper

from itertools import permutations
from time import clock

# Ask for scrambles to solve until no more are entered
while True:	
	letters = raw_input('\nEnter letters: ') 	# Get letters
	if not letters: break 				# Exit if blank
		
	start_time = clock()				# Get start time
	words = set()					# Make words set

	# Open a dictionary stored in txt format
	with open ('us_english_61k.txt', 'r') as f:
		for word in f:
			word = word.replace('\n', '')	# Remove \n character
			# Add words to set that match scramble length only
			if len(word) == len(letters):		
				words.add(word)

	# Permutate the scrambled letters into every combination
	perms = set(permutations(letters))

	print '\nUnscrambled words found:'

	# Test each permutation of scramble against loaded dictionary
	for p in perms:
		# Permutations of a string are given as a letter list. Join them
		word_test = ''.join(p)
		# Check if the permutation is a word in the set dictionary
		if word_test in words:
			print word_test
			
	# Print time rounded to ms		
	print '.....\nTime: {}s\n.....'.format(round(clock() - start_time, 3))

print 'Exiting...'
