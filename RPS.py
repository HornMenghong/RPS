import random

running = True
choices = ['rock', 'paper', 'scissors']

player_score = 0
Computer_score = 0
while running:
  player_choice = input("Select your choices: ").lower().strip()
  while player_choice not in choices:
    print("Invalid choice. Try again!")
    player_choice = input("Select your choices: ").lower()

  computer_choice = random.choice(choices)
  print(f"Your Choice: {player_choice}")
  print(f"Computer Choice: {computer_choice}")

  if player_choice == computer_choice:
    print("It's the same choice!")
  elif (player_choice =='rock' and computer_choice == 'scissors') or\
        (player_choice =='paper' and computer_choice == 'rock') or\
        (player_choice =='scissors' and computer_choice == 'paper'):
          print ("You Win🫨🫨!!!!!")
          player_score += 1
  else:
    print("You Lose 🫨😂")
    Computer_score += 1

  if player_score == 2:
      print("player Victory😁")
      running = False
  elif Computer_score == 2:
    print ("Bot victory😒")
    running = False

    
   