import random

def RPS_game(user_choice, computer_choice):
    if (user_choice == computer_choice): # Rock vs Rock or Paper vs Paper or Scisssor vs Scissor
        return 0     #-> No one wins
    
    elif (user_choice == 'R' and computer_choice == 'S'): # Rock vs Scissor
        return 1     #-> Rock wins
    
    elif (user_choice == 'P' and computer_choice == 'R'): # Paper vs Rock
        return 1     #-> Paper wins
    
    elif (user_choice == 'S' and computer_choice == 'P'): # Scissor vs Paper
        return 1     #-> Scissor wins
    
    elif (user_choice == 'S' and computer_choice == 'R'): # Scissor vs Rock
        return -1    #-> Rock wins    
    
    elif (user_choice == 'P' and computer_choice == 'S'): # Paper vs Scissor
        return -1    #-> Scissor wins
    
    elif (user_choice == 'R' and computer_choice == 'P'): # Rock vs Paper
        return -1    #-> Paper wins

play = 0 
computer_choice = 0    
user_choice = 0

print("*********************** Welcome to Rock Paper Scissor Game ***********************\n")

print("\t\t\t RULES of the Game are as follows: -")
print("-> The Game will be played between the Computer and You.")
print("-> Each player simultaneously forms one of three shapes: Rock(R) / Paper(P) / Scissor(S)")
print("-> The winner of the game is decided as per the below rules: -\n")
print("-> Rock vs Paper -> Paper wins")
print("-> Rock vs Scissor -> Rock wins")
print("-> Paper vs Scissor -> Scissor wins")
print("-> Rock vs Rock or Paper vs Paper or Scisssor vs Scissor -> No one wins")
print("-> In this game, the user will be asked to make choice and according to the choice of user and computer and then the result will be displayed along with the choices of both computer and user.\n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEST OF LUCK !! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

play = int(input("\t\tDo you want to play ? \n\t\tEnter 1 for \"YES\" \n\t\tEnter 0 for \"NO\"\n"));

while (play>0):

    print("\n\n########################## Game Starts ##########################\n\n");

    num = random.randint(0,2)

    if (num == 0):
        computer_choice = 'R'
        
    elif (num == 1):
        computer_choice = 'P'
        
    else:
        computer_choice = 'S'

    user_choice = input("\n\nEnter R for ROCK, P for PAPER and S for SCISSOR\n")
    if (user_choice == 'R') and computer_choice == 'R':
        print ('''You chose rock and computer also chose rock
   _______        _______
---'   ____)      (______ '---
       (_____)   (_____)
       (_____)   (_____)
       (____)     (____)
---.___(___)       (___)___.--
''')
    elif (user_choice == 'P'):
        print ('''You chose Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
        
    elif (user_choice == 'S'):
        print('''You chose Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        

    result = RPS_game(user_choice, computer_choice)
    if (result == 0):
        print("\nThis Game is a Draw, No-one wins!!\n")
        
    elif (result == -1):
        print("\nThis Game is won by Computer!!\n")
        
    else: #result == 1
        print("\nThis Game is won by you!!\n")

    print("\n############################ Game ends ############################\n")

    play = int(input("\n\t\tDo you want to play again? \n\t\tEnter 1 for \"YES\" \n\t\tEnter 0 for \"NO\""))


print("Terminating the Game")
