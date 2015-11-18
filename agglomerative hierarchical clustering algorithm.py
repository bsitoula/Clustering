import csv
import random
import numpy
from scipy.spatial import distance
import math
def euclideanDistance(single_point,overall_matrix):
    temp = []
    for everyPoint in overall_matrix:
        temp.append(distance.euclidean(single_point,everyPoint))
    return temp

def findingMinIndex(matrix):
    rowindex = []
    val = []
    for row in matrix:
        print("here")
        newrow = row.remove(0.0)
        print(row.remove(0.0))
        #rowindex.append(row.index(min(row.remove(0))))
        #val.append(min(row.remove(0)))
    minimumValue = min(val)
    colval = val.index(min(val))
    rowval = rowindex.index(minimumValue)
    print colval,rowval


if __name__ == '__main__':
    #### GIVE THE LOCATION OF WHERE THE FILE IS LOCATED
    filePath = "/Users/bibassitoula/Desktop/Data Mining /Assignment/assignment 4/wineDataset.csv"
    print("###################### Importing Wine Dataset ###############################")
    points = []
    with open(filePath, "r") as inputCsvFile:
        csvData = csv.reader(inputCsvFile, delimiter=',')
        k = 0
        for line in csvData:
            k = k + 1
            points.append(map(float,line[1:len(line)]))
    print("################ "+str(k)+" Instances Loaded Completely #####################")
    mapping = {}
    print(points[0])
    print(points[1])
    for i in range(0,178):
        mapping[i] = i
    priorityMatrix = []
    for everyPoint in points:
        priorityMatrix.append(euclideanDistance(everyPoint,points))
    for everline in priorityMatrix:
        print(everline)
    findingMinIndex(priorityMatrix)