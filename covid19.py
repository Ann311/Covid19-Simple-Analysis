#Import dataset
import pandas as pd
data=pd.read_csv('covid19.csv')
#Cleaning of the data
data.drop(['Sno','Time','Date','ConfirmedIndianNational','ConfirmedForeignNational'],inplace=True,axis=1) #Here we cancel the mutiple column by a list
#Splitting of data into x and y
x=data.iloc[:,0].values
y=data.iloc[:,1:].values
#Encoding the data
from sklearn.preprocessing import LabelEncoder 
lab=LabelEncoder()
x=lab.fit_transform(x)                   #Encoded the name of states into number in alphabetical order
#Visualizing the data
from matplotlib import pyplot as plt
w=0.35                                   #variable is used as width of the bar
plt.subplots(figsize=(10,7))
p1=plt.bar(x,y[:,2],w,color='r')
p2=plt.bar(x-w,y[:,0],w,color='g')
p3=plt.bar(x+w,y[:,1],w,color='b')
plt.xticks(x)
plt.legend((p1,p2,p3),('CONFIRMED','CURED','DEATHS'))
plt.xlabel('States')
plt.ylabel('No.of people')
