from mymodules import *

def euc(a,b):
 return distance.euclidean(a,b)

class MarvellousKNN():
 def fit(self,TrainingData,TrainingTarget):
  self.TrainingData = TrainingData
  self.TrainingTarget = TrainingTarget
 
 def predict(self,TestData):
  predictions = []
  for row in TestData:
   lebel = self.closest(row)
   predictions.append(lebel)
  return predictions

 def closest(self,row):
  bestdistance = euc(row,self.TrainingData[0])
  bestindex = 0
  for i in range(1,len(self.TrainingData)):
   dist = euc(row,self.TrainingData[i])
   if dist < bestdistance:
    bestdistance = dist
   bestindex = i
  return self.TrainingTarget[bestindex]
  

def marvellousKNeighbor():
  border = "_"*50
  
  iris = load_iris()
  data = iris.data
  target= iris.target
  
  print(border)
  print("actual data set")
  print(border)
  
  for i in range(len(iris.target)):
   print("ID:%d,Label:%s,Feature:%s"%(i,iris.data[i],iris.target[i]))
  print("size of actual data set %d"%(i+1))
  
  data_train,data_test,target_train,target_test = train_test_split(data,target,test_size = 0.5)
 
  
  print(border)
  print("training data set")
  print(border)
  
  for i in range(len(data_train)):
   print("ID:%d,Label:%s,Feature:%s"%(i,data_train[i],target_train[i]))
  print("size of training data set %d"%(i+1))
  
  print(border)
  print("test data set")
  print(border)
  
  for i in range(len(data_test)):
   print("ID:%d,Label:%s,Feature:%s"%(i,data_test[i],target_test[i]))
  print("size of test data set %d"%(i+1))
 
  classifier = MarvellousKNN()
  
  classifier.fit(data_train,target_train)
  
  predictions = classifier.predict(data_test)
  
  Accuracy = accuracy_score(target_test,predictions)
  
  return Accuracy
  
def main():
 Accuracy = marvellousKNeighbor()
 print("accuracy of classification with KNN is",Accuracy*100,"%")

if __name__== "__main__": 
 main()