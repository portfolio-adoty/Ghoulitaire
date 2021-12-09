"""
Solitaire Prototype v1.0
Autor: Andi Doty
Date: November 17, 2021
"""

import random

deck = [[1, "C"], [2, "C"], [3, "C"], [4, "C"], [5, "C"],
     [6, "C"], [7, "C"], [8, "C"], [9, "C"], [10, "C"],
	 [11, "C"], [12, "C"], [13, "C"],
	 [1, "D"], [2, "D"], [3, "D"], [4, "D"], [5, "D"],
     [6, "D"], [7, "D"], [8, "D"], [9, "D"], [10, "D"],
	 [11, "D"], [12, "D"], [13, "D"],
	 [1, "H"], [2, "H"], [3, "H"], [4, "H"], [5, "H"],
     [6, "H"], [7, "H"], [8, "H"], [9, "H"], [10, "H"],
	 [11, "H"], [12, "H"], [13, "H"],
	 [1, "S"], [2, "S"], [3, "S"], [4, "S"], [5, "S"],
     [6, "S"], [7, "S"], [8, "S"], [9, "S"], [10, "S"],
	 [11, "S"], [12, "S"], [13, "S"]]

numCards = 52

drawPile = []
discardPile = []

buildPileC = []
buildPileD = []
buildPileH = []
buildPileS = []

board = [[], [], [], [], [], [], []]

def shuffle():

    for i in range(numCards):

        r = i + (random.randint(0,55) % (numCards -i))
        tmp = deck[i]

        deck[i] = deck[r]
        deck[r] = tmp

    return deck

def deal(cards):

    for i in range(28):

        if i < 1:

            board[0].append(cards[i])

        elif i < 3:

            board[1].append(cards[i])

        elif i < 6:

            board[2].append(cards[i])

        elif i < 10:

            board[3].append(cards[i])

        elif i < 15:

            board[4].append(cards[i])

        elif i < 21:

            board[5].append(cards[i])

        else:

            board[6].append(cards[i])

    for i in range(28, 52):

        drawPile.append(cards[i])

def drawCard():

    discardPile.insert(0, drawPile[0])
    drawPile.pop(0)

def printBoard():

    nums = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}
    suits = {"C":" of Clubs", "D": " of Diamonds", "H": " of Hearts", "S":" of Spades"}

    print("Discard Pile:")
    if len(discardPile) > 0:

        print(nums[discardPile[0][0]] + suits[discardPile[0][1]])

    else:

        print("None")

    print(" ")

    c = 1
    r = 1

    for col in board:

        print("Column " + str(c) + ":")
        r = 1

        for card in col:

            if r == len(col):
                print(nums[card[0]] + suits[card[1]])
            else:
                print("?")
            r += 1

        c += 1
        print(" ")

def moveChoice():

    colors = {"C": "Black", "D": "Red", "H": "Red", "S": "Black"}

    print("Which card would you like to move? (Please choose a column between 1-7)")
    col = input()

    if int(col) > 7 or int(col) < 1:

        print("Please input a number between 1-7!")

    card = board[int(col)-1][len(board[int(col)-1])-1] #The bottom card.
    print("Card to move: " + str(card))

    print("Where would you like to move it? (Please choose a column between 1-7)")
    newCol = input()

    if int(newCol) > 7 or int(newCol) < 1:

        print("Please input a number between 1-7!")

    else:

        newCard = board[int(newCol)-1][len(board[int(newCol)-1])-1] #The bottom card.
        print("Card to place on: " + str(newCard))

        if newCard[0] == card[0] + 1 and colors[card[1]] != colors[newCard[1]]:

            print("You can place this card here!")
            moveCard(card, newCard)

        else:

            if newCard[0] != card[0] + 1:

                print("The parent card must be one value higer than the card you're moving!")
                moveChoice()

            if colors[card[1]] == colors[newCard[1]]:

                print("The colors of the two cards cannot match!")
                moveChoice()

def moveCard(cardToMove, newCardLocation):

    for col in range(len(board)):

        for card in range(len(board[col])):
            print("Card to be placed on: " + str(board[col][card]))
            print("Key: " + str(newCardLocation))

            if board[col][card] == newCardLocation:

                print("card moved")
                board[col].append(cardToMove)

            if board[col][card] == cardToMove:

                print("get rid of old card")
                board[col].pop(card)

    printBoard()
    moveChoice()

deal(shuffle())
printBoard()

drawCard()
printBoard()

moveChoice()




