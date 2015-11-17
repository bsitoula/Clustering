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
    #numberOfCluster = input("Enter The Number Of Cluster")
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
            #print(centroid[key-1])
            print("sum of square error for cluster: "),
            print(key),
            Cluster_SSE = calculateSSE(val,centroid[key-1])
            totalSSE.append(Cluster_SSE)
            print(Cluster_SSE)
            Cluster_SSE = []
        print("Sum of Squared Error for "+str(numberOfCluster)+" is : "),
        print(sum(totalSSE))
        SSE_Collection.append(sum(totalSSE))
        totalSSE = []
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
def findingInsatanceId(initialPoints,cluster):
    temp = {}
    print("Cluster Id with their Instances ID")
    for i in range(1,len(cluster)+1):
        temp[i] = []
    for key,val in cluster.items():
        for everyInstance in val:
            temp[key].append(initialPoints.index(everyInstance))
    return temp