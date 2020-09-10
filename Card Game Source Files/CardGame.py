import random
'''
Author: Brian(Kangjian) Ma, kangjianma@gmail.com
Date: Sep 10, 2020

A module of Card Game

Classes:
    
    Card
    CardGame

Functions:
    shuffleCards(float)
    dealCard()
    sortCards(list)
    play()
    
'''


class Card:
    """
    A class to represent a deck of cards.

    Attributes
    ----------
        card_number : list
            a list of decimal integers, number of card for each suit
        suits : list
            a list of strings, card suits in a deck

    """

    def __init__(self, card_number, suits):
        """
        Construct all the necessary attributes for the Card object

        Parameters
        ----------
            card_number : list of decimal integers
                number of cards for each suit
            suits : list of strings
                card suits in a deck

        Exception
        ----------
            If card number of any suit is less than 1, an ValueError will be raised.
        """

        if any(cardnumber < 1 for cardnumber in card_number):
            raise ValueError("The card number of any suit should be greater than 0.")

        self.cards = []
        self.suits = suits
        for cardnumber, suit in zip(card_number, suits):
            self.cards.extend([(suit, i) for i in range(cardnumber)])


class CardGame:
    """
    A class to represent a Card Game.

    Attributes
    ----------
        card_number : list
            a list of decimal integers, number of card for each suit in a deck
        suits : list
            a list of strings, card suits in a deck
        points : dictionary
            suit-point pairs in the game
        deck_number : int
            number of decks in one card game

    Methods
    -------
        shuffleCards(seed=None):
            Shuffle cards in random order, subject to the "seed" attribute.

        dealCard():
            Get a card from the top of cards.

        sortCards(suits_order):
            Sort cards in passed suits order, and the cards of the same suit are sorted in ascending order of
            the number on the card.

        play():
            2 players play the game by drawing 3 cards with alternate turns.
            Whoever has the higher score wins the game, otherwise there is a tie.
            The score is calculated as the sum of number on the card multiplying the suit point,
            according to the "suit-point" pair parameter "points" passed to the the __init__().

    """

    def __init__(self, card_number, suits, points, deck_number):
        """
       Construct all the necessary attributes for the CardGame object

       Parameters
       ----------
            card_number : list of decimal integers
                number of card for each suit
            suits : list of strings
                card suits in a deck
            points : dictionary
                a dictionary of suit-point pair in the game
            deck_number : int
                number of decks in one card game

       Exception
       ---------
           If suits do not have unique suit, an ValueError will be raised.
           If the "card_number" does not match "suits", an ValueError will be raised.
           If "suits" do not match suit-point pairs "points", an ValueError will be raised.
           If the number of deck is less than 1, an ValueError will be raised.
       """

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
        """
        Randomly shuffle the cards in the card deck, and return a whole deck of cards with a mixed order
        If the argument 'seed' is passed, the shuffled cards is predictable and reproducible.

        Parameters
        ----------
            seed : float, optional
                Random seed (default is None).

        Returns
        -------
            SNone
        """

        if seed:
            random.Random(seed).shuffle(self.cards)
        else:
            random.shuffle(self.cards)

    def dealCard(self):
        """
        Get one card from top of the cards.
        If there is no card left in the deck, a ValueError is raised.

        Returns
        -------
            A card with number and suit

        Exception
        ---------
            If there is no card left in the deck, a ValueError is raised.
        """

        if not self.cards:
            raise ValueError("There is no card left in the deck.")

        return self.cards.pop()

    def sortCards(self, suits_order):
        """
        Sort the cards in the order of passed suits. Cards of the same suit will be sorted in ascending order
        of the number on the card.

        Parameters
        ----------
            suits_order : list of string
                suit order, according to which the cards will be sorted.

        Returns
        -------
            None
        """

        for suit in self.suits:
            if suit not in suits_order:
                raise ValueError('The suit "{}" is not in the assigned suits order.'.format(suit))
        self.cards.sort(key=lambda x: (suits_order.index(x[0]), x[1]))

    def play(self):
        """
        2 players play the game with drawing 3 cards by taking turns.
        Whoever has the higher score wins the game, otherwise there is a tie.
        The score is calculated as the sum of number on the card multiplying the suit point,
        according to the "points" parameter passed to the the __init__().

        Returns
        -------
            None

        Exception
        ---------
            If the left cards is less than 6, an ValueError will be raised.
        """

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
