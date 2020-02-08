###Log
#1.00 Jimmy Seeber + DTO team 12.10.19 
#1.01 Darick Brokaw 12.11.19, changed varibles to inputs, renamed, added math, commented the existing code and stopped when reordering clockwise vs counter clockwise the Exterior Walls
#1.02 Darick Brokaw 12.12.19, changed walls to clockwise, uptadeted variable names
#1.03 Darick Brokaw 01.16.20, added stair Generator, review comments in stair Generator
#1.04 Darick Brokaw 02.04.20, added export to json file

###Rules###
#Addtional documentation will be located at https://sites.google.com/view/bagrepo/
#When editing it is required that you log it inside this file
#When writing code it must be commented well. Variables using abrevations must be spelled out in a comment.
#formatting style to follow PEP 8 Style Guide for Python Code  https://www.python.org/dev/peps/pep-0008/
#Coordinates for this application are defind defined to be Clockwise. Research yeilded no clear standard regarding order orientation.

###Abbreviations###
#Points = Pt

#==========================================================================

###Building Shell Inputs
A = int(input('Enter Total Square Footage of Building: ')) #A = Total Square Footage of Building, all floors. Ask for value, convert from string to integer,assign to a.
NOF = int(input('Enter Number of Floors: ')) #NOF = Number of Floors.
SFSQ = (A / NOF) #SFSQ = SingleFloorSQ
GoldenRatio = 1.61803398875 #building ratio of rectangle is hard coded to be a ratio of (GoldenRatio = 1.61803398875) but will need to be either an input (not recomended) or a range with the Golden Ratio at its center +/-
SLS = (SFSQ / GoldenRatio) #SLS = Shell Long Side Dimension
SSS = (SFSQ - SLS) #SSS = Shell Short Side Dimension
buildingParts = {} #Create empty dictionary that my be added to later.
###Exterior Walls
origin = (0, 0)
Pt1 = (0, SSS)
Pt2 = (SLS, SSS)
Pt3 = (SLS, 0)
shellCorners = [origin, Pt1, Pt2, Pt3]
buildingParts['Exterior_Walls'] = shellCorners #add to dictionary data structure named "buildingParts".
westMidPtHeight = SSS/2 #Left most point of the hallway center on left side wall
###Hallway/ Corridor
hallWidth = 6 #hallway width
hallwidthHalf = (hallWidth / 2) # half the width of the hallway to calculate corners
hwPt0 = (origin[0] , westMidPtHeight - hallwidthHalf) #hallway bottom left (Clockwise)
hwPt1 = (origin[0] , westMidPtHeight + hallwidthHalf) #hallway top left (Clockwise)
hwPt2 = (Pt1[0] , westMidPtHeight - hallwidthHalf) #hallway bottom right (Clockwise)
hwPt3 = (Pt1[0] , westMidPtHeight + hallwidthHalf) #hallway top right (Clockwise)
hallway = [hwPt0, hwPt1, hwPt2, hwPt3]
buildingParts['Hallway'] = hallway #add to dictionary data structure named "buildingParts".
###Elevator
elevatorSize = (10,10) #Elevator size and number of elevators need to be added in the future.
elevatorStartPt = (SLS / 2 , hwPt1[1]) #North placed elevator
elevatorPt0 = (elevatorStartPt[0] - (elevatorSize[0]/2), elevatorStartPt[1])
elevatorPt1 = (elevatorStartPt[0] - (elevatorSize[0]/2), elevatorStartPt[1] + elevatorSize[1])
elevatorPt2 = (elevatorStartPt[0] + (elevatorSize[0]/2), elevatorStartPt[1] + elevatorSize[1])
elevatorPt3 = (elevatorStartPt[0] + (elevatorSize[0]/2), elevatorStartPt[1])
elevator = [elevatorPt0,  elevatorPt1, elevatorPt2, elevatorPt3]
buildingParts['Elevator'] = elevator #add to dictionary data structure named "buildingParts".
###RestroomMen 
###RestroomWomen
###Stair
####ElectricalRoom
print("exterior wall points:", buildingParts['Exterior_Walls']) #Display data
print("hallway wall points:", buildingParts['Hallway']) #Display data
print("Elevator wall points:", buildingParts['Elevator']) #Display data

#==========================================================================


### Stair Generator
# All units are in inches
# Need to add ability to do switchback stairs as well as calculate 3D Cube size of stair core

import math
# Inputs
FloorToFloorHeight = int(input('Enter floor to floor height (Default 120"): ') or 120)
StairTreadDepth = int(input('Enter tread depth (Default 11"): ') or 11)
StairRise = int(input('Enter riser max. (Default 7"): ') or 7)
StairWidth = int(input('Enter egress width (Default 48"): ') or 48) #Need to calculate based on occupancy egress, need to get get from building code
Landing = StairWidth # building code says landing equal to width of stairs
#Calculations
StairRiserCount = (math.ceil(FloorToFloorHeight / StairRise))
StairRiserHeight = FloorToFloorHeight / StairRiserCount
StairTreadRunWOLanding = (StairRiserCount - 1) * StairTreadDepth #No Tread nosing
StairTreadRunWLanding = StairTreadRunWOLanding + (Landing * 2)
#Points

#Output
print(f"Number of risers: {StairRiserCount}, Riser Heigth: {StairRiserHeight}, Total run Length: {StairTreadRunWLanding} inches w landings")

#==========================================================================

### JSON Exporter

import json

with open("projectdotsdatafile.json", "w") as write_file:
    json.dump(buildingParts, write_file)

#==========================================================================
