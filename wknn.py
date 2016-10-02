import csvreader
import operator
import interpolate

trainingSet = csvreader.loadDataset('/home/pandey/Desktop/Major_Project/rssi.csv')

def sorensonDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += abs(instance1[x] - instance2[x]) / \
            abs(instance1[x] + instance2[x])  # sorenson distance
    return distance


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-2  # 4
    for x in range(len(trainingSet)):
        dist = sorensonDistance(testInstance, trainingSet[x], length)
        distances.append([trainingSet[x], dist])
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    normalizer = 0
    for x in range(k):
        if  distances[x][1]== 0:
	        neighbors.append(distances[x])
	        return neighbors
        else:
             normalizer+=(1/distances[x][1])  #total of sorenson distance
    for x in range(k):
        distances[x][1]= 1/(distances[x][1]*normalizer)   #normalized weight 
        neighbors.append(distances[x])
    return neighbors


def initialCor(testInstance):
    pos = []
    pos=getNeighbors(trainingSet, testInstance, 3)
    x_cor = 0.0
    y_cor = 0.0
    k = 3
    if len(pos) < 3  or pos[0][1] > 0.75:
        	x_cor  = pos[0][0][7]
        	y_cor  = pos[0][0][8]
    else:
        for i in range(k):
            x_cor += pos[i][0][7]*pos[i][1]
            y_cor += pos[i][0][8]*pos[i][1]
	            

    print x_cor, y_cor
    location = interpolate.interpolate(x_cor, y_cor)
    f = open('db.json', 'wb')
    f.write('[{"geometry": {"type": "Point", "coordinates": [' + str(location[0]) +
            ',' + str(location[1]) + ']}, "type": "Feature", "properties": {}}]')
    f.close()
    return x_cor, y_cor
