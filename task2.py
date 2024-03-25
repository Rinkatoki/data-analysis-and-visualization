import pandas as pd
import matplotlib.pyplot as plt
import csv
f= pd.read_csv('D:\\task2.csv')
print(f.head())
print("\n")
included_columns=f[['Name','phy_marks','mat_ma','en_mark','chem_mark']]
summary_stats = included_columns.describe(exclude='object')
print(summary_stats)
print("\n")
search_no=input("Enter the roll no to visualize the sem marks:")

with open('D:\\task2.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)
z=0
y=[]
for i in data_list:
    if(search_no==data_list[z]["Roll_no"]):
        req_name=data_list[z]["Name"]
        y.append(int(data_list[z]["phy_marks"]))
        y.append(int(data_list[z]["mat_ma"]))
        y.append(int(data_list[z]["en_mark"]))
        y.append(int(data_list[z]["chem_mark"]))
    z=z+1
x =["physics_mark","maths_mark","english_mark","chemistry_mark"]
plt.bar(x,y,color='blue')
plt.xlabel('Subjects')
plt.ylabel('performance of '+req_name)
plt.title('visualization')
plt.show()



