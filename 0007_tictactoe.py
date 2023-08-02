theBoard = {'top-left':' ','top-middel':' ','top-right':' ','mid-left':' ','mid-middel':' ','mid-right':' ','lower-left':' ','lower-middel':' ','lower-right':' '}

def printTheBoard():
    print(theBoard['top-left']+'|'+theBoard['top-middel']+'|'+theBoard['top-right'])
    print('-+-+-')
    print(theBoard['mid-left']+'|'+theBoard['mid-middel']+'|'+theBoard['mid-right'])
    print('-+-+-')
    print(theBoard['lower-left']+'|'+theBoard['lower-middel']+'|'+theBoard['lower-right'])


turn = 'X'
for i in range(9):
    printTheBoard()
    print("Turn for "+turn+" Move which space")
    moveSpace = input()
    theBoard[moveSpace]=turn
    if turn == 'X':
        turn = 'O'
    else :
        turn = 'X'

printTheBoard()