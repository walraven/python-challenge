#pyBank Homework by Taylor Walraven
import pandas as pd #makes this homework easy...
import os

#set the filename
csv_path = os.path.join('Resources', 'budget_data.csv')

#read file into dataframe
budget_df = pd.read_csv(csv_path)

#determine the number of months
num_months = budget_df['Date'].count()

#determine the total of amount of profit/losses
total_p_l = budget_df['Profit/Losses'].sum()

#determine the greatest increase in profits
max_inc = budget_df['Profit/Losses'].max()

#...and it's associated date :: there's probably a one-line way to do this.
#give an index to dataframe to use loc
budget_df = budget_df.reset_index()
inc_date_row = budget_df.loc[budget_df['Profit/Losses'] == max_inc, 'Date']
inc_date = inc_date_row.min() #it's the only value

#determine the greatest loss and it's associated date (2 lines possible?)
max_dec = budget_df['Profit/Losses'].min()
dec_date_row = budget_df.loc[budget_df['Profit/Losses'] == max_dec, 'Date']
dec_date = dec_date_row.max() #the biggest loser...out of all 1 losers

#print to terminal
print ("Financial Analysis")
print ("==============================")
print ("Total Months: {}".format(num_months))
print ("Total: ${}".format(total_p_l))   #watch out for long, ugly floats!
print ("Average Change: ${}".format(round(total_p_l / num_months, 2))) 
print ("Greatest Increase in Profits: {} (${})".format(max_inc, inc_date))
print ("Greatest Decrease in Profits: {} (${})".format(max_dec, dec_date))

#print to txt file

#set filename
file_name = os.path.join("output.txt")

#this is gonna seem familiar
with open (file_name, mode = 'w') as text_file:
    text_file.write ("Financial Analysis\n")
    text_file.write ("==============================\n")
    text_file.write ("Total Months: {}\n".format(num_months))
    text_file.write ("Total: ${}\n".format(total_p_l)) #who cares about less than a penny?
    text_file.write ("Average Change: ${}\n".format(round(total_p_l / num_months, 2))) 
    text_file.write ("Greatest Increase in Profits: {} (${})\n".format(inc_date, max_inc))
    text_file.write ("Greatest Decrease in Profits: {} (${})\n".format(dec_date, max_dec))

    #wrap it up
    text_file.close()