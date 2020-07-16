import csv
import numpy as np
def getDataSource(data_path):
    marks=[]
    days=[]
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return{"x":days, "y":days}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("The Correlation Coefficient between the Data: \n",correlation[0,1])
def Setup():
    data_path = "marks.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
Setup()