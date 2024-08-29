import random
import words_file
import stages_file

logo = stages_file.logo
stages = stages_file.stages
used_letters = []
game_finished = 0
word_chosen = random.choice(words_file.word_list)
word_length = len(word_chosen)
word_hidden = ""
for i in range(0,word_length):
    word_hidden += "_"
lives = 6

print(logo)
print("Welcome to Hangman\n------------------")

def replace_char(string, index, letter):
    return string[:index] + letter + string[index+1:]

while not game_finished:

    print("Word to guess:" + word_hidden)
    letter = input("Guess a letter:").lower()

    if used_letters.count(letter) > 0:
        print("You already said that\n")
        print(stages[lives])
        print(f"{lives} lives left!\n")
        continue

    if word_chosen.count(letter) != 0:
        print("Correct Guess!\n")
        for i in range(0, word_length):
            index = word_chosen[i:].find(letter) + i
            if i == index:
                word_hidden = replace_char(word_hidden,index,letter)



    else:
        print("Wrong Guess!\n")
        lives -= 1

    if lives == 0:
        game_finished = 1
        print("**********You lost**********")
        print(f"The word was {word_chosen}")


    if word_hidden.count("_") == 0:
        game_finished = 1
        print("**********You won**********")

    used_letters.append(letter)
    print(stages[lives])
    print(f"{lives} lives left!\n")
