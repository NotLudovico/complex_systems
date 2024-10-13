from random import randint


class SandPile:
    def __init__(self, dimension: int):
        self.grid = [0] * pow(dimension, 2)
        self.dimension = dimension

    def add_grain(self):
        index = randint(0, pow(self.dimension, 2) - 1)
        self.grid[index] += 1
        self.topple(index)

    def topple(self, index: int) -> int:
        number_of_toppling = 0
        if 0 <= index and index < len(self.grid) and self.grid[index] >= 4:
            self.grid[index] = 0
            if index + 1 < len(self.grid) and (index + 1) % self.dimension != 0:
                self.grid[index + 1] += 1
            if index - 1 >= 0 and index % self.dimension != 0:
                self.grid[index - 1] += 1
            if index + self.dimension < len(self.grid):
                self.grid[index + self.dimension] += 1
            if index - self.dimension >= 0:
                self.grid[index - self.dimension] += 1

            number_of_toppling += 1

            self.print()

            number_of_toppling += self.topple(index + 1)
            number_of_toppling += self.topple(index - 1)
            number_of_toppling += self.topple(index + self.dimension)
            number_of_toppling += self.topple(index - self.dimension)

        return number_of_toppling

    def __str__(self):
        line = ""
        for i in range(0, len(self.grid)):
            line += " | " + str(self.grid[i])
            if i != 0 and (i + 1) % self.dimension == 0:
                line += " |\n"
        return line
