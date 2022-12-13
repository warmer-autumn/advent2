
rock = {
    'player': 'X',
    'opponent': 'A',
    'score': 1
}
paper ={
    'player': 'Y',
    'opponent':'B',
    'score': 2
}
scissors ={
    'player':'Z',
    'opponent':'C',
    'score': 3
}
win={
'lose' : 0,
'draw' : 3,
'win' : 6
}

def getinput(file):
    read = open('input.txt', 'r')
    #read = open(file, 'r')
    read = read.read().replace('\n', ' ')
    print(read)
    count = 0
    return read

def split_inputs(input):
    player=[]
    opponent=[]
    count=0
    input = input.split()
    while True:
        if count != len(input):
            print('input is currently ' + input[count]+' at position: '+str(count))
            if (count %2) == 0:
                opponent.append(input[count])
                #print(player)
            else:
                player.append(input[count])
                #print(opponent)
            count+=1
        else:
            break
    return [player, opponent]
        
def matchup(player,opponent):
    count = 0
    total = len(opponent)
    total2 = 0
    while count != total:
        math = rps(player[count],opponent[count])
        #win = math['win']
        #choice = math['choice']
        total2 += math
        count+=1
    print(total2)
    return total2

def rps(player, opponent):

    if player == rock['player']:
        choice = rock['score']
        if opponent == rock['opponent']:
            match = win['draw']
            return match+choice
        if opponent == paper['opponent']:
            match = win['lose']
            return match+choice
        else:
            match = win['win']
        return match+choice
    
    elif player == paper['player']:
        choice = paper['score']
        if opponent == paper['opponent']:
            match = win['draw']
            return match+choice
        if opponent == scissors['opponent']:
            match = win['lose']
            return match+choice
        else:
            match = win['win']
        return match+choice

    elif player == scissors['player']:
        choice = scissors['score']
        if opponent == scissors['opponent']:
            match = win['draw']
            return match+choice
        if opponent == rock['opponent']:
            match = win['lose']
            return match+choice
        else:
            match = win['win']
        return match+choice
    