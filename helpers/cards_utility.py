

try:
    from constant import *
except:
    from helpers.constant import *


def generate_cards():
    """
        Generate the card of the game

    """
    cards = []
    for color in card_color:
        #print(color)
        for index in range(len(repartition)):
            rep = repartition[index]
            #print(rep)
            for i in range(rep):
                card = str(index + 1) + color
                #print(card)
                cards.append(card)

    return(cards)


def draw_card(deck,hand):
    """
        Draw card function

        return hand with a one more card if the deck not empty

    """
    if (len(deck) >= 1):
        hand.append(deck.pop())
    else:
        print("the deck is empty")
    return hand


# --- Functions to print and select the action available during the turn ---
def print_actions():
    """
        Print the different action choice available
    """
    print("Choississez une action parmi celles-ci:")
    print("")
    print("1- Jouer une carte")
    print("2- Défausser une carte")
    print("3- Donner un indice")
    print("4- Quittez")
    print("")

def get_action_from_player():
    """
        Get the action selected by the player

        return
        -------
        action: int 
            the action value selected
    """
    action = input("")
    print("")
    while (not((action) in ["1","2","3","4"])):
        print_board()
        print("Attention la valeur choisie doit être entre 1 et 4")
        print("")
        action = input("")
        print("")
    
    return (action)