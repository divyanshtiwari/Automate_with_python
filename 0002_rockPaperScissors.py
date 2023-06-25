import random
print('|||Rock, Paper, Scissors|||')
#These variables keep tracks of wins, losses and ties
wins = 0
losses = 0
ties = 0
while True:
    # print(str(wins)+' Wins, '+str(losses)+' Losses, '+str(ties)+' Ties.')
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('Enter your move: (r)ock (p)aper (s)cissor or (q)uit')
    ch = input()
    #Asumming 0 as rock, 1 as paper and 2 as scissors.
    #Taking a random int between them.
    compch = random.randint(0,2)
    if ch == 'r' and compch == 0:
        print('Rock Versus.... \nRock\nIt is a tie!')
        ties+=1
    elif ch == 'r' and compch == 1:
        print('Rock versus....\nPaper\nYou Lose!')
        losses+=1
    elif ch == 'r' and compch == 2:
        print('Rock versus....\nScissors\nYou Win!')
        wins+=1
    if ch == 'p' and compch == 0:
        print('Paper Versus.... \nRock\nYou Win!')
        wins+=1
    elif ch == 'p' and compch == 1:
        print('Paper versus....\nPaper\nIt is a tie!!')
        ties+=1
    elif ch == 'p' and compch == 2:
        print('Paper versus....\nScissors\nYou Lose!')
        losses+=1
    if ch == 's' and compch == 0:
        print('Scissors Versus.... \nRock\nYou Lose!')
        losses+=1
    elif ch == 's' and compch == 1:
        print('Scissors versus....\nPaper\nYou Win!')
        wins+=1
    elif ch == 's' and compch == 2:
        print('Scissors versus....\nScissors\nIt is a tie!')
        ties+=1
    elif ch == 'q':
        #one can use sys module to exit out of the program as well.
        #sys.exit()  # import sys before using this.
        break
    else :
        print('You entred a wrong character!!!!')
        print('Type one of r, p, s, or q.\n')
    