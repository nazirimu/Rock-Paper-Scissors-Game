import random

#Graphics for the 3 choices
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

print('Welcome to the rock - paper - scissors game')
pick = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))

choices = [rock, paper, scissors]
print('You picked:')
print(choices[pick])
print('VS')
comp = random.randint(0,2)
selection = choices[comp]
print(selection)

if (selection == rock) and (choices[pick] == paper):
  print('You win!')
elif (selection == paper) and (choices[pick] == rock):
  print('You lose!')
elif (selection == rock) and (choices[pick] == scissors):
  print('You lose!')
elif (selection == scissors) and (choices[pick] == rock):
  print('You Win!')
elif (selection == paper) and (choices[pick] == scissors):
  print('You win!')
elif (selection == scissors) and (choices[pick] == paper):
  print('You lose!')
elif (selection == rock) and (choices[pick] == rock):
  print('Tie game!')
elif (selection == paper) and (choices[pick] == paper):
  print('Tie game!')
else:
  print('Tie game!')

