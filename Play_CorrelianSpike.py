from CorrelianSpike import *


def player_turn():
    print("\nYour hand is:")
    user.show_hand()
    print("\nThe top card of the discard pile is:")
    game_deck.show_discard()
    move = input("\nIt is your turn. What would you like to do? Draw / Swap / Junk\n")
    if move.lower() == "draw":
        print("\nYou pick up a:")
        game_deck.get_topcard()
        keep = input("\nWould you like to keep this card? yes / no\n")
        if keep.lower() == "yes":
            user.draw()
        elif keep.lower() == "no":
            game_deck.discard.append(game_deck.draw())
        else:
            while True:
                keep_error = input("\nThat is not a valid input. Would you like to keep this card? yes / no\n")
                if keep_error.lower() == "yes":
                    user.draw()
                    break
                elif keep_error.lower() == "no":
                    game_deck.discard.append(game_deck.draw())
                    break
    elif move.lower() == "swap":
        print("\nWhich card in your hand would you like to swap out?\n")
        card_num = 1
        for card in user.hand:
            print("Card #", card_num, ":"), card.show()
            card_num += 1
        choice = 0
        while choice < 1 or choice > card_num - 1:
            try:
                choice = int(input())
                if choice < 1 or choice > card_num - 1:
                    print("That is not a valid choice. Which card in your hand would you like to swap out?\n")
                else:
                    pass
            except ValueError:
                print("That is not a valid choice. Which card in your hand would you like to swap out?\n")
        user.hand.append(game_deck.discard[-1])
        game_deck.discard.append(user.hand.pop(choice - 1))
        print("\nYour hand is now:")
        user.show_hand()
    elif move.lower() == "junk":
        print("\nYou junk your cards. Better luck next time!\n")
        user.junk()
        game_deck.discard.append(game_deck.draw())
    else:
        while True:
            move = input("That is not a valid input. What would you like to do? Draw / Swap / Junk\n")
            if move.lower() == "draw":
                print("You pick up a:")
                game_deck.get_topcard()
                keep = input("Would you like to keep this card? yes / no\n")
                if keep.lower() == "yes":
                    user.draw()
                elif keep.lower() == "no":
                    game_deck.discard.append(game_deck.draw())
                else:
                    while True:
                        keep_error = input("That is not a valid input. Would you like to keep this card? yes / no\n")
                        if keep_error.lower() == "yes":
                            user.draw()
                            break
                        elif keep_error.lower() == "no":
                            game_deck.discard.append(game_deck.draw())
                            break
                print("Your hand is now:\n")
                user.show_hand()
                break
            elif move.lower() == "swap":
                print("Which card in your hand would you like to swap out?\n")
                card_num = 1
                for card in user.hand:
                    print("Card #", card_num, ":"), card.show()
                    card_num += 1
                choice = 0
                while choice < 1 or choice > card_num - 1:
                    try:
                        choice = int(input())
                        if choice < 1 or choice > card_num - 1:
                            print("That is not a valid choice. Which card in your hand would you like to swap out?")
                        else:
                            pass
                    except ValueError:
                        print("That is not a valid choice. Which card in your hand would you like to swap out?")
                user.hand.append(game_deck.discard[-1])
                game_deck.discard.append(user.hand.pop(choice - 1))
                print("Your hand is now:")
                user.show_hand()
                break
            elif move.lower() == "junk":
                print("You junk your cards. Better luck next time!")
                user.junk()
                game_deck.discard.append(game_deck.draw())
                break






def play():
    print("\nWelcome to the beautiful jungle planet of Numidian Prime. Located on the edge of the galaxy's mid rim, the\n"
          "system is known for being a haven for smugglers and thieves. Legend has it that the infamous smuggler Han\n"
          "Solo won the legendary Millennium Falcon playing cards at this very table.\n") # Add randomized intros
    if n_players > 1:
        print("Sitting around the table with you are", n_players, "players:\n")
        for player in players:
            if player == user:
                pass
            else:
                print(player.name)
    elif n_players == 1:
        print("There is one player sitting at the table with you:\n")
        for player in players:
            if player == user:
                pass
            else:
                print(player.name)
    print("\nThe dealer deals out two cards to each player.")
    deal()
    for i in range(3):
        for player in players:
            if player == user:
                player_turn()
            else:
                player.take_turn()
        print("\nThe dealer rolls the dice.")
        if roll_dice():
            print("\nThe dice land on doubles. Everyone discards their cards and the dealer deals them the same amount\n"
                  "of cards they had.\n")
            for player in players:
                hand_size = len(player.hand)
                for card in player.hand:
                    game_deck.discard.append(card)
                    player.hand.remove(card)
                for j in range(hand_size):
                    player.draw()
        elif i < 2:
            print("\nThe dice do not land on doubles. Play resumes.")
        else:
            print("\nThe dice do not land on doubles, marking the end of the round.") 
    for player in players:
        print(player.name, "had:")
        player.show_hand()


play()