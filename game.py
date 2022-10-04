import random
turns = ['akmens', 'papīrs', 'šķēres']
human_turns = []
computer_turns = []

while(True):
    human_turn = input('Enter your turn, or type exit:')
    computer_turn = random.choice(turns)

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)
    
    print(f'Human:{human_turn} vs.:{computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')

    if human_turn == 'exit':
        print('Thank you for playing! Bye, bye')
        break

    elif human_turn == 'akmens' and computer_turn == 'šķēres':
        print('Human wins!')
    elif human_turn == 'papīrs' and computer_turn == 'akmens':
        print('Human wins!')
    elif human_turn == 'šķēres' and computer_turn == 'papīrs':
        print('Human wins!')

    else: 
        print('Computer wins!')

print(f'You have played {len(human_turns)} times')
print(human_turns)
print(computer_turns)
