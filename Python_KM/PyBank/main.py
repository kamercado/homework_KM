#Python - open and read csv file
import csv
file_location = '../Instructions/PyBank/Resources/budget_data.csv'
#count how many months
month_counter = 0
#The net total amount of "Profit/Losses" over the entire period
profit_losses = 0
#average change
index = 0
bank_list =[]

#greatest increase

#greatest decrease

#read csvfile
with open (file_location, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)
	print(f"CSV Header: {csv_header}")


#loop through rows in csv file to get info
	for rows in csvreader:
		#how many months
		month_counter += 1
		print(rows)
		#net total
		profit_losses += (int(rows[1]))
		#change
		index += 1
		bank_list.append((int(rows[1])))



# print final analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_counter}")
print(f"Net total: ${profit_losses}")
print(bank_list)
print(date)
print(amount)

