import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def meanData(arr):
 size = len(arr)
 sum = 0
 
 for i in range(size):
  sum = sum +arr[i]
  
 return (sum/size)

def marvellousHeadBrain(Name):
 dataset = pd.read_csv(Name)
 print("size of our dataset is",dataset.shape)
 
 x =dataset["Head Size(cm^3)"].values
 y = dataset["Brain Weight(grams)"].values
 
 print("length of x",len(x))
 print("length of x",len(x))
 
 mean_x = meanData(x)
 mean_y = meanData(y)
 
 print("mean of independent variable is",mean_x)
 print("mean of dependent variable is",mean_y)
 
 
#m = (sum(x-xb)*(y-yb))/sum(x-xb)2
 numerator = 0
 denomenator = 0
 
 for i in range(len(x)):
  numerator = numerator +(x[i]-mean_x)*(y[i]-mean_y)       #xb=mean_x
  denominator = denomenator +(x[i]-mean_x)**2
  
 m = numerator/denomenator
 print("value of slope is",m)
 
 #y=mx+c
 #c = y - mx
 #c = mean_y - (m*mean_x)
 
 c = mean_y - (m * mean_x)
 print("value of y intercept is:",c)
 
 x_Start = np.min(x) - 200
 x_End = np.max(x) + 200
 
 x = np.linspace(x_Start,x_End)
 y = m*x + c
 
 plt.plot(x,y,color ='r',label = "Regression Line")
 plt.scatter(x,y,color = 'b',label = "Data plot")
 
 plt.xlabel("head size")
 plt.ylabel("brain weight")
 
 plt.legend()
 plt.show()


def main():
 print("enter file name of dataset")
 name = input()
 
 marvellousHeadBrain(name)

if __name__== "__main__":
 main()