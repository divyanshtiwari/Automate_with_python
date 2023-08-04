#A funciton to validate a dictionary chess board
# Valid Board
# 1 B-king , 1 W-king
# 16 pieces at most for one player
# at most 8 pawns
# and all pieces must be on a valid space from 1a to 8h only ,that is a piece can't be on 9z space
# The piece name will begin with either a 'w' or 'b' to represent white or black, followed by 'pawn','kinght','bishop','rook','queen',' or 'King'

chessBoardSpaces = [
        '1a','2a','3a','4a','5a','6a','7a','8a','1b','2b','3b','4b','5b','6b','7b','8b','1c','2c','3c','4c','5c','6c','7c','8c','1d','2d','3d','4d','5d','6d','7d','8d','1e','2e','3e','4e','5e','6e','7e','8e','1f','2f','3f','4f','5f','6f','7f','8f','1g','2g','3g','4g','5g','6g','7g','8g','1h','2h','3h','4h','5h','6h','7h','8h'
        ]

# main Function logic
def isValidChessBoard(chessBoard):
    count = {}
    countSpaces = {} # can be used if the condition will became to also not have two pieces on the same space
    whiteCount = 0
    blackCount = 0
    for sp,piece in chessBoard.items():
        if sp not in chessBoardSpaces:
            return False
        count.setdefault(piece,0)
        count[piece]+=1
        # countSpaces.setdefault(sp,0)  # This commented piece of code can be used to determine is two piece are ocupying the same position in the ChessBoard.
        # countSpaces[sp]+=1
        # if countSpaces.get(sp,0)>1:
        #     return False
        if count.get('bpawn',0)>8:
            return False
        if count.get('wpawn',0)>8:
            return False
        if piece[0] == 'w':
            whiteCount +=1
            if whiteCount >16:
                return False
        elif piece[0] == 'b':
            blackCount +=1
            if whiteCount >16:
                return False 
        else : 
            return False
    if count.get('bking',0) != 1:
        return False
    if count.get('wking',0) != 1:
        return False

    return True

# Chess Board Dictionaries
correctcb = {'8h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5g': 'bqueen', '3e': 'wking'}
wrongNumber = {'8h': 'bking', '6c': 'wqueen', '0g': 'bbishop', '5g': 'bqueen', '3e': 'wking'}
wrongLetter = {'8h': 'bking', '6i': 'wqueen', '0g': 'bbishop', '5g': 'bqueen', '3e': 'wking'}
twoBKings = {'8h': 'bking', '2h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5g': 'bqueen', '3e': 'wking'}
twoWKings = {'8h': 'bking', '6c': 'wqueen', '2g': 'wking', '5g': 'bqueen', '3e': 'wking'}
seventeenBPieces = {'1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bbishop', '1f': 'bbishop', '1g': 'bbishop', '1h': 'bbishop', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '3a': 'bpawn', '8a': 'wking', '8b': 'wqueen', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wbishop', '8f': 'wbishop', '8g': 'wbishop', '8h': 'wbishop', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn'}
seventeenWPieces = {'8a': 'bking', '8b': 'bqueen', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bbishop', '8f': 'bbishop', '8g': 'bbishop', '8h': 'bbishop', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '8a': 'wking', '8b': 'wqueen', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wbishop', '8f': 'wbishop', '8g': 'wbishop', '8h': 'wbishop', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn', '6a': 'wpawn'}
nineBPawns = {'1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bbishop', '1g': 'bbishop', '1h': 'bbishop', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '3a': 'bpawn', '8a': 'wking', '8b': 'wqueen', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wbishop', '8f': 'wbishop', '8g': 'wbishop', '8h': 'wbishop', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn'}
nineWPawns = {'8a': 'bking', '8b': 'bqueen', '8c': 'bbishop', '8d': 'bqueen', '8e': 'bbishop', '8f': 'bbishop', '8g': 'bbishop', '8h': 'bbishop', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '8a': 'wking', '8b': 'wqueen', '8c': 'wbishop', '8d': 'wqueen', '8f': 'wbishop', '8g': 'wbishop', '8h': 'wbishop', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn', '6a': 'wpawn'}
wrongNames = {'8h': 'bkeeng', '6c': 'wqueen', '2g': 'wking', '5g': 'bqueen', '3e': 'wking'}

# function calls
print(isValidChessBoard(correctcb))
print(isValidChessBoard(wrongNumber)) 
print(isValidChessBoard(wrongLetter))
print(isValidChessBoard(twoBKings))
print(isValidChessBoard(twoWKings))
print(isValidChessBoard(seventeenBPieces))
print(isValidChessBoard(seventeenWPieces))
print(isValidChessBoard(nineBPawns))
print(isValidChessBoard(nineWPawns))
print(isValidChessBoard(wrongNames))