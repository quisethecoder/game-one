# Steps
# 1. Ask player one to choose rock paper or scissors
# 2. Ask player two to choose rock paper or scissors
# 3. display a message saying who won
# 4. if it's a tie display a message that it is a tie
import random

name_one = input("Player one, what is your name?: ")
name_two = input("Player two, what is your name?: ")

menu_player_one = (f"""{name_one}, Choose an option.
1. Rock
2. Paper
3. Scissors
4. Choose for me
Select [1-4]: """)

menu_player_two = (f"""{name_two}, Choose an option.
1. Rock
2. Paper
3. Scissors
4. Choose for me
select [1-4]: """)

option_player_one = input(menu_player_one)
option_player_two = input(menu_player_two)

while option_player_one not in ["1","2","3","4"] or option_player_two not in ["1","2","3","4"]:
    if option_player_one not in ["1","2","3","4"]:
        print(f"{name_one}, please enter a valid option for player 1, you chose {option_player_one}")
        option_player_one = input(menu_player_one)
    if option_player_two not in ["1","2","3","4"]:
        print(f"{name_two}, please enter a valid option for player 2, you chose {option_player_two}")
        option_player_two = input(menu_player_two)

option_player_one = int(option_player_one)
option_player_two = int(option_player_two)

if option_player_one == option_player_two and option_player_one < 4:
    print("It's a tie!")
elif option_player_one == 1 and option_player_two == 2:
    print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
    print(f"{name_two} Wins!")
elif option_player_one == 1 and option_player_two == 3:
    print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
    print(f"{name_one} Wins!")
elif option_player_one == 2 and option_player_two ==1:
    print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
    print(f"{name_two} Wins!")
elif option_player_one == 2 and option_player_two == 3:
     print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
     print(f"{name_two} Wins!")
elif option_player_one == 3 and option_player_two == 1:
     print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
     print(f"{name_one} Wins!")
elif option_player_one == 3 and option_player_two == 2:
     print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
     print(f"{name_one} Wins!")
elif option_player_one == 4 and option_player_two == 1:
    player_one_random = random.randint(1,3)
    option_player_one = player_one_random
    print(f"We chose {option_player_one} for {name_one}.")
    if option_player_one == option_player_two:
        print("It's a tie!")
    elif option_player_one == 1 and option_player_two == 2:
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_two} Wins!")
    elif option_player_one == 1 and option_player_two == 3:
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_one} Wins!")
    elif option_player_one == 2 and option_player_two ==1:
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_two} Wins!")
    elif option_player_one == 2 and option_player_two == 3:
         print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
         print(f"{name_one} Wins!")
    elif option_player_one == 3 and option_player_two == 1:
         print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
         print(f"{name_one} Wins!")
    else: 
        option_player_one == 3 and option_player_two == 2
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_two} Wins!")
elif option_player_one == 4 and option_player_two == 2:
    player_one_random = random.randint(1,3)
    option_player_one = player_one_random
    print(f"We chose {option_player_one} for {name_one}.")
    if option_player_one == option_player_two:
        print("It's a tie!")
    elif option_player_one == 1 and option_player_two == 2:
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_two} Wins!")
    elif option_player_one == 1 and option_player_two == 3:
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_one} Wins!")
    elif option_player_one == 2 and option_player_two ==1:
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_two} Wins!")
    elif option_player_one == 2 and option_player_two == 3:
         print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
         print(f"{name_one} Wins!")
    elif option_player_one == 3 and option_player_two == 1:
         print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
         print(f"{name_one} Wins!")
    else: 
        option_player_one == 3 and option_player_two == 2
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_two} Wins!")
elif option_player_one == 4 and option_player_two == 3:
    player_one_random = random.randint(1,3)
    option_player_one = player_one_random
    print(f"We chose {option_player_one} for {name_one}.")
    if option_player_one == option_player_two:
        print("It's a tie!")
    elif option_player_one == 1 and option_player_two == 2:
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_two} Wins!")
    elif option_player_one == 1 and option_player_two == 3:
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_one} Wins!")
    elif option_player_one == 2 and option_player_two ==1:
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_two} Wins!")
    elif option_player_one == 2 and option_player_two == 3:
         print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
         print(f"{name_one} Wins!")
    elif option_player_one == 3 and option_player_two == 1:
         print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
         print(f"{name_one} Wins!")
    else: 
        option_player_one == 3 and option_player_two == 2
        print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
        print(f"{name_two} Wins!")                
elif option_player_one == 1 and option_player_two == 4:
      player_two_random = random.randint(1,3)
      option_player_two = player_two_random
      print(f"We chose {player_two_random} for {name_two}")
      if option_player_two == option_player_one:
           print("It's a tie!")
      elif option_player_one == 1 and option_player_two == 2:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      elif option_player_one == 1 and option_player_two == 3:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_one} Wins!")
      elif option_player_one == 2 and option_player_two ==1:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      elif option_player_one == 2 and option_player_two == 3:
           print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
           print(f"{name_one} Wins!")
      elif option_player_one == 3 and option_player_two == 1:
           print(f"{name_one}chose {option_player_one} and {name_two} chose {option_player_two}")
           print(f"{name_one} Wins!")
      else: 
          option_player_one == 3 and option_player_two == 2
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
elif option_player_one == 2 and option_player_two == 4:
      player_two_random = random.randint(1,3)
      option_player_two = player_two_random
      print(f"We chose {player_two_random} for {name_two}")
      if option_player_two == option_player_one:
           print("It's a tie!")
      elif option_player_one == 1 and option_player_two == 2:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      elif option_player_one == 1 and option_player_two == 3:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_one} Wins!")
      elif option_player_one == 2 and option_player_two ==1:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      elif option_player_one == 2 and option_player_two == 3:
           print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
           print(f"{name_one} Wins!")
      elif option_player_one == 3 and option_player_two == 1:
           print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
           print(f"{name_one} Wins!")
      else: 
          option_player_one == 3 and option_player_two == 2
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")  
elif option_player_one == 3 and option_player_two == 4:
      player_two_random = random.randint(1,3)
      option_player_two = player_two_random
      print(f"We chose {player_two_random} for {name_two}")
      if option_player_two == option_player_one:
           print("It's a tie!")
      elif option_player_one == 1 and option_player_two == 2:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      elif option_player_one == 1 and option_player_two == 3:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      elif option_player_one == 2 and option_player_two ==1:
          print(f"{name_one}chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      elif option_player_one == 2 and option_player_two == 3:
           print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
           print(f"{name_one} Wins!")
      elif option_player_one == 3 and option_player_two == 1:
           print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
           print(f"{name_one} Wins!")
      else: 
          option_player_one == 3 and option_player_two == 2
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")                  
elif option_player_one == 4 and option_player_two == 4:
      player_two_random = random.randint(1,3)
      option_player_two = player_two_random
      player_one_random = random.randint(1,3)
      option_player_one = player_one_random
      print(f"We chose {player_one_random} for {name_one}")
      print(f"We chose {player_two_random} for {name_two}")
      if option_player_two == option_player_one:
           print("It's a tie!")
      elif option_player_one == 1 and option_player_two == 2:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      elif option_player_one == 1 and option_player_two == 3:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_one} Wins!")
      elif option_player_one == 2 and option_player_two ==1:
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      elif option_player_one == 2 and option_player_two == 3:
           print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
           print(f"{name_one} Wins!")
      elif option_player_one == 3 and option_player_two == 1:
           print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
           print(f"{name_one} Wins!")
      else: 
          option_player_one == 3 and option_player_two == 2
          print(f"{name_one} chose {option_player_one} and {name_two} chose {option_player_two}")
          print(f"{name_two} Wins!")
      

# Step Sequence
# 1. Give player 1 a menu option to choose betwwen rock paper or scissors
# Player 1 choose.
# 1. rock
# 2. paper
# 3. scissors
# 4. Choose for me
# select [1-4]: 4
# Make sure it's a valid entry only numbers 1-4
# 2. Do the same thing for player 2
# Going to need a loop for the options
# after players choose a message with the winner or tie should appear

# rock beats scissors 
# paper beats rock
# scisoors beats paper
# so if player 1 chose rock and player 2 picks papere then print player two wins







