import random
from assets import logo


print(logo + '\n')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def end(player_cards, computer_cards):
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)
    
    c_final_score = 21-computer_score
    p_final_score = 21-player_score
        
    if player_score > 21 or c_final_score < p_final_score and computer_score < 21:
        print(f" Your cards: {player_cards}, score: {player_score}")
        print(f" Computer cards: {computer_cards}, score: {computer_score}")
        print(" YOU LOSE :-(\n")
    elif player_score == computer_score:
        print(f" Your cards: {player_cards}, score: {player_score}")
        print(f" Computer cards: {computer_cards}, score: {computer_score}")
        print(" IT'S A DROW :O \n")
    elif computer_score > 21 or c_final_score > p_final_score:
        print(f" Your cards: {player_cards}, score: {player_score}")
        print(f" Computer cards: {computer_cards}, score: {computer_score}")
        print("YOU WIN!:-)\n")

def game():
    your_cards = []
    computer_cards = []
    wanna_play = input("\nDo you want to play a game of BLACKJACK? (y/n): ")
    if wanna_play == 'y':
        your_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))
        score = 0 
        

        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        print(f" Your cards: {your_cards}, current score is: {sum(your_cards)}")
        print(f" Computer first card is {computer_cards[0]}")
        print("")
        if sum(your_cards) == 21:
            print("_"*5)
            print("You have luck! Your score is 21. You hit the blackjack!")
            print("_"*5)
            play_again = input("Do you want to play again? (y/n): ")
            if play_again == 'y':
                game()
        continue_playing = input("Type 'y' to get another card or type 'n' to pass: ")
        if continue_playing == 'y':
            your_cards.append(random.choice(cards))
            score = sum(your_cards)
            if score > 21 and 11 in your_cards:
                your_cards.remove(11)
                your_cards.append(1)
                end(your_cards, computer_cards)
                play_again = input("Do you want to play again? (y/n): ")
                if play_again == 'y':
                    game()
            else:
                end(your_cards, computer_cards)
                play_again = input("Do you want to play again? (y/n): ")
                if play_again == 'y':
                    game()
        elif continue_playing == 'n':
            end(your_cards, computer_cards)
            play_again = input("Do you want to play again? (y/n): ")
            if play_again == 'y':
                game()
    
        

game()