import random
import hangman_words
import hangman_art
stages = hangman_art.stages
word_list = hangman_words.word_list
logo=hangman_art.logo

#Randomly choose a word from the word_list and assign it to a variable.
secret_word=random.choice(word_list)

#Split the string into an array of letters
secret_word_list=[]
for letter in secret_word:
    secret_word_list.append(letter)
    
#The number of tries a player has to guess the correct word
lives=len(stages)-1 

#A list which will hold all the letters that were guessed by the player
user_guesses=[]

#initialize the game
print(logo)

#To display the secret word in blank format
hidden_blank=[]
for letter in secret_word:
    hidden_blank.append('_')
print(' '.join(hidden_blank))

#Check whether the guessed letter occurs in the secret word. 
while lives>0:
    guess=input("Guess a letter: ").lower()
    
    if guess in user_guesses:
        print(f"You have already guessed {guess},please type another word")
    elif guess=='' or len(guess)>1:
        print("Please type a single letter!")
    elif guess in secret_word:
        user_guesses.append(guess)
        for i in range(0,len(secret_word_list)):
            if guess == secret_word_list[i]:
                hidden_blank[i]=guess
        print(' '.join(hidden_blank))
        print(stages[lives])
        if hidden_blank==secret_word_list:
            break
    else:
        print(' '.join(hidden_blank))
        #If wrong guess ,then the player loses a life.
        lives-=1
        print(stages[lives])
        user_guesses.append(guess)
        if lives==1:
            print(f'You guessed {guess}, that\'s not in the word.You have {lives} life left')
        else:
            print(f'You guessed {guess}, that\'s not in the word.You have {lives} lives left')
        
        
#Result of the game       
if lives==0:
    print("You lost :(")
    print(f"The secret word was {secret_word}")
else:
    print(f"That's right!,the secret word was {secret_word}")
    print("you won :)")