# =============================================================================
# Chloe Smith
# 2/9/2024
# to create a foot measure class
# =============================================================================

class FootMeasure:
    INCHES_PER_FOOT = 12

    def __init__(self,feet=0,inches=0):
        self.__feet = feet
        self.__inches = inches

    def __str__(self):
        if self.__inches == 0 and self.__feet != 0:
            result = str(self.__feet) + " ft."
        elif self.__inches != 0 and self.__feet == 0 and self.__inches < 12:
            result = str(self.__inches) + " in."
        elif self.__feet == 0 and self.__inches != 0 and self.__inches >= 12:
            result = str(self.convertToFeet())
        else:
            result = str(self.__feet) + ' ft. ' + str(self.__inches) + (' in.')
        return result

    def getFeet(self):
        return self.__feet

    def setFeet(self,other):
        self.__feet = other

    def getInches(self):
        return self.__inches

    def setInches(self,other):
        self.__inches = other

    def inInches(self):
        result = self.__feet * self.INCHES_PER_FOOT + self.__inches
        return result

    def convertToFeet(self):
        resultFeet = (self.__inches // self.INCHES_PER_FOOT) + self.__feet
        resultRemainder = self.__inches % self.INCHES_PER_FOOT
        result = FootMeasure(resultFeet, resultRemainder)
        return result

    def __add__(self, other):
        result = self.inInches() + other.inInches()
        result = FootMeasure(result // self.INCHES_PER_FOOT,result % self.INCHES_PER_FOOT)
        return result

    def __eq__(self,other):
        return self.inInches() == other.inInches()

    def __ne__(self,other):
        return self.inInches() != other.inInches()

    def __lt__(self, other):
        return self.inInches() < other.inInches()

    def __gt__(self, other):
        return self.inInches() > other.inInches()

    def __le__(self, other):
        self.inInches() <= other.inInches()

    def __ge__(self, other):
        self.inInches() >= other.inInches()

