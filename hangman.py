import random

def hangman(word):
    wrong = 0
    stages = ["",
    "____________        ",
    "|          |        ",
    "|          0        ",
    "|         /|\       ",
    "|         / \       "]

    remaining_letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    print("\n".join(stages))

    while wrong < 3:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[:len(stages)-e+1]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[:len(stages)-wrong]))
        print("You lose! it was {}".format(word))

list_of_words = ["game", "nature", "python","computer","science","car","it","programmer","null"]
t = random.randint(0, 8)

hangman(list_of_words[t])

