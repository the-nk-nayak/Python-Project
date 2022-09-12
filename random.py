import random
name = input("What's your happetight? ")
print("Good Luck ! ", name)
words = ['Chili Mushroom', 'Paneer butter masala', 'shai paneer', 'dal makhni', 'afghani chaap', 'Paneer Rolls', 'Momos', 'chowmein', 'Chinese', 'Pizza', 'Burger', 'Mix veg']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 12
while turns > 0:
	failed = 0
	for char in word:
		if char in guesses:
			print(char, end=" ")
		else:
			print("_")
			print(char, end=" ")
			failed += 1

	if failed == 0:
		print("You Win")
		print("The word is: ", word)
		break
	print()
	guess = input("guess a character:")
	guesses += guess
	if guess not in word:

		turns -= 1
		print("Wrong")
		print("You have", + turns, 'more guesses')

		if turns == 0:
			print("You Loose")
			break