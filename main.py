from art import logo
from replit import clear
import random
import time

play = input("Do you want to play a game of BlackJack? y or n: ")
if play == 'n':
  print("Yes you do, that's why you're here.")
elif play == 'y':
  print("Have fun. :)")
else:
  print("I don't know what language that is but I'll assume you do.")
  
time.sleep(2)
clear()

print(logo)


def deal_to_player():
  global player
  global continue_playing
  global continue_playing_player
  global continue_playing_dealer
  choice = input("Hit? y or n:")
  if choice == "n":
    continue_playing_player = False
    continue_playing_dealer = True
  else:
    player.append(random.choice(cards))
    print(f"Player has: {player}. Total {sum(player)}.")
    if sum(player) > 21:
      print("Bust! You lose.")
      continue_playing_player = False
      continue_playing = False
      continue_playing_dealer = False
    else:
      deal_to_player()
    
def deal_to_dealer():
  global dealer
  global continue_playing
  global continue_playing_dealer
  print(f"Dealer has: {dealer}. Total {sum(dealer)}.")
  if sum(dealer) > 21:
    print("Dealer busts, you win!")
    continue_playing = False
    continue_playing_dealer = False
  elif sum(dealer) < 17:
    dealer.append(random.choice(cards))
    deal_to_dealer()
  else:
    if sum(dealer) > sum(player):
      print("You lose!")
    elif sum(player) > sum(dealer):
      print("You win!")
    elif sum(player) == sum(dealer):
      print("It's a tie.")  
    continue_playing = False
    continue_playing_dealer = False
    

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []
  
  #initial deal
player.append(random.choice(cards))
player.append(random.choice(cards))
dealer.append(random.choice(cards))
dealer.append(random.choice(cards))
print(f"Dealer has: {dealer[0]}.")
print(f"Player has: {player}. Total {sum(player)}.")
continue_playing = False
if sum(player) == 21 and sum(dealer) != 21:
  print("Player has blackjack. You win!")
elif sum(player) == 21 and sum(dealer) == 21:
  print("Player has blackjack but so does dealer. You lose!")
elif sum(dealer) == 21:
  print("Dealer has blackjack. You lose!")
else:
  continue_playing = True
  continue_playing_player = True

while continue_playing == True:
  while continue_playing_player == True:
    deal_to_player()
  
  while continue_playing_dealer == True:
    deal_to_dealer()
    

    





  



    