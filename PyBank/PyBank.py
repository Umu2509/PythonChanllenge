        #PYBANK CHALLENGE

# The total number of months included in the dataset

# The total amount of revenue gained over the entire period

# The average change in revenue between months over the entire period

# The greatest increase in revenue (date and amount) over the entire period

# The greatest decrease in revenue (date and amount) over the entire period





# import files

import os
import csv

# open filepaths
filepath = os.path.join("raw_data","budget_data_1.csv")


# Make list for the variables

list_month = []
list_revenue = []


print("""Financial Analysis
----------------------------""")

#Read files
with  open(filepath, mode = 'r', newline="")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

    months = 0

    total_revenue = 0


#create a loop   

    for row in csvreader:

        revenue = int(row[1])

        total_revenue = total_revenue + revenue

        months = months + 1



        list_revenue.append(revenue)

        list_month.append(row[0])

#print months and revenue

    print(f"Total Months: {months}")

    print(f"Total Revenue: ${total_revenue}")


# define a function 

def average(list):

     total = sum(list)

     return total/len(list)


revenue_change_amount = [x - list_revenue[i - 1] 
for i, x in enumerate(list_revenue)][1:]



# call the avearge function 

print(f"Average Revenue Change: {average(revenue_change_amount)}")


revenue_change_month = list_month[1:]


revenue_change_dict = dict(zip(revenue_change_month,revenue_change_amount))


# define the dictionary greatest_increase

def greatest_increase(dict): 

    key=list(dict.keys())

    val=list(dict.values())

    maxval = max(val)

    month = key[val.index(maxval)]

    
    print(f"Greatest Increase in Revenue: {month} (${maxval})")


#   define the dictionary greatest_decresaeS

def greatest_decrease(dict): 

    key=list(dict.keys())

    val=list(dict.values())

    minval = min(val)

    month = key[val.index(minval)]

    print(f"Greatest Decrease in Revenue: {month} (${minval})")


greatest_increase(revenue_change_dict)

greatest_decrease(revenue_change_dict)