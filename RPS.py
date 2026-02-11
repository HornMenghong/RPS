import random

choices = ['rock', 'paper', 'scissors']
player_choice = input("Select your choices: ").lower()

while player_choice not in choices:
  print("Invalid choice. Try again!")
  player_choice = input("Select your choices: ").lower()