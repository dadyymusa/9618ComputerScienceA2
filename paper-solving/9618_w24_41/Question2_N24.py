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
    
    # 2d
# takes the height and risk of a fence as parameters
# • calculates the percentage chance of success for that horse jumping the fence without
# knocking it down
# • returns the calculated percentage chance of success as a real number.
    def Success(self, Height, Risk):
        Modifier = {
            1 : 1.0, 
            2 : 0.9,
            3 : 0.8,
            4 : 0.7,
            5 : 0.6
        }
        if Height <= self.MaxFenceHeight:
            return self.PercentageSuccess * Modifier[Risk]
        else:
            return self.PercentageSuccess * 0.2
    
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
        NewHeight = int(input(f"{i + 1}. Height Value: "))
        if NewHeight >= 70 and NewHeight <= 180:
            break
        print("Height should be between 70 to 180 inclusive")

    while True:
        NewRisk = int(input(f"{i + 1}. Risk Value: "))
        if NewRisk >= 1 and NewRisk <= 5:
            break
        print("Risk should be between 1 to 5 inclusive")
    NewFence = Fence(NewHeight, NewRisk)
    Course.append(NewFence)
#  2ei
#  calculate and output the chance of the first horse jumping each of the four fences without
# knocking each fence down
# • calculate and output the chance of the second horse jumping each of the four fences
# without knocking each fence down.
# example : 'The horse Fox at fence 1 has a 68% chance of success'
# 2eii
# calculate and output the average chance of success for each horse jumping over all
# four fences without knocking each fence down (the average is the total of values
# divided by the quantity of values). An example output for one horse jumping all of
# the fences is:
#  "The horse Fox has an average 70% chance of jumping over all four
# fences"
HighValue = [0, 0] #Stores the index of horse which has highest average chance of success
for horse in range(len(Horses)):
    average = 0
    for i in range(len(Course)):
        chance = Horses[horse].Success(Course[i].GetHeight(), Course[i].GetRisk())
        print(f'The horse {Horses[horse].GetName()} at fence {i + 1} has a {chance}% chance of success')
        average += chance
    average = average / 4
    if average > HighValue[1]:
        HighValue[0], HighValue[1] = horse, average
    print(f'The horse {Horses[horse].GetName()} has an average {average}% chance of jumping over all four fences')
    print()
print(f'{Horses[HighValue[0]].GetName()} has the best chance of winning')
# 152 5
# 121 1
# 130 3
# 145 4