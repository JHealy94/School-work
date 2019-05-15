#Purpose: building a classifier for finding the nearest neighbors
#James Healy
#AI midterm
#March 28, 2019
#The three closest neighbors to record #10 are the index positions of [9, 5, 2]

import csv
from sklearn.neighbors import NearestNeighbors

nearest=NearestNeighbors()
file_name = "midterm_SP2019.csv"
data = []

with open(file_name) as csv_file:
    dataReader=csv.reader(csv_file, delimiter=",")
    row_count=0
    for r in dataReader:
        #if row isnt blank on the csv sheet the program will increment the row counter and create a new row item
        #to add to the data sheet
        if r:
            row_count=row_count+1
            row=[]
            row.append(float(r[1]))
            #else-if statements to go see what value is stored in the row that informs if a person is married or not
            if(r[2]==' Single'):
                row.append(0)
            elif(r[2]==' Married'):
                row.append(1)
            elif(r[2]==' Other'):
                row.append(2)
            row.append(float(r[3]))
            data.append(row)
nearest.fit(data)
print ("row count ", row_count)
print("The index of the three closest neighbors to the position of [66, Married, 36120.34] is:")
print(nearest.kneighbors([data[9]],3,return_distance=False))

