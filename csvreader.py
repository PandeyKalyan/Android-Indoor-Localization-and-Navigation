import csv

def loadDataset(filename):
    trainingSet = []
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(1, len(dataset)):
            for y in range(9):
                dataset[x][y] = float(dataset[x][y])
            trainingSet.append(dataset[x])
    return trainingSet
