from functions import *


filename=print('Please input file name: ')
input = getinput(filename)
strategies = split_inputs(input)
player=strategies[0]
opponent=strategies[1]

matchup(player, opponent)

print('finished')