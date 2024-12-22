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
print(ser)

newDataaFrame = pd.DataFrame(np.random.rand(100,5),index= np.arange(100)) #creat a random 100 rows and 5 coloums data frame with all the series will be floating numbers
print(newDataaFrame)
print(type(newDataaFrame))
print(newDataaFrame.dtypes)#print data types of all the coloum/series