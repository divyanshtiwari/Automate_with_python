import time,sys

def createInfinitePattern():
    try :
        indent = 0
        while True:
            print(' '*indent,'*'*8,sep='')
            time.sleep(0.1)
            if indent == 20:
                inc = False
            if indent == 0 :
                inc = True
            if inc:
                indent +=1
            else:
                indent -=1
    except Exception as e :
        print( type(e))
        print("inside funciton")
        

try:
    createInfinitePattern()
except KeyboardInterrupt :
    print("Key board stop")
    # print( type(e))