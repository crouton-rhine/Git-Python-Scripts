import random

wordbank = ['radish', 'onion', 'tomato', 'cauliflower', 'acres', 'adult', 'advice', 'arrangement', 'attempt', 'august', 'autumn', 'border', 'breeze',
'brick', 'calm', 'canal', 'cast', 'chose', 'claws', 'coach', 'constantly', 'contrast', 'cookies', 'customs', 'damage', 'deeply', 'depth', 'discussion',
'doll', 'donkey', 'essential', 'exchange', 'exist', 'explanation', 'facing', 'film', 'finest', 'fireplace', 'floating', 'folks', 'fort', 'garage', 'grabbed',
'grandmother', 'habit', 'happily', 'heading', 'hunter', 'image', 'independent', 'instant', 'kids', 'label', 'lungs', 'manufacturing', 'mathematics', 'melted',
'memory', 'mill', 'mission', 'monkey', 'mysterious', 'neighborhood', 'nuts', 'occasionally', 'official', 'ourselves', 'palace', 'plates', 'poetry',
'policeman', 'positive', 'possibly', 'practical', 'pride', 'promised', 'recall', 'relationship', 'remarkable', 'require', 'rhyme', 'rocky', 'rubbed',
'rush', 'sale', 'satellites', 'satisfied', 'scared', 'selection', 'shake', 'shaking', 'shallow', 'shout', 'silly', 'simplest', 'slight', 'slip', 'slope',
'soap', 'solar', 'species', 'spin', 'stiff', 'swung', 'tales', 'thumb', 'tobacco', 'toy', 'trap', 'treated', 'tune', 'university', 'vapor', 'vessels',
'wealth', 'wolf', 'zoo']
GameWord = wordbank[random.randrange(0, len(wordbank))]
#print(GameWord)

def checkGuess(UserGuess):
	if UserGuess.lower() not in 'abcdefghijklmnopqrstuvwxyz':
		UserGuess = input('That is not a letter! Please try again: ')
		return checkGuess(UserGuess)
	elif len(UserGuess) > 1:
		UserGuess = input('Please enter 1 letter!: ')
		return checkGuess(UserGuess)
	else:
		return UserGuess

VisWord = '-'*len(GameWord)
VisWordList = list(VisWord)

def Hangman(Guess):
	GuessLim = 8
	WrongGuesses = ''
	guesses = 0
	while guesses <= GuessLim:
		if Guess in GameWord:
			indexes = [i for i,x in enumerate(list(GameWord)) if x == Guess]
			for i in indexes:
				VisWordList[i] = Guess
			VisWordRpl = ''.join(VisWordList)
			print(VisWordRpl)
			if VisWordRpl == GameWord:
				print('You win!')
				break
			print('You have used the following wrong letters already: ' + WrongGuesses)
			Guess = input('Please input the next letter: ')
			Guess = checkGuess(Guess)
		else:
			if guesses == GuessLim:
				print('You lose!')
				break
			print('You have %i guesses left.' % (GuessLim - guesses))
			WrongGuesses += Guess
			print('You have used the following wrong letters already: ' + WrongGuesses)
			Guess = input('Please input another letter: ')
			Guess = checkGuess(Guess)
			guesses += 1

#print(VisWord)
print('The word is %i letters long.' % len(GameWord))
UserGuess = input("Please guess a letter: ")
Guess = checkGuess(UserGuess)
Hangman(Guess)
