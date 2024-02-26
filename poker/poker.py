class Card:
    suit = ""
    value = 0
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    deck = set()

    def __init__(self):
        for s in { "Spades", "Clubs", "Hearts", "Diamonds" }:
            for v in range(1,14):
                self.deck.add(Card(s,v))
    
    def get_card(self):
        return self.deck.pop()

class Player:
    name = ""
    hand = set()

    def __init__(self,name):
        self.name = name
    
    def say_hi(self):
        print("Hi, my name is {}".format(self.name))
    
    def deal_hand(self,hand=set()):
        self.hand = hand
    
    def say_hand(self):
        print(self.hand)
   
players = set()
p_name = ""
while p_name != "s":
    p_name = input("Enter player name or [s] to start game: ")
    if p_name != "s":
        players.add(Player(p_name))

print("There are {} players".format(len(players)))


    

