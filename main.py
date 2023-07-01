import random

deck = [
    "Spade 1", "Spade 2", "Spade 3", "Spade 4", "Spade 5", "Spade 6", "Spade 7", "Spade 10",
    "Club 1", "Club 2", "Club 3", "Club 4", "Club 5", "Club 6", "Club 7", "Club 10",
    "Heart 1", "Heart 2", "Heart 3", "Heart 4", "Heart 5", "Heart 6", "Heart 7", "Heart 10",
    "Diamond 1", "Diamond 2", "Diamond 3", "Diamond 4", "Diamond 5", "Diamond 6", "Diamond 7", "Diamond 10"
]

def deal_cards():
    random.shuffle(deck)
    player1_hand = deck[:3]
    player2_hand = deck[3:6]
    return player1_hand, player2_hand

def play_round(player1_hand, player2_hand):
    player1_card = random.choice(player1_hand)
    player2_card = random.choice(player2_hand)
    print("Player 1 plays:", player1_card)
    print("Player 2 plays:", player2_card)
    
    if player1_card > player2_card:
        print("Player 1 wins the round")
    elif player1_card < player2_card:
        print("Player 2 wins the round")
    else:
        print("Round is a tie")

player1_hand, player2_hand = deal_cards()
print("Player 1's hand:", player1_hand)
print("Player 2's hand:", player2_hand)
print("Game starts...\n")

for _ in range(3):
    play_round(player1_hand, player2_hand)
    print()

print("End of the game")