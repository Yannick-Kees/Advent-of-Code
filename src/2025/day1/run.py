from src.base_class import riddle
import math

TOTAL_SIZE = 100
START_POINT = 50

class code():
    def __init__(self, instructions: str):
        self.direction = instructions[0]
        self.length = int(instructions[1:])

    def __radd__(self, other):
        return (other + self.length) % TOTAL_SIZE if self.direction=="R" else (other - self.length) % TOTAL_SIZE

    def turning(self, pos):
        new_point = pos + self.length if self.direction=="R" else pos - self.length
        turns = abs(math.floor(pos / TOTAL_SIZE) - math.floor(new_point / TOTAL_SIZE) )
        turns += (new_point % TOTAL_SIZE == 0) and self.direction == "L" 
        turns -= (pos == 0 and self.direction == "L")

        return new_point % TOTAL_SIZE, turns

    
class day1(riddle):
    def __init__(self, day, mode):
        super(day1, self).__init__(day, mode)

    def a(self):
        x = START_POINT
        print( sum(1 for l in self.lines if (x := x + code(l)) == 0))

        print(zeros)

    def b(self):
        x = START_POINT
        zeros = 0
        for l in self.lines:
            x, new_zeros = code(l).turning(x)
            zeros += new_zeros

        print(zeros)

if __name__ == "__main__":
    x = day1(day = 1, mode = "full")
    x.a()
    x.b()

