import random


words_bank = ["tree", "book", "blue", "train", "fish", "woman", "iran", "sky"]
user_mistakes = 0
user_success = 0
good_chars = []
bad_chars =[]
x = random.randint(0, len(words_bank) - 1)
word = words_bank[x]
while user_mistakes < 6:
    for i in range(len(word)):
        if word[i] in good_chars:
                print(word[i], end=" ")

        else:
            print("- ", end="")

    user_char = input("please write your guess: ").lower()
    if len(user_char) == 1:
        if user_char in word:
            good_chars.append(user_char)
            user_success += 1
            print("✔")
            if user_success == len(word):
                 print(word, "You win")
                 break
        else:
            bad_chars.append(user_char)
            user_mistakes += 1
            print("😡")
    else:
         print("mesle adam type kon")
if user_mistakes == 6:
     print("Game over") 

 