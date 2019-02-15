import random

word_bank = ["book", "sweater", "closet", "shoes", "computer", "hair", "glasses", "wire", "speaker", "handle"]
guesses_left = 8
letters_guessed = []
word = random.choice(word_bank)

string1 = word
word_list = list(string1)

for character in word_list:
    current_index = word_list.index(character)
    word_list.pop(current_index)
    word_list.insert(current_index, "_")
print("".join(word_list))

while guesses_left > 0:
    guess = input("guess a letter.")
    word_list = list(word_list)
    answer = list(answer)
    if word_list == answer:
        print("you guessed correctly")
        exit()
    guess = input("guess a letter.")
    word = list(word)
    while guess in word:
        word_list = list(word_list)