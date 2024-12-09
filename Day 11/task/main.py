import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 11 is Ace
    return random.choice(cards)


def calculate_score(hand):
    """Calculates the score of the given hand."""
    # Check for a Blackjack (Ace + 10)
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Return 0 to represent Blackjack

    # Handle the case where Ace (11) should be counted as 1
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(player_score, dealer_score):
    """Compares the final scores of player and dealer."""
    if player_score == dealer_score:
        return "It's a draw. 🙃"
    elif dealer_score == 0:
        return "Lose, the dealer has Blackjack. 😱"
    elif player_score == 0:
        return "Win with a Blackjack! 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Dealer went over. You win! 😁"
    elif player_score > dealer_score:
        return "You win! 😃"
    else:
        return "Dealer wins. 😤"


def play_blackjack():
    print("Welcome to Blackjack!")
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != 'y':
        return

    # Initialize hands
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Calculate initial scores
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # If either the player or dealer has a Blackjack (0), game ends immediately
    if player_score == 0 or dealer_score == 0:
        game_over = True
    else:
        game_over = False

    # Player's turn
    while not game_over:
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score > 21:
            game_over = True
        else:
            # Let the player choose to hit or stand
            player_should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_should_continue == "y":
                player_hand.append(deal_card())
                player_score = calculate_score(player_hand)
            else:
                game_over = True

    # Dealer's turn (dealer must draw until they reach at least 17)
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    # Final hands and scores
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))


# Main loop to allow multiple games
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_blackjack()