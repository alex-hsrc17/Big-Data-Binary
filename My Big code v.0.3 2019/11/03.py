# Big-Data-Binary

task = "binar data job ver.0.3"
import numpy as np
import urllib.request as urllib
# url with dataset
  ##url = "https://dropmefiles.com.ua/hHVk8"   #url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

# download the file
  ## raw_data = urllib.urlopen(url)    #open (url)
raw_data = open("tabular_data.csv")
#rez_data = open("tabular_data.csv")

# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",", skiprows=1)


# separate the data from the target attributes
X = dataset[:,2:44]
y = [0,0,0,0,0,0,1,1,1]
print (X,y)
