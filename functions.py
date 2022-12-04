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
player=[]
opponent=[]

def getinput(file):
    input = open('input.txt', 'r')
    count = 0
    while True:
        if count == 0: 
            line = list.append(file.readline())
        else:
            line = list.append(file.readline())
            

def split_inputs(input):
    count=0
    input = input.split()
    while True:
        if count != len(input):
            print('input is currently ' + input[count]+' at position: '+str(count))
            if (count %2) == 0:
                player.append(input[count])
            else:
                opponent.append(input[count])
            count+=1
        else:
            break
        

