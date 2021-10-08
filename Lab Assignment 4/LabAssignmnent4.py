########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    again = input('Do you want to play again? Y/Yes/N/No')
    if(again.upper() == "Y" or again.upper() == "YES"):
        return True
    elif(again.upper() == "N" or again.upper() == "NO"):
        return False
    else:
        print("Please enter a correct value")
        play_again()
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while(True):
        wager = int(input('How many chips do you want to wager? ==>'))
        if(wager < 1):
            print('The wager amount must be greater than 0. Please enter again')
        elif(wager > bank):
            print('The wager amount cannot be greater than how much you have')
        elif(wager <= bank) or (wager > 0):
            break
        else:
            print('incorrect input please enter a number')

    return wager

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''

    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10)

    return (reel1, reel2, reel3)

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb == reelc:
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while(True):
        chips = int(input('How many chips do you want to start with? ==>'))
        if(chips < 1):
            print('Too Low a value, you can only choose 1 - 100 chips')
        elif(chips > 101):
            print('Too High a value, you can only choose 1 - 100 chips')
        elif(chips <= 101) or (chips > 1):
            break
        else:
            print('incorrect input please enter a proper input')

    return chips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if(matches == 3):
        return wager * 10
    if(matches == 2):
        return wager * 3
    if(matches == 0):
        return wager * -1
    else:
        return 0

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()