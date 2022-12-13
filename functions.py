
rock = {
    'player': 'A',
    'opponent': 'X',
    'score': 1
}
paper ={
    'player': 'B',
    'opponent':'Y',
    'score': 2
}
scissors ={
    'player':'C',
    'opponent':'Z',
    'score': 3
}
win={
'lose' : 0,
'draw' : 3,
'win' : 6
}

def getinput(file):
    input = open('input.txt', 'r')
    count = 0
    while True:
        if count == 0: 
            line = list.append(file.readline())
        else:
            line = list.append(file.readline())
            

def split_inputs(input):
    player=[]
    opponent=[]
    count=0
    input = input.split()
    while True:
        if count != len(input):
            print('input is currently ' + input[count]+' at position: '+str(count))
            if (count %2) == 0:
                player.append(input[count])
                print(player)
            else:
                opponent.append(input[count])
                print(opponent)
            count+=1
        else:
            break
    return [player, opponent]
        
def matchup(player,opponent):
    count = 0
    total = len(player)
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
        if opponent == paper['opponent']:
            match = win['lose']
        else:
            match = win['win']
        return match+choice
    
    elif player == paper['player']:
        choice = paper['score']
        if opponent == paper['opponent']:
            match = win['draw']
        if opponent == scissors['opponent']:
            match = win['lose']
        else:
            match = win['win']
        return match+choice

    elif player == scissors['player']:
        choice = scissors['score']
        if opponent == scissors['opponent']:
            match = win['draw']
        if opponent == rock['opponent']:
            match = win['lose']
        else:
            match = win['win']
        return match+choice
