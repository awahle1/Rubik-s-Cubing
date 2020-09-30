import random

class Cube:
    def __init__(self):
        self.sides={
            "white": [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
            "red" : [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
            "yellow" : [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
            "orange" : [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
            "green" : [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
            "blue" : [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],

        }
    def __str__(self):
        cube = ""
        for side in self.sides.values():
            for row in side:
                for val in row:
                    cube += val
                cube += '\n'
            cube += "-------------" + '\n'

        return(cube)

    def rotateface(self, color):
        face = self.sides[color]
        rface = [['', '', ''], ['', '', ''], ['', '', '']]

        rface[0][0] = face[2][0]
        rface[0][1] = face[1][0]
        rface[0][2] = face[0][0]

        rface[1][0] = face[2][1]
        rface[1][1] = face[1][1]
        rface[1][2] = face[0][1]

        rface[2][0] = face[2][2]
        rface[2][1] = face[1][2]
        rface[2][2] = face[0][2]

        return(rface)

    def r(self):
        sides = self.sides
        tempwhite = [[], [], []]
        for i in range(3):
            for j in range(3):
                tempwhite[i].append(sides['white'][i][j])
        tempred = sides['red'].copy()
        temporange = sides['orange'].copy()
        tempyellow = sides['yellow'].copy()
        for i in range(3):
            sides['white'][i][2] = tempred[i][2]
        for i in range(3):
            sides['red'][i][2] = tempyellow[i][2]
        for i in range(3):
            sides['yellow'][i][2] = temporange[i][0]
        for i in range(3):
            sides['orange'][i][0] = tempwhite[i][2]

        self.rotateface("blue")

        self.sides = sides

        print('R')

        return()

    def rprime(self):
        sides = self.sides
        tempyellow = [[], [], []]
        for i in range(3):
            for j in range(3):
                tempyellow[i].append(sides['yellow'][i][j])
        tempred = sides['red'].copy()
        temporange = sides['orange'].copy()
        tempwhite = sides['white'].copy()
        for i in range(3):
            sides['yellow'][i][2] = tempred[i][2]
        for i in range(3):
            sides['red'][i][2] = tempwhite[i][2]
        for i in range(3):
            sides['white'][i][2] = temporange[i][0]
        for i in range(3):
            sides['orange'][i][0] = tempyellow[i][2]
        self.sides = sides

        print('Rprime')

        return()

    def l(self):
        sides = self.sides
        tempyellow = [[], [], []]
        for i in range(3):
            for j in range(3):
                tempyellow[i].append(sides['yellow'][i][j])
        tempred = sides['red'].copy()
        temporange = sides['orange'].copy()
        tempwhite = sides['white'].copy()
        for i in range(3):
            sides['yellow'][i][0] = tempred[i][0]
        for i in range(3):
            sides['red'][i][0] = tempwhite[i][0]
        for i in range(3):
            sides['white'][i][0] = temporange[i][2]
        for i in range(3):
            sides['orange'][i][2] = tempyellow[i][0]
        self.sides = sides

        print('L')

        return()

    def lprime(self):
        sides = self.sides
        tempwhite = [[], [], []]
        for i in range(3):
            for j in range(3):
                tempwhite[i].append(sides['white'][i][j])
        tempred = sides['red'].copy()
        temporange = sides['orange'].copy()
        tempyellow = sides['yellow'].copy()
        for i in range(3):
            sides['white'][i][0] = tempred[i][0]
        for i in range(3):
            sides['red'][i][0] = tempyellow[i][0]
        for i in range(3):
            sides['yellow'][i][0] = temporange[i][2]
        for i in range(3):
            sides['orange'][i][2] = tempwhite[i][0]
        self.sides = sides

        self.rotateface("green")

        print('Lprime')

        return()

    def u(self):
        sides = self.sides
        tempred = sides['red'].copy()
        tempgreen = sides['green'].copy()
        temporange = sides['orange'].copy()
        tempblue = sides['blue'].copy()

        sides['red'][0] = tempblue[0]
        sides['blue'][0] = temporange[0]
        sides['orange'][0] = tempgreen[0]
        sides['green'][0] = tempred[0]

        print('U')

        return()

    def uprime(self):
        sides = self.sides
        tempred = sides['red'].copy()
        tempgreen = sides['green'].copy()
        temporange = sides['orange'].copy()
        tempblue = sides['blue'].copy()

        sides['red'][0] = tempgreen[0]
        sides['green'][0] = temporange[0]
        sides['orange'][0] = tempblue[0]
        sides['blue'][0] = tempred[0]

        print('Uprime')

        return()

    def d(self):
        sides = self.sides
        tempred = sides['red'].copy()
        tempgreen = sides['green'].copy()
        temporange = sides['orange'].copy()
        tempblue = sides['blue'].copy()

        sides['red'][2] = tempgreen[2]
        sides['green'][2] = temporange[2]
        sides['orange'][2] = tempblue[2]
        sides['blue'][2] = tempred[2]

        self.rotateface("yellow")

        print("D")

        return()

    def dprime(self):
        sides = self.sides
        tempred = sides['red'].copy()
        tempgreen = sides['green'].copy()
        temporange = sides['orange'].copy()
        tempblue = sides['blue'].copy()

        sides['red'][2] = tempblue[2]
        sides['blue'][2] = temporange[2]
        sides['orange'][2] = tempgreen[2]
        sides['green'][2] = tempred[2]

        print("Dprime")

        return()

    def f(self):
        sides = self.sides
        tempwhite = [[], [], []]
        for i in range(3):
            for j in range(3):
                tempwhite[i].append(sides['white'][i][j])
        tempgreen = sides['green'].copy()
        tempyellow = sides['yellow'].copy()
        tempblue = sides['blue'].copy()

        sides['white'][2][0] = tempgreen[2][2]
        sides['white'][2][1] = tempgreen[1][2]
        sides['white'][2][2] = tempgreen[0][2]

        sides['green'][0][2] = tempyellow[0][0]
        sides['green'][1][2] = tempyellow[0][1]
        sides['green'][2][2] = tempyellow[0][2]

        sides['yellow'][0][0] = tempblue[0][0]
        sides['yellow'][0][1] = tempblue[1][0]
        sides['yellow'][0][2] = tempblue[2][0]

        sides['blue'][0][0] = tempwhite[2][0]
        sides['blue'][1][0] = tempwhite[2][1]
        sides['blue'][2][0] = tempwhite[2][2]

        print("F")

        return()

    def fprime(self):
        sides = self.sides
        tempwhite = [[], [], []]
        for i in range(3):
            for j in range(3):
                tempwhite[i].append(sides['white'][i][j])
        tempgreen = sides['green'].copy()
        tempyellow = sides['yellow'].copy()
        tempblue = sides['blue'].copy()

        sides['white'][2][0] = tempblue[0][0]
        sides['white'][2][1] = tempblue[1][0]
        sides['white'][2][2] = tempblue[2][0]

        sides['blue'][0][0] = tempyellow[0][0]
        sides['blue'][1][0] = tempyellow[0][1]
        sides['blue'][2][0] = tempyellow[0][2]

        sides['yellow'][0][0] = tempgreen[2][2]
        sides['yellow'][0][1] = tempgreen[1][2]
        sides['yellow'][0][2] = tempgreen[0][2]

        sides['green'][0][2] = tempwhite[2][0]
        sides['green'][1][2] = tempwhite[2][1]
        sides['green'][2][2] = tempwhite[2][2]

        print("Fprime")

        return()

    def b(self):
        sides = self.sides
        tempwhite = [[], [], []]
        for i in range(3):
            for j in range(3):
                tempwhite[i].append(sides['white'][i][j])
        tempgreen = sides['green'].copy()
        tempyellow = sides['yellow'].copy()
        tempblue = sides['blue'].copy()

        sides['white'][0][0] = tempblue[0][2]
        sides['white'][0][1] = tempblue[1][2]
        sides['white'][0][2] = tempblue[2][2]

        sides['blue'][0][2] = tempyellow[2][0]
        sides['blue'][1][2] = tempyellow[2][1]
        sides['blue'][2][2] = tempyellow[2][2]

        sides['yellow'][2][0] = tempgreen[0][0]
        sides['yellow'][2][1] = tempgreen[1][0]
        sides['yellow'][2][2] = tempgreen[2][0]

        sides['green'][0][0] = tempwhite[0][0]
        sides['green'][1][0] = tempwhite[0][1]
        sides['green'][2][0] = tempwhite[0][2]

        print("B")

        return()

    def bprime(self):
        sides = self.sides
        tempwhite = [[], [], []]
        for i in range(3):
            for j in range(3):
                tempwhite[i].append(sides['white'][i][j])
        tempgreen = sides['green'].copy()
        tempyellow = sides['yellow'].copy()
        tempblue = sides['blue'].copy()

        sides['white'][0][0] = tempgreen[0][0]
        sides['white'][0][1] = tempgreen[1][0]
        sides['white'][0][2] = tempgreen[2][0]

        sides['green'][0][0] = tempyellow[2][0]
        sides['green'][1][0] = tempyellow[2][1]
        sides['green'][2][0] = tempyellow[2][2]

        sides['yellow'][2][0] = tempblue[0][2]
        sides['yellow'][2][1] = tempblue[1][2]
        sides['yellow'][2][2] = tempblue[2][2]

        sides['blue'][0][2] = tempwhite[0][0]
        sides['blue'][1][2] = tempwhite[0][1]
        sides['blue'][2][2] = tempwhite[0][2]

        print("Bprime")

        return()

    def scramble(self):
        for i in range(0, 100):
            x = random.randint(0,11)
            print(x)
            if(x == 0):
                self.r()
            elif(x == 1):
                self.rprime()
            elif(x == 2):
                self.l()
            elif(x == 3):
                self.lprime()
            elif(x == 4):
                self.u()
            elif(x == 5):
                self.uprime()
            elif(x == 6):
                self.d()
            elif(x == 7):
                self.dprime()
            elif(x == 8):
                self.f()
            elif(x == 9):
                self.fprime()
            elif(x == 10):
                self.b()
            else:
                self.bprime()

        return()

    def iswcsolved(cube):
        sides = cube.sides
        if (sides['white'][0][1]=='w' and sides['white'][1][0]=='w' and sides['white'][1][2]=='w' and sides['white'][2][1]=='w') and (sides['red'][0][1]=='r' and sides['blue'][0][1]=='b' and sides['orange'][0][1]=='o' and sides['green'][0][1] == 'g'):
            return(True)
        else:
            return(False)
        return()

    def solve(self):
        #white cross
        topspots = [(0,1), (1,0), (1,2), (2,1)]
        sides = self.sides
        #wc = False
        #wc = iswcsolved(self)
        #while (not wc):
        # misplaced whites on white side
        for spot in topspots:
            if (sides['white'][spot[0]][spot[1]]=='w'):
                print("spot")

                if spot[0] == 0:
                    edge = sides['orange'][0][1]
                    if(edge == 'g'):
                        self.uprime()
                    elif(edge == 'r'):
                        self.u()
                        self.u()
                    elif(edge == 'b'):
                        self.u()
                    else:
                        co = True

                elif spot[1] == 0:
                    edge = sides['green'][0][1]
                    if(edge == 'g'):
                        cg = True
                    elif(edge == 'r'):
                        self.uprime()
                    elif(edge == 'b'):
                        self.u()
                        self.u()
                    else:
                        self.u()

                elif spot[0] == 1:
                    edge = sides['blue'][0][1]
                    if(edge == 'g'):
                        self.u()
                        self.u()
                    elif(edge == 'r'):
                        self.u()
                    elif(edge == 'b'):
                        cb = True
                    else:
                        self.uprime()

                else:
                    edge = sides['red'][0][1]
                    if(edge == 'g'):
                        self.u()
                    elif(edge == 'r'):
                        cr = True
                    elif(edge == 'b'):
                        self.uprime()
                    else:
                        self.u()
                        self.u()




def main():
    cube1 = Cube()
    #cube1.scramble()
    cube1.r()
    cube1.r()
    cube1.lprime()
    cube1.lprime()

    cube1.d()
    print(cube1)
    cube1.d()
    cube1.r()
    cube1.r()
    cube1.lprime()
    cube1.lprime()
    print(cube1)
    #print(cube1)
    #cube1.solve()
    #print(cube1)
    return()

if __name__ == "__main__":
    main()
