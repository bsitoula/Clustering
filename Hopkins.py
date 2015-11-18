import csv
import random
import numpy
from scipy.spatial import distance
import math
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
    numberOfSample = (5*k/100)
    H = []
    for i in range(0,10):
        xi = []
        yi = []

        p_i = random.sample(points,numberOfSample)
        v_p_i = [item for item in points if item not in p_i]
        for everyPi in p_i:
            temp1 = []
            for everyVpi in v_p_i:
                temp1.append(distance.euclidean(everyPi,everyVpi))
            xi.append(min(temp1))

        q_i = random.sample(points,numberOfSample)
        v_q_i = [item for item in points if item not in q_i]

        for everyQi in q_i:
            temp2 = []
            for everyVqi in v_q_i:
                temp2.append(distance.euclidean(everyQi,everyVqi))
            yi.append(min(temp2))
        print("Hopkins Statistics for Iteration "),
        print(i+1),
        print("is :"),
        print(sum(yi)/(sum(xi)+sum(yi)))
        H.append(sum(yi)/(sum(xi)+sum(yi)))
    print("The Average Value of the Hopkins Statistics is : "),
    print(sum(H)/10)