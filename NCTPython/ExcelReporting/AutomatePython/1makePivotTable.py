# Installed these for python on the machine
# Also had to make sure they were applied to pycharm
# pip install xlrd
# pip install pandas
# pip install openpyxl
import pandas as pd

# Read Excel File
df = pd.read_excel('supermarket_sales.xlsx')

# Select columns: 'Gender', 'Product line', 'Total'
# These are 3 of the columns in the original spreadsheet
'''
Gender	    Product line            Total
Female	    Health and beauty       548.9715
Female	    Electronic accessories  80.22
Male	    Home and lifestyle      340.5255
Male	    Health and beauty       489.048
'''
df = df[['Gender', 'Product line', 'Total']]

# Make pivot table
pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)
'''
This is what the Pivot table will come out as, though I shortened up the column titles for notes
From original sheet, the gender column has either male and female, for thousands of purchases
So 'index' will separate those options from that specific collected column
Then 'columns' will separate the items in that specific collected column
Then 'values' along with 'sum' if a Male bought EA, add it to that correlated cell. 
---------------------------------------------------
Gender	EA	    FA	    F&B	    H&B	    H&L	    S&T
Female	27102	30437	33171	18561	30037	28575
Male	27236	23868	22974	30633	23825	26548

'''

# Export pivot table to Excel file
pivot_table.to_excel('1.make-pivot-table.xlsx', 'Report', startrow=4)
