
try:
    from constant import *
    from cards_utility import *
except:
    from helpers.constant import *
    from helpers.cards_utility import *


def print_instruction_play(hand):
    print("Choississez la carte que vous voulez jouer")
    print("")
    for i in range(5):
        print(str(i + 1) + "- " + hand[i])
    print("")

def get_card_to_play(hand):
    action_value = input("")
    print("")
    while (not((action_value) in ["1","2","3","4","5"])):
        print_board()
        print("attention la valeur choisie doit être entre 1 et 5")
        print("")
        action_value = input("")
        print("")

    card_to_play = hand[int(action_value) - 1]
    return (card_to_play)


def is_valid_card_to_play(board,card):

    index_card = card_color.index(card[1])

    number_on_board = int(board[index_card][0])

    if (number_on_board + 1 == int(card[0])):
        return (True)
    else:
        return (False)

def play_card(board,card):
    index_card = card_color.index(card[1])

    board[index_card] = card

    return board    

def remove_card_from_hand(hand,card):
    hand.remove(card)
    return hand

def remove_card_from_know_info(hand,know_infos,card):
    index_card = hand.index(card)
    
    know_infos[index_card] = "? "
    return know_infos
    

def play(deck,board,hands,know_infos,error_token,turn):
    """
        Action play

        parameters
        -----------
        deck: list of cards on the deck

        board: list of cards on the board

        hands: the list of the cards of the player (unknow for the current player)

        know_infos: list of the know infos

        error_token: the number of error token

        turn: the number of the current player

        return
        -------
        the new state for the deck the hands the know_infos after the play
    """
    
    # the hand of the player
    hand = hands[turn]

    # the know info from the player
    know_info = know_infos[turn]

    # Get the card selected by the current player
    print_instruction_play(hand) # replace by know info
    card = get_card_to_play(hand)

    if (is_valid_card_to_play(board,card)):
        # If the play is valid play it on the board
        board = play_card(board,card)
        
        # Then remove the card from the hand of the player
        know_info = remove_card_from_know_info(hand,know_info,card)
        hand = remove_card_from_hand(hand,card)

        # Finally draw a card
        hand = draw_card(deck,hand)
        print(board)
    else:
        #
        error_token += 1
        print("Erreur! Vous perdez une vie!")

    
    return deck,board,hands,know_infos,error_token