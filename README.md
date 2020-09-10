# Card-Game
A Card Game Designed in Python 3

Design Assumptions:
  1) User can assign the number of decks to play, which should be at least 1.
  2) User can assign suit types in a deck while the assigned suit type should be unique, e.g. suits = ['red', 'yellow', 'green'], suits = [‘spade’, ‘club’, ‘heart’, ‘diamond’] are valid, while suits = ['red', red, 'green'] will induce an Error.
  3) When initiated, each suit has user-assigned number of cards, which can be same or different to other suits. The range of the number on a card of one suit is [0, total number of cards of the suit - 1]
  4) User can assign suit-point matching pattern to calculate points in the play, e.g. points = {'red': 3, 'yellow': 2, 'green': 1}
  5) There is one type of deck of cards in each play, and different decks of cards can not mix in a play.
  
Classes Design:
There are two classes designed.
  1) Class Card: A class to represent a deck of cards with assigned suits and number of cards for each suit.
  2) Class CardGame: A class to represent a card game with randomly shuffle, deal a card from top, sort in assigned order, and play methods, which supporting 2 players to determine a winner. 

The relationship between class CardGame and class Card is composition. A CardGame object has at least one Card object to play. 
  
Methods Design:
The designed Card Game supports 3 operations and two players can play the game.
  1) Shuffle cards in the deck: randomly mix the cards in the card deck, and return a whole deck of cards with a mixed order.
  2) Get a card from the top of the deck: get one card from top of the card deck, return a card, and if there is no card left in the deck return error or exception.
  3) Sort cards: take a list of color as parameter and sort the card in that color order. Numbers should be in ascending order.  
      
      For example, if the deck has a card contains with following order  
          
          (red, 1), (green, 5), (red, 0), (yellow, 3), (green, 2) 
      
      Sort cards([yellow, green, red]) will return the cards with following order 
          
          (yellow, 3), (green, 0), (green, 5), (red, 0), (red, 1) 

Note:
1) The Card Game Source file refers to "Card Game Source Files/CardGame.py".
2) The Test Case Source file refers to "Card Game Source Files/test_case.py"
3) The game design is documented in the file "Card Game Design Documentation.pdf"
4) The API usage is documented in the file "Card Game API Documentation.pdf"
5) The test cases are sumarized in the file "Test Cases.pdf"
6) The code interview question is in the file "Code Interview Question.pdf"

If there is any question, please feel free to teach out to Brian(Kangjian) Ma (kangjianma@gmail.com).

