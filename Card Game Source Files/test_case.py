from CardGame import *

test_case = 4

# Functional Test Case

if test_case == 1:
    # Test Case 1
    # Test the card is initiated correctly.

    cardgame = CardGame(card_number=[2, 4, 6], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=1)

    print("cards=", cardgame.cards, '\n')

    print("suits=", cardgame.suits, '\n')

    print("points=", cardgame.points, '\n')

    print("deck number=", cardgame.deck_number)

elif test_case == 2:
    # Test Case 2
    # Test “Shuffle cards in the deck” Operation works

    cardgame = CardGame(card_number=[2, 4, 6], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=1)

    print("original cards:", cardgame.cards)

    cardgame.shuffleCards()

    print("original cards:", cardgame.cards)

    print("shuffled cards", cardgame.cards)

elif test_case == 3:
    # Test Case 3
    # Test “Get a card from the top of the deck” Operation works

    cardgame = CardGame(card_number=[2, 4, 6], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=1)

    print("Original Cards=", cardgame.cards)

    print("Card Number=", len(cardgame.cards), '\n')

    deal_card = cardgame.dealCard()

    print("Deal Card=", deal_card)

    print("Cards=", cardgame.cards)

    print("Card Number=", len(cardgame.cards), '\n')

    deal_card = cardgame.dealCard()

    print("Deal Card=", deal_card)

    print("Cards=", cardgame.cards)

    print("Card Number=", len(cardgame.cards), '\n')

    deal_card = cardgame.dealCard()

    print("Deal Card=", deal_card)

    print("Cards=", cardgame.cards)

    print("Card Number=", len(cardgame.cards), '\n')

elif test_case == 4:
    # Test Case 4
    # Test “sort Cards” Operation works

    cardgame = CardGame(card_number=[2, 4, 6], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=1)

    print("Original Cards=", cardgame.cards, '\n')

    cardgame.shuffleCards(seed=1)

    print("Shuffled Cards=", cardgame.cards, '\n')

    cardgame.sortCards(suits_order=["yellow", "green", "red"])

    print("Sorted Cards=", cardgame.cards)

# elif test_case == 5:
#     # Test Case 5
#     # Test “Determine winners” Operation works
#
#     cardgame = CardGame(card_number=[2, 4, 6], suits=['red', 'yellow', 'green'],
#                         points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=1)
#
#     print("Original Cards=", cardgame.cards, '\n')
#
#     cardgame.play()

elif test_case == 6:
    # Test Case 6
    # Test “Determine winners” Operation works with reproducible Shuffling

    cardgame = CardGame(card_number=[2, 4, 6], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=1)

    print("Original Cards=", cardgame.cards, '\n')

    cardgame.shuffleCards(seed=1)

    print("Shuffled Cards=", cardgame.cards, '\n')

    print(cardgame.cards)

    cardgame.play()

    cardgame.play()

# Edge Case Test:

elif test_case == 7:
    # Test Case 7
    # Test the case of more than one deck

    cardgame = CardGame(card_number=[2, 4, 6], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=2)

    print("cards=", cardgame.cards, '\n')

    print("suits=", cardgame.suits, '\n')

    print("points=", cardgame.points, '\n')

    print("deck number=", cardgame.deck_number)

elif test_case == 8:
    # Test Case 8
    # Test the case where the number of a suit is less than 1

    cardgame = CardGame(card_number=[2, 0, 6], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=1)

    print("cards=", cardgame.cards, '\n')

    print("suits=", cardgame.suits, '\n')

    print("points=", cardgame.points, '\n')

    print("deck number=", cardgame.deck_number)

elif test_case == 9:
    # Test Case 9
    # Test the case where the card number for suits does not match suits

    cardgame = CardGame(card_number=[2, 4, 6, 3], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=1)

    print("cards=", cardgame.cards, '\n')

    print("suits=", cardgame.suits, '\n')

    print("points=", cardgame.points, '\n')

    print("deck number=", cardgame.deck_number)

elif test_case == 10:
    # Test Case 10
    # Test case where user-assigned suits does not match user-assigned suit-point pairs (number of items do not match)

    cardgame = CardGame(card_number=[2, 4, 6], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'green': 1}, deck_number=1)

    print("cards=", cardgame.cards, '\n')

    print("suits=", cardgame.suits, '\n')

    print("points=", cardgame.points, '\n')

    print("deck number=", cardgame.deck_number)

elif test_case == 11:
    # Test Case 11
    # Test case where user assigned suits do not match user assigned suit-point pairs (terms of items do not match)

    cardgame = CardGame(card_number=[2, 4, 6], suits=['blue', 'yellow', 'green'],
                        points={'red': 3, 'green': 1}, deck_number=1)

    print("cards=", cardgame.cards, '\n')

    print("suits=", cardgame.suits, '\n')

    print("points=", cardgame.points, '\n')

    print("deck number=", cardgame.deck_number)

elif test_case == 12:
    # Test Case 12
    # Test case where there is no card left to deal

    cardgame = CardGame(card_number=[1, 1, 1], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1}, deck_number=1)

    print("cards=", cardgame.cards, '\n')

    deal_card = cardgame.dealCard()

    print("Deal Card=", deal_card)

    deal_card = cardgame.dealCard()

    print("Deal Card=", deal_card)

    deal_card = cardgame.dealCard()

    print("Deal Card=", deal_card)

    deal_card = cardgame.dealCard()

    print("Deal Card=", deal_card)

elif test_case == 13:
    # Test Case 13
    # Test the case where there are duplicates in user-assigned suits

    cardgame = CardGame(card_number=[1, 1, 1], suits=['red', 'red', 'green'],
                        points={'red': 3, 'green': 1}, deck_number=1)

    print('cards=', cardgame.cards, "\n")

elif test_case == 14:
    # Test Case 14
    # Test case where the left cards are not enough to play to get a winner

    cardgame = CardGame(card_number=[2, 1, 3], suits=['red', 'yellow', 'green'],
                        points={'red': 3, 'yellow': 2, 'green': 1},
                        deck_number=1)

    print("Original Cards=", cardgame.cards, '\n')

    cardgame.shuffleCards(seed=1)

    print("Shuffled Cards=", cardgame.cards, '\n')

    print(cardgame.cards)

    cardgame.play()

    cardgame.play()

else:
    raise ValueError("The desired test case number exceeds the maximum case number.")
