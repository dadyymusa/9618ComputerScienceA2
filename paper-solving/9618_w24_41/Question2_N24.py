# 2ai
class Horse:
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        self.Name = Name    #String
        self.MaxFenceHeight = MaxFenceHeight    #Integer
        self.PercentageSuccess = PercentageSuccess  #Integer

# 2aii  
    def GetName(self):
        return self.Name
    
    def GetMaxFenceHeight(self):
        return self.MaxFenceHeight
    
# 2b
# • declare the array, Horses, local to the main program with space for two Horse
# objects
# • store the two horses described in the array
# • output the name of both Horse objects from the array
    
Horses = []

Beauty = Horse('Beauty', 150, 72)
Jet = Horse('Jet', 160, 65)

Horses.append(Beauty)
Horses.append(Jet)

print(Horses[0].GetName())
print(Horses[1].GetName())


# 2ci The class Fence stores data about the fences. Each fence has a height in cm and a risk
# number. 

class Fence:
    def __init__(self, Height, Risk):
        self.Height = Height #Integer
        self.Risk = Risk #Integer

    def GetHeight(self):
        return self.Height
    
    def GetRisk(self):
        return self.Risk
    
# 2cii

Course = []

for i in range(4):
    while True:
        NewHeight = int(input(f"{i}. Height Value: "))
        if NewHeight >= 70 and NewHeight <= 180:
            break
        print("Height should be between 70 to 180 inclusive")

    while True:
        NewRisk = int(input(f"{i}. Risk Value: "))
        if NewRisk >= 1 and NewRisk <= 5:
            break
        print("Risk should be between 1 to 5 inclusive")