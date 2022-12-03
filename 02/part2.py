f=open('02/input.txt','r')
#l=[x.split(' ') for x in f.read().split("\n")]
ls=f.read().split("\n")
s=0
r={'A X':3, 'A Y':4, 'A Z':8, 'B X':1, 'B Y':5, 'B Z':9, 'C X':2, 'C Y':6, 'C Z':7}
for m in ls:
    s+=r[m]
print(s)


'''
#r={'A X':3+0, 'A Y':1+3, 'A Z':2+6, 'B X':1+0, 'B Y':2+3, 'B Z':3+6, 'C X':2+0, 'C Y':3+3, 'C Z':1+6}
'C X', 'A Y', 'B Z', 'B Y', 'A Z', 'B X', 'C Y', 'C Z', 'A X'
Opp : A for Rock, B for Paper, and C for Scissors
You : X for Rock, Y for Paper, and Z for Scissors

X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

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