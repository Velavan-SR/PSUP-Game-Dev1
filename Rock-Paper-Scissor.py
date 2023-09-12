import random
def playGame():
    player_Score = 0
    computer_Score = 0
    items = ['null','Rock','Paper','Scissor']
    print('***ROCK PAPER SCISSORS***')
    no_Of_Rounds = int(input("Please Enter The Number Of Rounds : "))
    for i in range(no_Of_Rounds):
        while True:
            player_Input = input('Enter the corresponding no. of your choice: 1.Rock, 2.Paper, 3.Scissor : ')
            if player_Input not in ['1', '2', '3']:
                print('Please Enter a Valid Input')
            else:
                player_Input = int(player_Input)
                break

        comp_choice = items[random.randint(1,3)]
        print('The computer chose : ',comp_choice)
        if (items[player_Input]=='Rock' and comp_choice=='Paper') or (items[player_Input]=='Paper' and comp_choice=='Scissor') or (items[player_Input]=='Scissor' and comp_choice=='Rock'):
            computer_Score+=1
        elif (items[player_Input]=='Paper' and comp_choice=='Rock') or (items[player_Input]=='Scissor' and comp_choice=='Paper') or (items[player_Input]=='Rock' and comp_choice=='Scissor'):
            player_Score+=1
        else:
            pass
    if player_Score>computer_Score:
        print('Congrats ! You Win !!!')
    elif computer_Score>player_Score:
        print('Computer Wins :(')
    else:
        print('Its A Tie !!')
        
while True:
    playGame()
    choice = input("Enter 'Y' to play the game again , 'N' to quit : ").strip().lower()
    if choice !='y':
        print("Bye-Byeee :)")
        break
