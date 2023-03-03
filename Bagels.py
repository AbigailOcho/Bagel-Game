import random

NUM_DIGITS = 2
MAX_GUESSES = 5

def main():
    print('''Bagels, a deductive logic game".
By Al Swiegart al@inventwithpython.com
Edited by Abigail Ochoa

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is.  Here are some clues:
When I say:     That means:
  Panda          One digit is correct but in the wrong position.
  Capybara       One digit is correct and in the right position.
  Wolf           No digit is correct.

For example, if the secret number was 21 and your guess was 12, the
clues would be Panda Panda.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGueses = 1
        while numGueses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGueses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGueses += 1

            if guess == secretNum:
                break
            if numGueses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
            return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Capybara')
        elif guess[i] in secretNum:
            clues.append('Panda')
    if len(clues) == 0:
        return 'Wolf'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()


