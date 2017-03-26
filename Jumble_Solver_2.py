# Word jumble solver, used to solve jumble 'colisa' in TN newspaper
# Now can attempt to solve a 2 word jumble

from itertools import permutations
from time import clock

# Print intro
print """
        **********************************
      *                                    * 
     *    Ben's Magic Word Jumble Solver    *
     *             v 2.0.1                  *
      *                                    *
        **********************************

   *Enter jumbled letters or leave blank to exit*
    * If the jumble answer is 2 words, enter 2 *
"""

def getWordsFromDictionary(length):
	# Returns words from loaded dictionary when len() == length
	# Create set
	words = set()
	# Open a dictionary of words stored in txt format
	with open ('us_english_61k.txt', 'r') as f:
		for word in f:
			word = word.replace('\n', '')	# Remove \n character
			# Add words to set that match length only
			if len(word) == length:		
				words.add(word)
	return words
	
def getPermutations(letters):
	# Get permutations of the letters
	all_perms = permutations(letters)
	# Permutations of a string are given as a letter list. Join them
	# and add to set
	perms = set()
	for perm in all_perms:
		perms.add(''.join(perm))

	return perms

def solve_2_words(letters, len_word_1, quiet = False):
	# Solve a 2 word jumble
	# First, get permutations of the letters
	
	# Don't print anything if quiet == True	
	if quiet == False:
		if len(letters) == 10:
			print 'This will take a minute...'
		elif 10 < len(letters) < 14:
			print 'This will take a while...'
		elif 14 < len(letters) < 18:
			print 'This may take hours...'
		elif len(letters) > 18:
			print 'This will take forever... Try something else.'
		
		print 'Scrambling letters...'
		
	# Permutate the jumbled letters
	perms = getPermutations(letters)

	# Loop through each permutation, splitting at the corrent word lengh
	# and checking against the dictionary for each word length
	word_dict_1 = getWordsFromDictionary(len_word_1)
	word_dict_2 = getWordsFromDictionary(len(letters)-len_word_1)
	answers = []
	for perm in perms:
		# Check if len_first_1 chars of permutation is a word
		if perm[:len_word_1] in word_dict_1:
			# Is a word, check second part
			if perm[len_word_1:] in word_dict_2:
				# Also found in second dictionary, answer found
				answer = perm[:len_word_1] + ' ' + perm[len_word_1:]
				answers.append(answer)
				
				if not quiet:
					print 'Answer found: {}'.format(answer)
				
	return answers
	

# Ask for jumbles to solve until no more are entered
while True:	
	print '------------------------------------------------------------'
	letters = raw_input('\nJumbled letters: ') 		# Get letters
	if not letters: break 							# Exit if blank
	
	letters = letters.replace(' ', '')				# Remove any spaces
	# Remove characters that aren't letters
	letters = ''.join([letter for letter in letters if letter.isalpha()])
	letters = letters.lower()						# Make lowercase

	# Check if the answer is 2 words
	if '2' in letters:
		# Answer is 2 words, ask for length of both words
		len_word_1 = raw_input('Length of first word: ')
		# Check that input is an int 1-12
		while len_word_1 not in [str(n) for n in range(1,13)]:
			print 'ERROR: Please type a number 1-12'
			len_word_1 = raw_input('Length of first word: ')
		# Convert to int
		len_word_1 = int(len_word_1)
		letters = raw_input('Jumbled letters: ')
		start_time = clock()	# Get start time
		words_found = solve_2_words(letters, len_word_1)
	else:
		start_time = clock()	# Get start time
		# Load word set from dictionary
		words = getWordsFromDictionary(len(letters))
		
		# Permutate the jumbled letters
		perms = getPermutations(letters)

		# Create list for unjumbled words found
		words_found = []

		# Test each permutation of jumble against loaded dictionary
		for p in perms:
			# Check if the permutation is a word in the set dictionary
			if p in words:
				# Word found, append to list
				words_found.append(p)
				
	# Print the words that were found if any
	if words_found:
		print '\n\nUnjumbled words found:'
		print '----------------------'
		for word_found in words_found:
			print word_found
	else:
		print '\n\nNo unjumbled words found...'
			
	# Print time rounded to ms		
	time_output = 'Time: {}s'.format(round(clock() - start_time, 3))
	print '\n'
	print '=' * len(time_output)
	print time_output
	print '=' * len(time_output)
	print ''


print 'Exiting...'
