f=open('02/input.txt','r')
#l=[x.split(' ') for x in f.read().split("\n")]
ls=f.read().split("\n")
s=0
r={'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z':9, 'C X':7, 'C Y':2, 'C Z':6}
for m in ls:
    s+=r[m]
print(s)


'''
#r={'A X':3+1, 'A Y':6+2, 'A Z':0+3, 'B X':0+1, 'B Y':3+2, 'B Z':6+3, 'C X':6+1, 'C Y':0+2, 'C Z':3+3}
'C X', 'A Y', 'B Z', 'B Y', 'A Z', 'B X', 'C Y', 'C Z', 'A X'
Opp : A for Rock, B for Paper, and C for Scissors
You : X for Rock, Y for Paper, and Z for Scissors

1 for Rock, 2 for Paper, and 3 for Scissors
0 if you lost, 3 if the round was a draw, and 6 if you won

AY
AX
AZ
BY
BX
BZ
CY
CX
CZ
'''