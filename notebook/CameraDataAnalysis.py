# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 20:06:47 2025

@author: Simran
"""

import os
import pandas as pd
import numpy as np

os.chdir(r"C:\Users\Simran\Documents\Python\Project\Project 1-20250904T101823Z-1-001\Project 1")

#Task 1: Create a dataframe “Camera_data” using Camera.csv.
Camera_data = pd.read_csv("Camera.csv")
Camera_data

#Task 2: Find out the percentage of blank values in each column
Camera_data.isnull().sum() 
Camera_data.isnull().sum()/len(Camera_data) * 100

#Task 3: View the statistical summary of the data 
print(Camera_data.describe())

#Task 4: Replace all the blank values with NaN.
Camera_data.replace('', np.nan, inplace = True) 
print(Camera_data)

#Task 5: Now replace all the Blank values with the column median.
Camera_data.loc[:,"Max resolution"]=Camera_data['Max resolution'].fillna(Camera_data['Max resolution'].median())

Camera_data.loc[:,"Low resolution"]=Camera_data['Low resolution'].fillna(Camera_data['Low resolution'].median())

Camera_data.loc[:,"Zoom wide (W)"]=Camera_data['Zoom wide (W)'].fillna(Camera_data['Zoom wide (W)'].median())

Camera_data.loc[:,"Macro focus range"]=Camera_data['Macro focus range'].fillna(Camera_data['Macro focus range'].median())

Camera_data.loc[:,"Storage included"]=Camera_data['Storage included'].fillna(Camera_data['Storage included'].median())

Camera_data.loc[:,"Weight (inc. batteries)"]=Camera_data['Weight (inc. batteries)'].fillna(Camera_data['Weight (inc. batteries)'].median())

Camera_data.loc[:,"Dimensions"]= Camera_data['Dimensions'].fillna(Camera_data['Dimensions'].median())

#Verify Missing Values are replaced 
Camera_data.isnull().sum() 

#Task 6: Add a new column “Discounted_Price” in which give a discount of 
#5% in the Price column.
Camera_data['Discounted_Price'] = Camera_data['Price']*0.95
Camera_data

#Task 7: Drop the columns Zoom Tele & Macro Focus range 
Camera_data_New = Camera_data.drop(['Zoom tele (T)','Macro focus range'],axis=1)
#Camera_data = Camera_data.drop(['Macro focus range'],axis=1)
Camera_data_New

#Task 8: Replace the Model Name “Agfa ePhoto CL50” with “Agfa ePhoto CL250” 
Camera_data['Model'] = Camera_data['Model'].replace('Agfa ePhoto CL50','Agfa ePhoto CL250')
Camera_data

#Validation check
result = Camera_data[Camera_data["Model"].str.contains("Agfa ePhoto CL250", case=False)]
print(result)

#Task 9: Rename the column name from Release Date to Release Year. 
Camera_data = Camera_data.rename(columns={'Release date':'Release Year'})
Camera_data

#Task 10: Which is the most expensive Camera? 
Camera_dataMax = (
    Camera_data.groupby('Model', as_index=False)['Price']
    .max()
    .sort_values(by='Price', ascending=False)
)
max_price = Camera_dataMax['Price'].max()
Camera_dataMax[Camera_dataMax['Price']==max_price]

#Task 11: Which camera have the least weight? 
Least_Weight = Camera_data['Weight (inc. batteries)'].min()
Least_Weight_Model_Name = Camera_data[Camera_data['Weight (inc. batteries)']==Least_Weight]['Model']
Least_Weight_Model_Name
print(Least_Weight_Model_Name + ' '+ 'has the least weight')

#Task 12: Group the data on the basis of their release year. 
Group_by_Release_year = Camera_data.groupby(['Release Year'])
Group_by_Release_year

for year, group in Group_by_Release_year:
    print(f"\nRelease Year: {year}")
    print(group)

#Task 13: Extract the Name, Storage Include, Price, Disounted_Price & Dimensions columns.
Camera_data[['Model','Storage included','Price','Discounted_Price','Dimensions']]

#Task 14: Extract the records for the cameras released in the year 2005 & 2006 
Camera_data[(Camera_data['Release Year']==2005) | (Camera_data['Release Year']==2006)]
#use 'in'
#'in' - operator

#Task 15: Find out 2007’s expensive & Cheapest Camera. 
#sort the data
Camera_data_2007 =  Camera_data[Camera_data['Release Year']==2007]
print(Camera_data_2007)

Cheapest_camera_2007_price =  Camera_data_2007['Price'].min()
Cheapest_camera_2007_Model = Camera_data_2007[Camera_data_2007['Price']==Cheapest_camera_2007_price]
Cheapest_camera_2007_Model['Model']

expensive_camera_2007_price = Camera_data_2007['Price'].max()
expensive_camera_2007_Model = Camera_data_2007[Camera_data_2007['Price']==expensive_camera_2007_price]
expensive_camera_2007_Model['Model']

#Task 16: Which Year maximum number of models is released?

Camera_data_Year_Model_Count =  Camera_data['Release Year'].value_counts()
Camera_data_Year_Model_Count.index[0]
print(Camera_data_Year_Model_Count.index[0] + " is the year where maximum models are released")




























