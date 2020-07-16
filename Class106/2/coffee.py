import csv
import numpy as np
def getDataSource(data_path):
    cups=[]
    sleep=[]
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":sleep, "y":cups}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("The Correlation Coefficient between the Data: \n",correlation[0,1])
def Setup():
    data_path = "coffee.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
Setup()