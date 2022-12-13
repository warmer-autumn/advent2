from functions import *
test_input = 'A Z C Y B X'
print(test_input)
strategies = split_inputs(test_input)
player=strategies[0]
opponent=strategies[1]
print(player)
print('\n')
print(opponent)
print('\n')
#successfully got outputs from function
#need to create another function to run Rock paper Scissors
print(matchup(player, opponent))

print('finished')