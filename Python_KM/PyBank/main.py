#Python - open and read csv file
import csv
file_location = '../Instructions/PyBank/Resources/budget_data.csv'
#count how many months
month_counter = 0
#The net total amount of "Profit/Losses" over the entire period
net_total = 0
#store the profits/losses in own column to calculate stuff
PL_list = []
#store months to associate changes with each month
month_list = []
#need new column/list for change between months
PL_change_list = []
#need list to show changes appended to corresponding months
change_month = []


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
		net_total += (int(rows[1]))
		PL_list.append((int(rows[1])))
		month_list.append(str(rows[0]))
#check that lists were made properly
print(PL_list)
print(month_list)
#loop through bank list to calculate change between months
for i in range(len(PL_list)):
#skip first value [0] since there's no row before it to calculate change
	if i >= 1:
		PL_change_list.append((PL_list[i] - PL_list[i-1]))
	#attach to corresponding month
		change_month.append(month_list[i])


#check that list made properly and that there's proper number of values
print(PL_change_list)
print(len(PL_change_list))
print(change_month)
print(len(change_month))

#find average of changes
#sum
change_sum = 0
for value in PL_change_list:
	change_sum += value
print(change_sum)
#count of values
change_count = len(PL_change_list)
print(change_count)
#calculate average
average_change = (float(change_sum) / float(change_count))
print(average_change)


#greatest increase

greatest_increase = max(PL_change_list)
index_GI = PL_change_list.index(max(PL_change_list))
print(index_GI)

month_GI = change_month[int(index_GI)]

#greatest decrease
greatest_decrease = min(PL_change_list)
index_GD = PL_change_list.index(min(PL_change_list))
print(index_GD)

month_GD = change_month[int(index_GD)]



# print final analysis
print("")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_counter}")
print(f"Net total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month_GI} (${greatest_increase})")
print(f"Greatest Decrease in Profits:{month_GD} (${greatest_decrease})")

#create a .txt file
txtfile = open("Financial_Analysis.txt",'w')
txtfile.write("Financial Analysis\n")
txtfile.write("----------------------------\n")
txtfile.write(f"Total Months: {month_counter}\n")
txtfile.write(f"Net total: ${net_total}\n")
txtfile.write(f"Average Change: ${average_change}\n")
txtfile.write(f"Greatest Increase in Profits: {month_GI} (${greatest_increase})\n")
txtfile.write(f"Greatest Decrease in Profits:{month_GD} (${greatest_decrease})\n")
txtfile.close()
print("")
print("Analysis complete. .txt file created.")
