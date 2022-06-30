import random
word_file = open('words_alpha.txt')
word_list = word_file.read()
word_list = word_list.split("\n")
word_file.close()

answer = random.choice(word_list)
answer = answer.upper()

def wordguess(answer):
    number_of_guesses = 7
    answer_listed = list(answer)
    wrong_guesses = []
    display_word = ['_']*len(answer)
    while number_of_guesses > 0:
        guess = str(input("Guess a letter or word:"))
        guess = guess.upper()
        while guess in wrong_guesses: #as long as it has been guessed, it will throw an error
            print("You've already guessed '" + str(guess) + "'. Try again.")
            guess = str(input("Guess a letter or word:"))
            guess = guess.upper()
        if len(guess) == 1:
            #Check If Letter is in word
            if guess in answer:
            #If it is, fill in the letters
                while guess in answer_listed:
                    letter = answer_listed.index(guess)
                    answer_listed[letter] = " "
                    display_word[letter] = guess
                else:
                    print(display_word)
                    if display_word == list(answer):
                        print("You completed the word " + answer + ". Congrats!")
                        return
            #If not, show current words, take guess away and display guesses
            else:
                number_of_guesses -= 1
                wrong_guesses.append(guess)
                print('\nThat is not in the answer. Wrong guesses so far:')
                print(wrong_guesses)
                print("You have " + str(number_of_guesses) + " guesses left.")
        #If guess is longer than one letter, compare words
        else:
            if guess == answer:
            #If word matches, congratulate
                print("Congratulations! You guessed " + answer)
                return
            #If not a match, take away guess
            else:
                number_of_guesses -= 1
                print("Sorry, that is not the correct word.")
                print("You have " + str(number_of_guesses) + " guesses left.")

    else:
        print("Game Over!")

wordguess(answer)