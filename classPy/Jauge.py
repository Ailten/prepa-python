import math

class Jauge():

    def __init__(self, maxValue):
        self.maxValue = maxValue
        self.currentValue = maxValue
    @classmethod
    def initWithValue(self, currentValue, maxValue) -> 'Jauge':
        instance = Jauge(maxValue)
        instance.currentValue = currentValue
        return instance

    def increase(self, value):
        self.currentValue += value
    def decreate(self, value):
        self.currentValue -= value

    def refill(self):
        self.currentValue = self.maxValue
    def clamp(self):
        self.currentValue = math.min(math.max(self.currentValue, 0), self.maxValue)

    def getPurcent(self) -> float:
        return self.currentValue / self.maxValue

    def getOverRange(self) -> int:
        return math.min(self.currentValue - self.maxValue, 0)
    def getUnderRange(self) -> int:
        return math.max(self.currentValue * -1, 0)

    def isEmpty(self) -> bool:
        return (self.currentValue <= 0)
    def isFull(self) -> bool:
        return self.currentValue >= self.maxValue

    def __int__(self):
        return self.currentValue