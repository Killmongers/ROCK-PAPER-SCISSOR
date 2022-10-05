


import sys,random
print('rock,paper,scissor')
wins=0
losses=0
ties=0
while True:
    print('%s wins,%s,losses,% sties'%(wins,losses,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissor or(q)uit')
        pmove=input()
        if pmove=='q':
            sys.exit()
        if pmove=='r' or pmove=='p' or pmove=='s':
            break
        print('type one of r,p,s or q.')
    if pmove=='r':
        print('rock vs.....') 
    elif pmove=='p':
        print('paper vs.....')
    elif pmove=='s':
        print('scissor vs.....')

    computerMove=''    
    random_number=random.randint(1,3)
    if random_number==1:
        computerMove=='r'
        print('rock') 
    elif random_number==2:
        computerMove=='p'
        print('paper' )
    elif random_number==3:
        computerMove=='s'         
        print('scissor')

    if pmove==computerMove:
        print('Its a tie')
        ties=ties+1
    elif pmove=='r' and computerMove=='s':
        print('you win')
        wins=wins+1
    elif pmove=='s' and computerMove=='p':
        print('you win')
        wins=wins+1
    elif pmove=='p' and computerMove=='r':
        print('you win')
        wins=wins+1
    elif pmove=='s' and computerMove=='r':
        print('you loss')
        losses=losses+1
    elif pmove=='r' and computerMove=='p':
        print('you loss')
        losses=losses+1
    elif pmove=='p' and computerMove=='s':
        print('you loss')
        losses=losses+1
                     

