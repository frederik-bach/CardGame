
import random

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def generate_deck(deck):

    for S in SUITS:
        for R in RANKS:
            d_list= []
            first_item = R + " of " + S
            d_list.append(first_item)
            d_list.append(S)
            d_list.append(R)
            
            deck.append(d_list) 
            
        
    return(deck)

deck=[]

deck= generate_deck([])
score = []




def calculate_score(deck):
    
    for list in  (deck):
        for j in list:
            if list[2] == "Ace": 
                 list[2] = int("14")
            if list [2] == "King":
                list[2] = int("13")
            if list [2] == "Queen":
                list[2] = int("12")
            if list [2] == "Jack":
                list[2] = int("11")
            elif list[2] is not ["Ace", "Jack", "Queen", "King"]:
                list[2] = int(list[2])
                
    for list in (deck):
        for j in list:
            if list[1]== "Clubs":
                list[1]= int("1")
            if list[1]== "Diamonds":
                list[1]= int("2")
            if list [1] == "Hearts":
                list[1] = int("3")
            if list [1] == "Spades":
                list[1] = int("4")
                
    for list in (deck) :
        for j in list:
            
            rankscore = (list[2])
            suitscore = (list[1])
            score.append(rankscore + suitscore)     
            
             
    return rankscore + suitscore      

   
print(deck)  

calculate_score(deck)

print(score)
print(deck)

# This method is used to store the score assigned with each card in a dictionary. We will call the calculate_score(card)
# method from here for each card of the deck and store the card as key and its associated score as value in the dictionary.
# Use the first element of the "card" list as key for the dictionary. Dictionary entries will look like this: '2 of Clubs': 3
# and 'Jack of Diamonds': 13.

storing_dic= {}

def store_score(deck):
    i=0 # setting start value = 0 outside of the loop 
    for list in (deck):
        
        for j in list:
            
            storing_dic[list[0]] = score[i] #for the first loop i = 0, then next loop it will equal 1 and so on..
            i= i+1
                
    return storing_dic

store_score(deck)
#Check if it is working 
print("Jack of Hearts: ", storing_dic["Jack of Hearts"])
print("Ace of Spades has the value : ",storing_dic["Ace of Spades"])
print("King of Diamonds has the value : " , storing_dic["King of Diamonds"])

# This method is used for shuffling a copy of the initial deck using the random.randrange() function (see lecture slides).

def shuffle(deck):
    random.shuffle(deck)
    return deck

shuffle(deck)
#works fine
print(deck)

# This method is used for distributing the cards of the shuffled deck to player1 and player2. Hand out the first ten cards
# in an alternating way to the decks of the players, i.e. player1 gets the cards with indices 0,2,4,6,8 and player2
# gets the cards with indices 1,3,5,7,9.
# Hint: use the modulus function '%' to determine whether the current list index is odd or even.
    
deck_player1 =[] #Creating empty lists first, so I can distribute the shuffled cards to them individually 
deck_player2 =[]

def distribute_cards(deck):
    i=0
    for list in (deck):
        
        if i < 10: 
            if deck.index(list) % 2 != 0:
                deck_player1.append(list)
                i= i+1
            elif deck.index(list) % 2 == 0:
                deck_player2.append(list)
                i= i+1
        #assign card to player 1 
        
        
    return deck_player1, deck_player2

distribute_cards(deck)

print("the deck of player1 is : " , deck_player1)
print("the deck of player2 is : " ,deck_player2)
print("the lenght of player2's deck is :",len(deck_player2))
print("the lenght of player1's deck is :",len(deck_player1))

#This method is used for playing one round comparing two cards with each other based on their calculated score.
# Use the dictionary to look up the score for each card. Compare scores, if player1's score is larger than player 2's then
# he/she wins, analogous for player2, or there is a tie if both scores are equal. Return the result as an Integer with:
# 1 means player 1 won, 2 means player 2, 0 means tie. Also, print the result of a round on the console in the form:
# Player 1: 5 of Clubs, score=6
# Player 2: Jack of Hearts, score=14
# Hint: use the format() function for strings to create the output strings..

card1= deck_player1[0]
card2= deck_player2[0]

print("player 1 's first card is : ", card1)
print(storing_dic[str(card1[0])])
winsplayer1=[]
winsplayer2=[]
ties=[]
 
def play_round(card1,card2,storing_dic):
    #card1= deck_player1[0]
    #card2= deck_player2[0]

    if storing_dic[str(card1[0])] > storing_dic[str(card2[0])]:
        res = 1
        print( "Player one plays: ", card1[0], "score: ", storing_dic[str(card1[0])], " ; ",  "Player 2 plays: ", card2[0],
        "score: ", storing_dic[str(card2[0])])
        print("Player 1 wins")
        winsplayer1.append(1)

    if storing_dic[str(card1[0])] < storing_dic[str(card2[0])]:
        res = 2
        print( "Player one plays: ", card1[0], "score: ", storing_dic[str(card1[0])], " ; ", "Player 2 plays: ", card2[0],"score: ",
                                            storing_dic[str(card2[0])])
        print("Player 2 wins")
        winsplayer2.append(1)
    
    if storing_dic[str(card1[0])] == storing_dic[str(card2[0])]:
        res=0
        print( "Player one plays: ", card1[0],"score: ", storing_dic[str(card1[0])], " ; ", "Player 2 plays: ", card2[0],"score: ",
        storing_dic[str(card2[0])])
        print("This is a tie, nobody wins")
        ties.append(1)
      
    
    
    #deck_player1.remove(card1)
    #deck_player2.remove(card2)
    
    return res

#play_round(card1,card2,storing_dic)



# This method is used for simulating a complete game consisting of playing all the cards on player1 and player2's decks,
# i.e. 1 card each in 5 rounds. Call the play_round() function for each round with card1, card2 and the score dictionary
# as input. Use the returned value of th play_round() function to evaluate the result of one round. Print if Player 1 or Player 2
# won the round or there was a Tie on the console.
# Also, keep track of the number of of wins for player 1, player 2 and ties. Similarly to playing one round, return
# the total result of the game, with total=1 meaning that player 1 has won, total=2 meaning that player 2 has won,
# and total=0 meaning nobody has won.
# Print the result of a complete game on the console in the form:
# The total score is: Player 1: 2, Player 2: 3, Ties: 0
# Player 2 wins the game.
# Hint: use the format() function to create the output strings.te the output strings.




def play_game (deck_player1, deck_player2,storing_dic):
    i=0
    for list in deck_player1: #and list in deck_player2: 
        if i < 6:
            play_round(deck_player1[i],deck_player2[i], storing_dic)
            i= i+1 
            if i < 6: 
                wins1 = len(winsplayer1)
                wins2 = len(winsplayer2)
                tiestotal = len(ties) 

    print('The total score is: Player 1: {} wins, Player 2: {} wins, Ties: {}'.format(wins1, wins2, tiestotal))
    if wins1 > wins2:
        print("Player 1 is the winner")
    if wins1 < wins2:
        print("Player 2 is the winner")
    if tiestotal > wins1 and wins2 or wins1 == wins2 :
        print("The players tie")
    
    return deck_player1, deck_player2

play_game(deck_player1, deck_player2, storing_dic)

print(type(deck_player1[0]))

    