import random


class Card:
    def __init__(self, card_number, suits):
        if any(cardnumber < 1 for cardnumber in card_number):
            raise ValueError("The card number of any suit should be greater than 0.")

        self.cards = []
        self.suits = suits
        for cardnumber, suit in zip(card_number, suits):
            self.cards.extend([(suit, i) for i in range(cardnumber)])


class CardGame:
    def __init__(self, card_number, suits, points, deck_number):
        for suit in suits:
            if suits.count(suit) > 1:
                raise ValueError("The suits should have unique suit.")

        if len(card_number) != len(suits):
            raise ValueError("The card number and suit number are not matching.")

        if set(suits) != set(points.keys()):
            raise ValueError("The input suits and input points are not matching.")

        if deck_number < 1:
            raise ValueError("The number of decks should be greater than 0.")

        self.cards = []
        for _ in range(deck_number):
            self.cards.extend(Card(card_number=card_number, suits=suits).cards)

        self.suits = suits
        self.points = points
        self.deck_number = deck_number


    def shuffleCards(self, seed=None):
        if seed:
            random.Random(seed).shuffle(self.cards)
        else:
            random.shuffle(self.cards)


    def dealCard(self):
        if not self.cards:
            raise ValueError("There is no card left in the deck.")

        return self.cards.pop()

    def sortCards(self, suits_order):
        for suit in self.suits:
            if suit not in suits_order:
                raise ValueError('The suit "{}" is not in the assigned suits order.'.format(suit))
        self.cards.sort(key=lambda x: (suits_order.index(x[0]), x[1]))

    def play(self):
        if len(self.cards) < 6:
            raise ValueError("The number of cards left is not enough to play the game.")

        player_1 = []
        player_2 = []
        player_1_points = player_2_points = 0

        for _ in range(3):
            player_1.append(self.dealCard())
            player_2.append(self.dealCard())

        print("Card Suit - Point: ", self.points, '\n')
        print("Player 1's cards: ", player_1)
        print("Player 2's cards: ", player_2, '\n')

        for suit, num in player_1:
            player_1_points += self.points[suit] * num

        for suit, num in player_2:
            player_2_points += self.points[suit] * num

        if player_1_points > player_2_points:
            print("Player 1 Wins!(Points: {})".format(player_1_points))
        elif player_1_points < player_2_points:
            print("Player 2 Wins!(Points: {})".format(player_2_points))
        else:
            print("Tie (Points: {}, {})".format(player_1_points, player_2_points))
