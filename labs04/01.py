from random import randint

def createBingo():
    def generate(start, end):
        return [
            randint(start, end)
            for i in range(15)
        ]
    return\
        { 'B' : generate( 1, 15)
        , 'I' : generate(16, 30)
        , 'N' : generate(31, 45)
        , 'G' : generate(46, 60)
        , 'O' : generate(61, 75)
        }

def printBingo(bingo):
    print(' ', end='')
    for k in bingo.keys():
        print(k, end='  ')
    print()
    for i in range(5):
        for k in bingo.keys():
            if bingo[k][i] < 10:
                print(' ', end='')
            print(bingo[k][i], end=' ')
        print()

bingo = createBingo()
printBingo(bingo)
