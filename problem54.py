f = open('')
for line in f:
    hands = line.split()
    player1 = hands[:5]
    player2 = hands[5:]



def rank(hand):
    a1,a2,a3,a4,a5 = hand
    
    
