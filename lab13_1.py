import random

class KARD:
    def __init__(self):
        self.suits = ['♥', '♦', '♣', '♠']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [(value, suit) for suit in self.suits for value in self.values]

        self.count = len(self.cards)
        
    def shuffle(self):
        random.shuffle(self.cards)       
        
    def remove_card(self):
        if self.count > 0:
            self.count -= 1
            card = self.cards.pop()
            print('Видалена карта: ', card)
            return card
        else:
            return None
        
deck = KARD()
deck.shuffle()
N = int(input("Кількість гравців: "))
cards_per_player = int(input("Карт на гравця: "))
players = [[] for _ in range(N)]

if N * cards_per_player <= deck.count:
    for i in range(cards_per_player):
        for j in range(N):
            card = deck.remove_card()
            players[j].append(card)

    for i in range(N):
        print(f"Гравець {i + 1}: {players[i]}")

else:
    print("Недостатньо карт у колоді!")