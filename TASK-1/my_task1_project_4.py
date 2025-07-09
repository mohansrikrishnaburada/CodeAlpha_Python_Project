import random
#import hangman_stages
word_list=['banana','apple','beautiful',"potato",'beatuiful']
print("Welcome to the Hangman Game! Get ready for an exciting challenge 🎉")
lives=6
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("guess a letter:").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
            lives-=1
            print(f"lives rmaining is:{lives}")
            print("Oops, that's not in the word! Keep trying, you're doing awesome! 💪")
            if lives== 0:
                game_over=True
                print("You loose!")
                print("Don't lose heart! You fought bravely! Jump back in and win next time! 😊")
                break
    if '_' not in display:
         game_over=True
         print("you win!!")
    #print(hangman_stages.stages[lives])        

