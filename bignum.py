import random

#   BigNum  v1.0
#  a game by Dan Sanderson (aka Doc Brown)
#
# Enter bet ('h' for instructions, 'q' to quit, 200 minimum):
# h
#
#
#  BigNum is a fairly simple game.  You have five places to put
# digits to construct a five digit number.  These five digits are
# picked randomly (from 0 to 9), one by one.  As they are picked,
# you choose where to put it.  Once you place the digit, you can't
# move it.  The goal is to construct the largest possible number with
# those digits.
#
#  The board looks like this:
#
#        a   b   c   d   e
#      ---------------------
#      |   |   |   |   |   |
#      ---------------------
#
#  To place a digit, simply press the letter.
#
#  If you get the largest number possible, you get back twice
# your bet!  If you get the first digit the largest you get 25%
# of your bet back.
#

def instructions():
    print("\n")
    print("BigNum is a fairly simple game.  You have five places to put")
    print("digits to construct a five digit number.  These five digits are")
    print("picked randomly (from 0 to 9), one by one.  As they are picked,")
    print("you choose where to put it.  Once you place the digit, you can't")
    print("move it.  The goal is to construct the largest possible number with")
    print("those digits.")
    print("\n")
    print("  The board looks like this:")
    print("\n")
    print("            a   b   c   d   e  ")
    print("          ---------------------")
    print("          |   |   |   |   |   |")
    print("          ---------------------")
    print("\n")
    print("  To place a digit, simply press the letter.")
    print("\n")
    print("If you get the largest number possible, you get back twice")
    print("your bet!  If you get the first digit the largest you get 25%")
    print("of your bet back.\n")
    return

def displayboard():
    print(" The board currently looks like:")
    print("\n")
    print("       a   b   c   d   e  ")
    print("     ---------------------")
    print("     | {} | {} | {} | {} | {} |".format(boardnum[0], boardnum[1], boardnum[2], boardnum[3], boardnum[4]))
    print("     ---------------------")
    print("\n")
    return


# Give the player $1000 to start
wallet = 1000

# Initialize variables
bet = 0
minimumbet = 200
playerinput = ""
bignum = [0, 0, 0, 0, 0]
playernum = [0, 0, 0, 0, 0]
boardnum = [" ", " ", " ", " ", " "]

playagain = True

# Title screen
print("  BigNum v1.0")
print(" a game by Dan Sanderson (aka Doc Brown)\n")
print("Ported to Python 3 by Cliff Chipman")

while (playagain == True) & (wallet >= 200):

    while (bet < minimumbet) | (bet > wallet):
        bignum = [0, 0, 0, 0, 0]
        playernum = [0, 0, 0, 0, 0]
        boardnum = [" ", " ", " ", " ", " "]
        print("You have ${} in your wallet.".format(wallet))
        print("Enter your bet (${} minimum), 'h' for instructions, or 'q' to quit:".format(minimumbet))
        playerinput = input()
        playerinput = playerinput.lower()  # Accept both upper & lower case letters

        if playerinput == "h":
            instructions()
        elif playerinput == "q":
            playagain = False
            break
            # exit()
        else:
            try:
                # Did the player enter a valid numeric string?
                bet = int(playerinput)
            except ValueError:
                bet = 0
# print("Bet = " + str(bet))

    if playagain == False: break
    wallet -= bet  # Subtract bet from wallet
    occupied = False  # Flag that the player already picked a column for a number
    goback = False  # Flag that the player pressed an invalid key

    # Generate bignum
    for n in range(0,5):
        num = random.randint(0,9)  # pick a random number between 0 and 9 (inclusive)
        bignum[n] = num
        goback = True
        while goback == True:  # Loops back here if player presses any key besides "a" - "e"
            if occupied == True: print("There is already a number there.")
            occupied = False  # Reset the flag
            displayboard()
            print("The number is {}".format(num))
            playerinput = input("Place:")
            playerinput = playerinput.lower()  # Convert all incoming letters to lowercase to accept either

            if playerinput == "a":  # | (playerinput == "A")):  # Player picked column a

                if boardnum[0] != "":
                    playernum[0] = num
                    boardnum[0] = str(num)
                    goback = False
                else:
                    occupied = True

            elif playerinput == "b":  # | (playerinput == "B")):  # Player picked column b

                if boardnum[1] != "":
                    playernum[1] = num
                    boardnum[1] = str(num)
                    goback = False
                else:
                    occupied = True

            elif playerinput == "c":  # | (playerinput == "C")):  # Player picked column c

                if boardnum[2] != "":
                    playernum[2] = num
                    boardnum[2] = str(num)
                    goback = False
                else:
                    occupied = True

            elif playerinput == "d":  # | (playerinput == "D")):  # Player picked column d

                if boardnum[3] != "":
                    playernum[3] = num
                    boardnum[3] = str(num)
                    goback = False
                else:
                    occupied = True

            elif playerinput == "e":  # | (playerinput == "E")):  # Player picked column e

                if boardnum[4] != "":
                    playernum[4] = num
                    boardnum[4] = str(num)
                    goback = False
                else:
                    occupied = True
            else:                       # Player picked some other character!
                occupied = True

    bignum = sorted(bignum, reverse=True)  # Make bignum the biggest number possible
    print("The board is full.")
    print("Your number is: {}{}{}{}{}".format(playernum[0],playernum[1],playernum[2],playernum[3],playernum[4]))
    print("The highest possible number: {}{}{}{}{}".format(bignum[0],bignum[1],bignum[2],bignum[3],bignum[4]))

# Calculate player's score
# If you get the largest number possible, you get back twice your bet!
# If you get the first digit the largest you get 25% of your bet back.
# Otherwise, you get nothing.

    if playernum == bignum:  # If you get the largest number possible, you get back twice your bet!
        print("You made the largest number possible!")
        print("You won ${}".format(int(bet * 2)))
        wallet += bet * 2

    elif playernum[0] == bignum[0]:  # If you get the first digit the largest you get 25% of your bet back.
        print("You got the first digit!")
        print("You won ${}".format(int(bet * 0.25)))
        wallet += bet * 0.25

    else:
        print("Sorry, no money awarded this round.")  # Sorry -- you get nothing -- try again
    bet = 0

#  playagain should be false at this point
print("You are leaving the game with ${}".format(int(wallet)))
if wallet < 200: print("You don't have enough money to place a bet.")
print("Thanks for playing!")
exit()