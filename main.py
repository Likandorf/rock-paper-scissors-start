rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
rand_index = random.randint(0, len(game) - 1)
rand_choice = game[rand_index]
if player_choice == 0:
  print(game[0])
  print(f"Computer chose:\n {rand_choice}")
  if rand_index == 1:
    print("You lose")
  if rand_index == 2:
    print("You won")
  if rand_index == 0:
    print("It's a tie")
elif player_choice == 1:
  print(game[1])
  print(f"Computer chose:\n {rand_choice}")
  if rand_index == 1:
    print("It's a tie")
  if rand_index == 2:
    print("You lose")
  if rand_index == 0:
    print("You win")
elif player_choice == 2:
  print(game[2])
  print(f"Computer chose:\n {rand_choice}")
  if rand_index == 1:
    print("You won")
  if rand_index == 2:
    print("It's a tie")
  if rand_index == 0:
    print("You lose")