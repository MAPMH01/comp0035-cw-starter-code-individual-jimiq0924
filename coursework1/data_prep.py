#Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import os


#1.Import data
##Read the excel file
filepath = os.path.join('County0010_initial.xlsx')
##Read xlsx files 
##Xlsx is read without defaulting to any sheets
ori_data = pd.read_excel(filepath,sheet_name = None)



#2.Check the data for null values
##check column'A100008_00'
print(pd.isna(ori_data['County0010']['A100008_00']))
print(type(ori_data['County0010']['A100008_00'][0]))
ori_sheet1_data = pd.read_excel(filepath,sheet_name = 'County0010')
print(ori_sheet1_data.value_counts('A100008_00'))
##check column'A100008_10'
print(pd.isna(ori_data['County0010']['A100008_10']))
print(type(ori_data['County0010']['A100008_10'][0]))
ori_sheet2_data = pd.read_excel(filepath,sheet_name = 'County0010')
print(ori_sheet2_data.value_counts('A100008_10'))
##check column'A100009_00'
print(pd.isna(ori_data['County0010']['A100009_00']))
print(type(ori_data['County0010']['A100009_00'][0]))
ori_sheet3_data = pd.read_excel(filepath,sheet_name = 'County0010')
print(ori_sheet3_data.value_counts('A100009_00'))
##check column'A100009_10'
print(pd.isna(ori_data['County0010']['A100009_10']))
print(type(ori_data['County0010']['A100009_10'][0]))
ori_sheet4_data = pd.read_excel(filepath,sheet_name = 'County0010')
print(ori_sheet4_data.value_counts('A100009_10'))



#3.Calculate the statistical characteristics of the data (mean, variance, etc.)
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


##Analyze column'A100009_00'
###calculate sum
col_A100009_00_sum = 0
###iterrow function gives index and object
for index,row in ori_sheet3_data.iterrows():
    print(index)
    print(type(row))
    print(row['A100009_00'])
    break

for index,row in ori_sheet3_data.iterrows():
    col_A100009_00_sum += row['A100009_00']
print(col_A100009_00_sum)

###mean value
col_A100009_00_mean = col_A100009_00_sum / (index+1)
print(col_A100009_00_mean)

###variance
col_A100009_00_var = 0
for index,row in ori_sheet3_data.iterrows():
    col_A100009_00_var += (col_A100009_00_mean - row['A100009_00'])**2
print(col_A100009_00_var)



#4.Extract useful data (convert data types to sets)
Prov_code_set = ori_sheet1_data.value_counts('GbProv')
print(type(Prov_code_set))
print(Prov_code_set.keys())
Prov_code_set = set(Prov_code_set.keys())
print(Prov_code_set)



#5.Build up the dictionary as the format{'province':[city,rural]}
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

##Build up the second dictionary for 2010
population_dic_10 = {}
for code in Prov_code_set:
    population_dic_10[code] = [0,0]
print(population_dic_10)

for index,row in ori_sheet1_data.iterrows():
    prov_code = row['GbProv']
    population_dic_10[prov_code][0] += row['A100008_10']
    population_dic_10[prov_code][1] += row['A100009_10']
print(population_dic_10)



#6.Save the new file
##Save the first file
population_dataframe = pd.DataFrame(population_dic_00,index=['Urban','Rural'])
population_dataframe.to_excel('County0010_prepared_2000.xlsx',sheet_name = 'population list',index = True, header = True)
##Save the second file
population_dataframe = pd.DataFrame(population_dic_10,index=['Urban','Rural'])
population_dataframe.to_excel('County0010_prepared_2010.xlsx',sheet_name = 'population list',index = True, header = True)



#7.Data Visualisation
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


####Draw the graph for 2010
###Initialise two lists
urban_list_2 = []
rural_list_2 = []
for item in population_dic_10.items():
    urban_list_2.append(item[1][0])
    rural_list_2.append(item[1][1])
print(type(item))

###plot the graph 
plt.scatter(urban_list_2,rural_list_2)
plt.title('The rural population against the urban population in 2010')
plt.xlabel('Urban population')
plt.ylabel('Rural population')
plt.show()