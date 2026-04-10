import random
import math

class RandomManager():

    @classmethod
    def rng(self, maxValueExclude) -> int:  # from zero to num send (-1).
        return math.floor(random.random() * maxValueExclude)
    @classmethod
    def rngDice(self, faces=6) -> int:  # from one to num send.
        return RandomManager.rng(faces) + 1
    @classmethod
    def rngBetween(self, minNum, maxNum) -> int:  # get a random number between two num (both include).
        rangeRand = maxNum - minNum
        rangeRand += 1
        return RandomManager.rng(rangeRand) + minNum