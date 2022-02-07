import random


class Card(object):
    def __init__(self, value, stave):
        self.value = value
        self.stave = stave

    def get_value(self):
        return self.value

    def get_stave(self):
        return self.stave

    def show(self):
        print("{}: {}".format(self.value, self.stave))


class Deck(object):
    def __init__(self):
        self.values = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.staves = ["Circle", "Triangle", "Square"]
        self.sylop_value = 0
        self.sylop_stave = "Sylop"
        self.cards = []
        self.build()
        self.discard = []

    def build(self):
        for value in self.values:
            for stave in self.staves:
                self.cards.append(Card(value, stave))
        for i in range(2):
            self.cards.append(Card(self.sylop_value, self.sylop_stave))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()

    def show(self):
        for card in self.cards:
            card.show()

    def show_discard(self):
        self.discard[-1].show()

    def get_topcard(self):
        return self.cards[-1].show()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self):
        self.hand.append(game_deck.draw())

    def junk(self):
        players.remove(self)
        for card in self.hand:
            self.hand.remove(card)
            game_deck.discard.append(card)

    def show_hand(self):
        for card in self.hand:
            card.show()


class Dealer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self):
        self.hand.append(game_deck.draw())

    def show_hand(self):
        for card in self.hand:
            card.show()


class NPC:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self):
        self.hand.append(game_deck.draw())

    def show_hand(self):
        for card in self.hand:
            card.show()

    def junk(self):
        players.remove(self)
        for card in self.hand:
            self.hand.remove(card)
            game_deck.discard.append(card)

    def take_turn(self):
        move = random.randint(1, 10)
        if 1 <= move <= 5:  # Draw
            print("\n" + self.name, "draws a card.")
            keep = random.randint(1, 2)
            if keep == 1:
                self.draw()
                print(self.name, "keeps the card.")
            else:
                game_deck.discard.append(game_deck.draw())
                print(self.name, "discards the card.")
        elif 6 <= move <= 9:  # Swap
            choice = random.randint(0, len(self.hand) - 1)
            print("\n" + self.name, "swaps the")
            game_deck.show_discard()
            print("from the discard pile for a")
            self.hand[choice].show()
            self.hand.append(game_deck.discard[-1])
            game_deck.discard.append(self.hand.pop(choice))

        else:  # Junk
            self.junk()
            game_deck.discard.append(game_deck.draw())
            print("\n" + self.name, "junks his cards.")


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 == die2


def deal():
    for i in range(2):
        for player in players:
            player.draw()
    game_deck.discard.append(game_deck.draw())


n_players = random.randint(1, 7)
game_deck = Deck()
game_deck.shuffle()
players = []
p_names = ["Lando Calrissian", "Han Solo", "Boba Fett", "Jabba the Hutt", "The Crimson Corsair", "Grand Admiral Thrawn",
           "Count Dooku"]
player_name = input("What is your name?\n")
random.shuffle(p_names)
user = Player(player_name)
players.append(user)
for p in range(n_players):
    players.append(NPC(p_names.pop()))
random.shuffle(players)
