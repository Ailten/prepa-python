import math

class Jauge():

    def __init__(self, maxValue):
        self.maxValue = maxValue
        self.currentValue = maxValue

    def increase(self, value):
        self.currentValue += value
    def decreate(self, value):
        self.currentValue -= value

    def refill(self):
        self.currentValue = self.maxValue

    def getPurcent(self):
        return self.currentValue / self.maxValue

    def getOverRange(self):
        return math.min(self.currentValue - self.maxValue, 0)
    def getUnderRange(self):
        return math.max(self.currentValue * -1, 0)

    def isEmpty(self) -> bool:
        return (self.currentValue <= 0)
    def isFull(self) -> bool:
        return self.currentValue >= self.maxValue