import pandas as pd
import numpy as np

dict = {
    "Name":["Aman","Sohail","Arman","Bickey"],
    "Marks":[89,98,76,65],
    "Rank":[1,2,3,4]
}

df = pd.DataFrame(dict)
#print(df)

#print(df.head(2))#print head 2 rows only
#print(df.tail(2))#print tail 2 rows only

#print(df.describe())#print min ,max ,mean ,std 

#df.to_csv("AmanDetails.csv")


tranDetails ={
    "Train Number": [
        12345, 12346, 12347, 12348, 12349, 12350, 12351, 12352, 12353, 12354, 12355, 12356, 12357, 12358, 12359
    ],
    "Speed (km/h)": [
        110, 120, 95, 105, 115, 130, 90, 100, 85, 140, 125, 135, 98, 110, 145
    ],
    "Train Name": [
        "Rajdhani Express", "Shatabdi Express", "Duronto Express", "Garib Rath", "Vande Bharat",
        "Jan Shatabdi", "Humsafar Express", "Tejas Express", "Mahamana Express", "Kavi Guru Express",
        "Sampark Kranti", "Antyodaya Express", "Uday Express", "Gatimaan Express", "Superfast Express"
    ],
    "City": [
        "Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore", 
        "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Lucknow",
        "Bhopal", "Patna", "Indore", "Chandigarh", "Coimbatore"
    ]
}

train = pd.DataFrame(tranDetails)


train.to_csv('TrainData.csv')
ordinal_list = [
    "first", "second", "third", "fourth", "fifth", 
    "sixth", "seventh", "eighth", "ninth", "tenth", 
    "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth"
]

# print(train["Speed (km/h)"][0])#its print the 0th index value of col speed (km/h)
# train["Speed (km/h)"][0] = 120#and here we are changing that value 
train.index=ordinal_list#changing index 0 , 1, 2 to first second 
#print(train)


ser = pd.Series(np.random.rand(5), index=np.arange(5)) #creat a random float of 5 rows series
#print(ser)

newDataaFrame = pd.DataFrame(np.random.rand(100,5),index= np.arange(100)) #creat a random 100 rows and 5 coloums data frame with all the series will be floating numbers
# print(newDataaFrame)
#print(type(newDataaFrame))
#print(newDataaFrame.dtypes)#print data types of all the coloum/series

#print(newDataaFrame.to_numpy())

newDataaFrame.T #transpose 
#print(newDataaFrame.head())

#shorting the index
newDataaFrame.sort_index(axis=0,ascending=False,inplace=True)#axis = 0 means Rows, axis = 1 means coloums
#if we will not use implace  = true , this will  creat a new data frame instead of modyfying

#print(newDataaFrame)


newdf = newDataaFrame # it will only creat a any copy with the name of newdf it will only point to the newDataFrame if i change any thing to newdf it will change newDataFrame it creat a only view

#newdf[0][0] = 0.11
#print(newDataaFrame)

#To creat a copy of dataframe 
newdf2 = newDataaFrame.copy()

newdf2.sort_index(axis=0,ascending=True,inplace= True)
#for changing any data from dataframe we have to use .loc function
newdf2.loc[0,0] = 0.1234
#print(newdf2.head())


#for deleting any col 
newdf2.drop(0,axis=1,inplace=True)# for deleting coloum for row axis = 0
# print(newdf2.head())


newdf2.columns = ["A", "B", "C", "D"]  # Match the number of columns in newdf2
#print(newdf2.head())

#for printing only a part of th data it will only in view mode
#print(newdf2.loc[[4,5,6] ,['A','B','C']])



#we can use CURD operation in the dataframe
#print(newdf2.loc[(newdf2['A']<0.3) & (newdf2['C']>0.1)])


#when we need to select the data by the index only wether the indexing by number or any string name 
#print(newdf2.iloc[0,3])

#print(newdf2)
#print(newdf2.drop([1,5],axis=0))

#for setting the new index 
#print(newdf2.reset_index())#it will add new col of index 
 #if we dont want new col of index we want to change the index we can do 
#print(newdf2.reset_index(drop=True))



#To check wether the col is null or not 
#print(newdf2['B'].isnull())


#for getting the dimension of data frame 
# print(newdf2.shape)

#for information about dataframe
# print(newdf2.info)


#-------------------------------------------------------------------

#ASSIGMENT BY CODE WITH HARRY 
#CREAT A DATAFRAME WHICH CONTAINS ONLY INTEGERS WITH 3 ROW 2 COLUMNS AND RUN THE FOLLOWING DATAFRAME METHODS

# df.describe()
# df.mean()
# df.corr()
# df.count()
# df.max()
# df.min()
# df.median()
# df.std()

# df = pd.DataFrame(np.random.randint(0,9 ,size=(3,2)))
# df.columns = ['A','B']
# df.index = ['X','Y','Z']
# print(df)
# print("\nPrinting the describe function...\n")
# print(df.describe())
# print("\nPrinting the Mean function...\n")
# print(df.mean())
# print("\nPrinting the Corr function...\n")
# print(df.corr())
# print("\nPrinting the Count function...\n")
# print(df.count())
# print("\nPrinting the Max function...\n")
# print(df.max())
# print("\nPrinting the Min function...\n")
# print(df.min())
# print("\nPrinting the Medin function...\n")
# print(df.median())
# print("\nPrinting the std function...\n")
# print(df.std())








# -------------------------------------------------------
data = pd.read_excel('DSA sheet.xlsx')
print(data.head())