import random

def drawBoard(grid):
    for row in grid:
        print(" ".join(row))


def findPoint(move):
    points = [
            ["0", "0"], ["0", "1"], ["0", "2"],
            ["1", "0"], ["1", "1"], ["1", "2"],
            ["2", "0"], ["2", "1"], ["2", "2"],
              ]

    location = points[move - 1]
    return location


def botRandom(x):
    validBot = True
    while validBot:
        bot = random.randint(1, 9)
        if bot not in x:
            bot = random.randint(1, 9)
        else:
            validBot = False
    return bot


def vertloop(grid):

    correct = 0

    for i in range(0, 3):

        if grid[0][i] == grid[1][i] == grid[2][i] == "x":
            correct += 1

        elif grid[0][i] == grid[1][i] == grid[2][i] == "o":
            correct += 1

    if correct != 0:
        return True

    else:
        return False


def checkwinner(grid):
    checker = 0
    if grid[0][0] == grid[1][1] == grid[2][2] == "x"\
            or grid[0][0] == grid[1][1] == grid[2][2] == "o":
        checker += 1

    elif grid[0][2] == grid[1][1] == grid[2][0] == "x"\
            or grid[0][2] == grid[1][1] == grid[2][0] == "o":
        checker += 1

    elif vertloop(grid):
        checker += 1

    else:
        for i in grid:

            if i.count("x") == 3 or i.count("o") == 3:
                checker += 1

    if checker != 0:
        return False
    else:
        return True


def setTurn():
    userChoice = int(input("Would you like to go 1st or 2nd (1 or 2): "))
    if userChoice == 1:
        return True
    else:
        return False

slots = [
        ["-", "-", "-"],  # 00 01 02
        ["-", "-", "-"],  # 10 11 12
        ["-", "-", "-"]   # 20 21 22
         ]


game = True
turn = setTurn()
possibleTurns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while game:
    drawBoard(slots)
    valid = False
    if turn and game:
        print(possibleTurns)
        userMov = int(input("Please take your move: "))
        while not valid:
            if int(userMov) not in possibleTurns:
                userMov = int(input("Please take a valid move: "))
            else:
                possibleTurns.remove(int(userMov))
                valid = True
        pointer = findPoint(userMov)
        a, b = pointer[0], pointer[1]
        slots[int(a)][int(b)] = "x"
        game = checkwinner(slots)

    else:
        print("Bot's Turn")
        botMov = botRandom(possibleTurns)
        possibleTurns.remove(int(botMov))
        pointer = findPoint(botMov)
        a, b = pointer[0], pointer[1]
        slots[int(a)][int(b)] = "o"
        game = checkwinner(slots)
    turn = not turn

print("Final State")
drawBoard(slots)
# sort out way to stop if nobody has won
if turn != True:
    print("User won")
else:
    print("Bot won")
