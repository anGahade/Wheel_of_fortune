import random

words_list = ("cow", "rabbit", "bear", "deer", "fox", "pigeon")
game_word = words_list[random.randrange(0, len(words_list))]
letters = list(game_word)
guess = ["*" for i in range(len(game_word))]

user_try = int(input("Write your number of tries: "))

while user_try > 0:
    user_answer = input("Enter your guess: ")

    if len(user_answer) >= 2:
        if user_answer == game_word:
            print("Congratulations, you`v won!")
            break
        else:
            print("You`v lost!")
            break

    if user_answer in letters:
        index = letters.index(user_answer)
        guess[index] = user_answer
        result = ""
        for i in range(len(guess)):
            if guess[i] == "*":
                result += "*"
            else:
                result += guess[i]

        print(result)
    else:
        print("Sorry, that letter is not in the word.")

    user_try -= 1

    if "".join(guess) == game_word:
        print("You guessed the word!", game_word)
        break

    if user_try == 0:
        print("You are out of tries. The word was", game_word)
