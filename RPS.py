import random

choices = ['rock', 'paper', 'scissors']
player_choice = input("Select your choices: ").lower()

while player_choice not in choices:
  print("Invalid choice. Try again!")
  player_choice = input("Select your choices: ").lower()

  computer_choice = random.choice(choices)
  print(f"Your Choice: {player_choice}")
  print(f"Comoputer Choice: {computer_choice}")

  if player_choice == computer_choice:
    print("It's the same choice!")
  elif (player_choice =='rock' and computer_choice == 'scissors') or\
       (player_choice =='paper' and computer_choice == 'rock') or\
       (player_choice =='scissors' and computer_choice == 'paper'):
          print ("You Win🫨🫨!!!!!")
  else:
    print("You Lose 🫨😂")