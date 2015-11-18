__author__ = 'bibassitoula'
import csv
import random
import numpy
from scipy.spatial import distance
import math
import matplotlib.pyplot as plt

#### Calculate the Euclidean distance between the points
def euclideanDistance(given_row,given_centorid):
    eucDistance=[]
    for everyCentroid in given_centorid:
            eucDistance.append(distance.euclidean(given_row,everyCentroid))
    return eucDistance.index(min(eucDistance))


#### Calculate the New Centroid from the Collected clusters
def CalculateNewCentroid(new_clusters):
    new_cluster_Rows = new_clusters
    new_centroid_row = []
    for key,val in new_cluster_Rows.items():
        index = 0
        center = []
        while index < 13:
            averageValue = 0
            for i in range(0,len(val)):
                averageValue = averageValue + val[i][index]
            center.append(averageValue/len(val))
            index = index + 1
        new_centroid_row.append(center)
    return new_centroid_row

#### Checking if the new centroid is equal to the old centroid
def isTheCentroidEqual(new_centroid,old_centroid):
    for i in range(0,len(new_centroid)):
        if old_centroid[i] != new_centroid[i]:
            return 1
    return 0
#### Calculate the SSE for each cluster
def calculateSSE(cluster_values,centers):
    newSet = []
    print("  With "+str(len(cluster_values))+" Number of Instances is "),
    for everySet in cluster_values:
        newSet.append(sum([math.pow((m_i - x_i),2) for m_i, x_i in zip(centers, everySet)]))
    return sum(newSet)

def findingInsatanceId(initialPoints,cluster):
    temp = {}
    for i in range(1,len(cluster)+1):
        temp[i] = []
    for key,val in cluster.items():
        for everyInstance in val:
            temp[key].append((initialPoints.index(everyInstance))+1)
    return temp



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
    SSE_Collection = []
    for i in range(2,7):
        print("#################################")
        print("Running K-means with k = "+str(i))
        numberOfCluster = i
        cluster = {}
        for cluster_id in range(1,numberOfCluster+1):
            cluster[cluster_id] = []
        initialCentroids = random.sample(points,numberOfCluster)
        centroid = initialCentroids
        flag = 1
        while flag == 1:
            for everyRow in points:
                cluster[euclideanDistance(everyRow,centroid)+1].append(everyRow)
            newCentroid = CalculateNewCentroid(cluster)
            flag = isTheCentroidEqual(newCentroid,centroid)
            if flag ==1:
                centroid = newCentroid
                for cluster_id in range(1,numberOfCluster+1):
                    cluster[cluster_id] = []
            elif flag == 0:
               cl_id_tr_in = findingInsatanceId(points,cluster)

    ## Calculating the total sum of squared error and sum of squared error for each cluster
        totalSSE = []
        Cluster_SSE = []
        for key,val in cluster.items():
            print("sum of square error for cluster: "),
            print(key),
            Cluster_SSE = calculateSSE(val,centroid[key-1])
            totalSSE.append(Cluster_SSE)
            print(Cluster_SSE)
            Cluster_SSE = []
        print("Sum of Squared Error for "+str(numberOfCluster)+" Cluster is : "),
        print(sum(totalSSE))
        SSE_Collection.append(sum(totalSSE))
        totalSSE = []
        print("The Cluster Mean for each cluster is")
        r= 0
        for eveyitem in centroid:
            print("Cluster "),
            print(r+1),
            print(eveyitem)
            r=r+1
        print("Cluster Id =====> Instance Id")
        for key,val in cl_id_tr_in.items():
            print(key),
            print("=======>"),
            print(val)
Number_of_Cluster = range(2,7)
plt.xlabel('Number Of Cluster')
plt.ylabel('Sum of Squared Error')
plt.title('total sum of squared errors vs. K')
plt.plot(Number_of_Cluster, SSE_Collection,'bo',Number_of_Cluster, SSE_Collection,'K')
plt.show()





