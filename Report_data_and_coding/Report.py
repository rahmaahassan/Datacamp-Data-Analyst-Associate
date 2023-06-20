import pandas as pd
import numpy as np

data = pd.read_csv('pet_supplies_2212.csv')

missValues = data.isna().sum() #missing values for every column
print(missValues)

''' Data cleaning '''

#replace "unlisted" by NA in price column
data.price.replace('unlisted',np.nan,inplace=True)

#convert price values to continuous values anf replace NA by the median
data['price'] = data['price'].astype('float64').fillna(round(data.price.median(),2))

#convert rating values to discrete and fill NA with 0
data['rating']=data['rating'].fillna(0).astype(int)

#convert product_id,repeat_purchase,category, animal, size values to categorical
data=data.astype({"product_id":'category',"repeat_purchase":'category',"category":'category',"animal":'category',"size":'category'})

''' Data validation '''

#check dataset to see if the changes have been done
print(data.head())
print(data.info())
print(data.isna().sum())

#export data for visualization
data.to_csv('pet_supplies_2212_cleaned.csv')

''' I made some visualizations with Power BI because i wanted to use differents tools '''