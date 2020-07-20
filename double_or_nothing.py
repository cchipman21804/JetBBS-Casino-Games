import random

# [Credit 47302] Bank: Double or Nothing
#
# Double or Nothing
#
# Starting bet: 200
#
# You lose.
#
# [Credit 47102] Bank: Double or Nothing
#
# Double or Nothing
#
# Starting bet: 200
#
# You have 400 credits in the pot.
#
# Continue? yes
#
# You lose.
#
# [Credit 46902] Bank: Double or Nothing
#
# Double or Nothing
#
# Starting bet: 200
#
# You have 400 credits in the pot.
#
# Continue? yes
#
# You have 800 credits in the pot.
#
# Continue? yes
#
# You lose.
#
# [Credit 39025] Bank: Double or Nothing
#
#     Double or Nothing
#
# Starting bet: 200
#
# You have 400 credits in the pot.
#
# Continue? yes
#
# You lose.


def instructions():
    print("Double Or Nothing is a VERY simple game.  Enter your bet at the prompt.  The computer flips a virtual coin")
    print("If the coin falls on HEADS, the computer gives back double your bet.  If the coin falls TAILS, the computer")
    print("keeps your money.\n")
    return


# Give the player $1000 to start
wallet = 1000

# Initialize variables
bet = 0
pot = 0
minimumbet = 200
playerinput = ""
playagain = True

# Title screen
print("  Double or Nothing v1.0")
print("Ported to Python 3 by Cliff Chipman")

while (playagain == True) & (wallet >= 200):  # Python says this expression can be simplified: while (playagain & wall...

    while (bet < minimumbet) | (bet > wallet):
        print("You have ${} in your wallet.".format(wallet))
        print("There is ${} in the pot.".format(pot))
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

    if playagain == False: break  # Python says this expression can be simplified: if not playagain: break
    wallet -= bet  # Subtract bet from wallet
    # goback = False  # Flag that a player pressed an invalid key
    coin = random.randint(0,1)
    if coin == 1:
        pot += bet * 2
        print("*** HEADS *** There is ${} in the pot.".format(pot))
    else:
        print("*** TAILS *** You lose.")
        pot = 0
    playerinput = input("Continue? ")
    playerinput = playerinput.lower()
    if playerinput == "y":
        playagain = True
    else:
        playagain = False
    bet = 0

# playagain should be False at this point
wallet += pot
print("You are leaving the game with ${}".format(wallet))
if wallet < 200: print("You don't have enough money to place a bet.")
print("Thanks for playing!")
exit()