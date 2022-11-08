```
Import required libraries

import pandas as pd
import matplotlib.pyplot as plt
import os
```

In this section, we imported the Pandas, Matplotlib, and OS libraries. The pandas library is used to read and process CSV and XLSX files. The os library is used to get files directly from the system path. The matplotlib library is used for data visualization.



# Exploration of County_0010_initial.xlsx

# 1.Import data
```
filepath = os.path.join('County0010_initial.xlsx')
ori_data = pd.read_excel(filepath,sheet_name = None)
```

In this section, we read the County_0010_initial file without defaulting to any sheets by using os and pandans library.


# 2.Check the data for null values
```
## check column'A100008_00'
print(pd.isna(ori_data['County0010']['A100008_00']))
print(type(ori_data['County0010']['A100008_00'][0]))
ori_sheet1_data = pd.read_excel(filepath,sheet_name = 'County0010')
print(ori_sheet1_data.value_counts('A100008_00'))
```

# Taking this code as an example, in this section we perform null checks on the four columns of data that need to be used.
# The logic for determining whether a column has a null value is: if any row of a column is empty, it returns true; If false is returned, no row is empty。

```
print(pd.isna(ori_data['County0010']['A100008_00']))
```
# Using this line of code as an example, if the data has null values, run this line to show where values are null and where are not

```
print(type(ori_data['County0010']['A100008_00'][0]))
```
# Using this line of code as an example，suppose we know that a row is not a null value, then look at its data type


# 3.Calculate the statistical characteristics of the data
# In this section, we analyze the statistical characteristics of the urban population in 2000 and 2010, and calculate the sum, mean, and variance of the two sets of data. Taking the urban population in 2000 as an example, the code to implement the calculation is as follows:

```
##Analyze column'A100008_00'
###calculate sum
col_A100008_00_sum = 0
###iterrow function gives index and object
for index,row in ori_sheet1_data.iterrows():
    print(index)
    print(type(row))
    print(row['A100008_00'])
    break

for index,row in ori_sheet1_data.iterrows():
    col_A100008_00_sum += row['A100008_00']
print(col_A100008_00_sum)

###mean value
col_A100008_00_mean = col_A100008_00_sum / (index+1)
print(col_A100008_00_mean)

###variance
col_A100008_00_var = 0
for index,row in ori_sheet1_data.iterrows():
    col_A100008_00_var += (col_A100008_00_mean - row['A100008_00'])**2
print(col_A100008_00_var)
```

From this part of the calculation, we get a huge variance, which represents a huge difference in population distribution in different regions of China. At the same time, we can also compare the variance between 2000 and 2010, and from the calculation results, the variance shows a downward trend. This means that the proportion of urbanization in various regions has become higher and higher in the past 10 years.


# 4.Extract useful data (convert data types to sets)

```
Prov_code_set = ori_sheet1_data.value_counts('GbProv')
print(type(Prov_code_set))
print(Prov_code_set.keys())
Prov_code_set = set(Prov_code_set.keys())
print(Prov_code_set)
```

In this code, we extract the data information of the province code and convert it into set format, which is ready for the next step of building a dictionary.


# 5.Build up the dictionary as the format{'province':[city,rural]}

```
##Build up the first dictionary for 2000
population_dic_00 = {}
for code in Prov_code_set:
    population_dic_00[code] = [0,0]
print(population_dic_00)

for index,row in ori_sheet1_data.iterrows():
    prov_code = row['GbProv']
    population_dic_00[prov_code][0] += row['A100008_00']
    population_dic_00[prov_code][1] += row['A100009_00']
print(population_dic_00)
```

In this section, we created two dictionaries of urban and rural population data for 2000 and 2010 by province code, in the format {'province':[city,rural]}. As shown above, this part of the code created and printed the 2000 urban and rural population data dictionary.


# 6.Save the new file
We save the two dictionaries created in the previous step in xlsx format files through this part of the code, so that we can more intuitively observe the difference in urban and rural population distribution between the two years. The main implementation principle is to convert python native data types to pandas dataFrame types. The code used is as follows:

```
population_dataframe = pd.DataFrame(population_dic_00,index=['Urban','Rural'])
population_dataframe.to_excel('County0010_prepared_2000.xlsx',sheet_name = 'population list',index = True, header = True)
```

# 7.Data Visualisation

```
##Draw the graph for 2000
###Initialise two lists
urban_list_1 = []
rural_list_1 = []
for item in population_dic_00.items():
    urban_list_1.append(item[1][0])
    rural_list_1.append(item[1][1])
print(type(item))

###plot the graph 
plt.scatter(urban_list_1,rural_list_1)
plt.title('The rural population against the urban population in 2000')
plt.xlabel('Urban population')
plt.ylabel('Rural population')
plt.show()
```

In this section, we use the matplotlib library to represent the previously created dictionary as a scatter plot. The horizontal axis of the scatter plot is the urban population, and the vertical axis of the scatter plot is the rural population. From the drawn image, we can group the points in the scatter plot (each point represents a province). The dot in the upper left corner represents a larger rural population than an urban population, which we can speculate is an underdeveloped area, and vice versa, the dot in the lower right corner represents a developed area.