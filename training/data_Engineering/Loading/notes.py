# region

#### Extract => Transforming => Loading (ETL)
#### Extract => Loading => Transforming (ELT): #? For big data

# region

#? Loading data:
# Save the final version of the data after transforming it.
#
#? Where is Data loaded:
#! get from slides
# Relational
# Data warehouses      
# Data lakes
# Cloud Storage
# 
#? Types of Data Loading:
#* Full load.
#   load all data at once (used for initial setups).
#* Incremental Load.
#   load only new or changed data (used for dialy updates).
#* Real-Time/ Straming Load.
#   load data continuously as it arrives.
#
#? Writing Data (Save files after transforming data)
#* df.to_csv ('output.csv', index=False).
#* df.to_excel ('output.xlsx', index=False).
#* df.to_json ('output.csv').

# region

#? Why use ELT:
#* Scalabibity
#* Flexivility
#* Faster Initial Load

# region

#? Accessing Data
#* Clice and dice in DataFreames:
#   Slice: select a subset of rows or columns from a DataFrame. [one dimention]
#   Dice: select a smaller sub-matrix [block of data] by specifying both rows and columns you're intrested in. [two dimentions]
#
#? To Do Slicing and Dincing:
#! [from : to]
#! [from row : to row, 'from col' : 'to col']
#
#? loc : Upper bound included
#* Slice
# row: 
#   - df.loc[1 : 3] 
#   - df.loc[2]
#   - df.loc[0 : 5]
# col: 
#   - df['Name'] 
#   - df.loc[:, 'Name' : 'Contry]
#* Dice
#   - df.loc[1 : 3, 'Name' : 'Contry'] 
#
#? iloc : Upper bound NOT included [iloc can't deal with text, index only]
#* Slice
# row:
#   - df.iloc[1 : 4] === df.loc[1 : 3]
# col:
#   - df.iloc[:, 0 : 3]
#* Dice
#   - df.iloc[0 : 5, 1 : 4]
#
# * iloc ignore the lable and set numbers.
# * loc can't ignore lables.
# region
#
#
#
# region