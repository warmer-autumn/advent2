#import functions.py
test = 'A Z'
print(test.split())
print(test.encode())
print(test.count(0))
print(test.center(0))


#print(test(0))
#print(test(1))


player=[]
opponent=[]
count=0
test_input = 'A Y B X C Z'
test_input = test_input.split()
while True:
    if count != len(test_input):
        print('input is currently ' + test_input[count]+' at position: '+str(count))
        if (count %2) == 0:
            player.append(test_input[count])
        else:
            opponent.append(test_input[count])
        count+=1
    else:
        break
print(player)
print(opponent)
print('OK BOSS')
