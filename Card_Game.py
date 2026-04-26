import random

import time


def Game_menu():
    print("""Welcome to card game, you have the following options: 
    1. start game 
    2. pick a card 
    3. shuffle deck 
    4. show my cards 
    5. check win or lose 
    6. exit

    enter space

    Which suits do you want:
    enter 1 for ["♥", "♦", "♣", "♠"]
    enter 2 for ["😃", "😈", "😵", "🤢", "😨"]
    enter 3 for ["🤡", "👹", "👺", "👻", "👽", "👾", "🤖"]:

    """)


def Create_Deck(suits):
    deck = []
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    if suits == "1":
        suit = ["♥", "♦", "♣", "♠"]
    elif suits == "2":
        suit = ["😃", "😈", "😵", "🤢", "😨"]
    elif suits == "3":
        suit = ["🤡", "👹", "👺", "👻", "👽", "👾", "🤖"]
    for i in range(0, len(suit)):
        for j in range(0, len(values)):
            deck.append(f"{values[j]}{suit[i]}")
    return deck


def Pick_Card(deck):
    card_index = random.randint(0, len(deck) - 1)
    card = deck.pop(card_index)
    return card


def Shuffle_Deck(deck):
    random.shuffle(deck)


def Check_Result(p, r, suit):
    # Check 1 for PLAYER win
    count_same_p = {}
    for card in p:
        if card[0] in count_same_p:
            count_same_p[card[0]] += 1
        else:
            count_same_p[card[0]] = 1
    for card in count_same_p:
        if count_same_p[card] == 4:
            return True

    # Check 1 for ROBOT win
    count_same_r = {}
    for card in r:
        if card[0] in count_same_r:
            count_same_r[card[0]] += 1
        else:
            count_same_r[card[0]] = 1
    for card in count_same_r:
        if count_same_r[card] == 4:
            return False

    suit_1 = len(suit) - 1
    # Check 2 for PLAYER win
    for card in p:
        if count_same_p[card] == suit_1:
            return True

    # Check 2 for ROBOT win
    for card in r:
        if count_same_r[card] == suit_1:
            return False

    # check 3 for PLAYER win
    secsuit = suit[1]
    player_2 = 0
    for i in range(0, len(p)):
        if p[i][1] == secsuit:
            player_2 += 1
            print("The player won by having more cards from the second suit than the robot")
            return True
        elif L > K:
            print("The robot won by having more cards from the second suit than the player")
            return False

    # check 3 for PLAYER win
    secsuit = suit[1]
    K = 0
    L = 0
    for i in range(0, len(p)):
        if p[i][1] == secsuit:
            K += 1
        if r[i][1] == secsuit:
            L += 1
        if K > L:
            print("The player won by having more cards from the second suit than the robot")
            return True
        elif L > K:
            print("The robot won by having more cards from the second suit than the player")
            return False
    # check 4
    averagep = 0
    averager = 0
    for i in range(0, len(p)):
        averagep += p[i][0]
        averager += r[i][0]
    averagep / len(p)
    averager / len(r)
    if averagep > averager:
        print("The player won by having an average score higher than the robot's")
    else:
        print("The robot won by having an average score higher than the player's")


def Play_Game():  # 1. start game 2. pick a card 3. shuffle deck 4. show my cards 5. check win or lose 6. exit
    deck = []
    suit = []
    suits_options = {"1": ['♥', '♦', '♣', '♠'],
                     "2": ['😀', '😈', '😵', '🤢', '😨'],
                     "3": ['🤡', '👹', '👺', '👻', '👽', '👾', '🤖']}
    player_cards = []
    robot_cards = []
    while True:
        Game_menu()
        ask = input("Please enter your selection:")
        asks = ask.split()
        if len(asks) > 1:
            ask1 = asks[0]
            ask2 = asks[1]
        else:
            ask1 = asks[0]
            ask2 = "1"
        if ask1 == "1":
            suit = suits_options[ask2]
            deck = Create_Deck(ask2)
            print("Deck:", deck)
        elif ask1 == "2":
            if len(player_cards) < 6:
                player_cards.append(Pick_Card(deck))
                robot_cards.append(Pick_Card(deck))
            else:
                print("You already have 6 cards.")
                time.sleep(0.5)
        elif ask1 == "3":
            Shuffle_Deck(deck)
        elif ask1 == "4":
            print("Player Cards:", player_cards)
            time.sleep(1)
        elif ask1 == "5":
            Check_Result(player_cards, robot_cards, suit)
        else:
            exit()


Play_Game()