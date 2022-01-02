import pandas as pd 
from sklearn.cluster import KMeans 
import csv
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt
import seaborn as sns

rows = []

with open("main.csv")as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
headers[0] = "row_num"

temp_star_data_rows = list(star_data_rows)
for star_data in temp_star_data_rows:
    star_mass = star_data[3]
    star_radius = star_data[4] 

X = []
for index, star_mass in enumerate(star_mass):
  temp_list = [star_radius[index], star_mass]
  X.append(temp_list)

print(X)

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters = i, init = "k-means++", random_state=42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.figure(figsize = (10,5))
sns.lineplot(range(1,11),wcss, marker="o", color = "red")
plt.show()