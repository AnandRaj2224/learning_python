from random import shuffle as shuff

class Card:

    permitted_cards = ["Hearts", "Diamonds", "Clubs","Spades"]
    permitted_card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs","Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit,value) for value in values for suit in suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards"
    
    def count(self):
        return len(self.cards)
    
    def _deal(self,num_to_remove):
        count = self.count()
        if count == 0:
            raise ValueError("All cards have been dealt\n")
        
        num_to_remove = min([count,num_to_remove])
        dealt = []
        while num_to_remove != 0:
            dealt.append(self.cards.pop(-1))
            num_to_remove -=1
        
        return dealt
    
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.\n")
        shuff(self.cards)
    
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self,hand_size):
        return self._deal(hand_size)


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(5)
print(hand)