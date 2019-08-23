import random


sales = {} # month, profit/loss(total)
salesvar = {} # month, variation in profit/loss(total)

profitloss = 0
last_month_amount  = 0


f=open("pybank.csv", "r")
#cvsreader = cvs.reader

num = 1

f1 = f.readlines()

for x in f1:

	if num > 1:
		date,amount = x.split(",")
		keymonth,year = date.split("-")

		#print (keymonth)
		#print (year)
		exists = date in sales.keys()
		#print (exists)
		
		if exists == True:
			sales[date] = int(sales[date]) + int(amount)
		else:
			sales[date] = int(amount)  
			
		if (last_month_amount!=0):			
			salesvar[date] = int(amount) - last_month_amount	
		else:
			salesvar[date] = 0
			
		last_month_amount = int(amount)	
	num = num + 1
	
total_sales = 0	
min_var = 0
min_month_var = ""
max_var = 0 
max_month_var = ""
total_var = 0


for month in sales:
	total_sales = total_sales + sales[month]
	total_var = total_var + int(salesvar[month]) 
	
	if (max_var==0 or max_var < salesvar[month]):
		max_var = salesvar[month]
		max_month_var = str(month)

	if (min_var==0 or min_var > salesvar[month]):
		min_var = salesvar[month]
		min_month_var = str(month)
			
	#print (month)
	#print ("sales are %s and difference is %s" % (sales[month],salesvar[month]))

print ("total months analyzed: %s" %(num-2))	
print ("total profit: $%s" %(total_sales))
print("Average  Change: $%s" %(round(total_var/(num-3),2)))
print("Greatest Increase in Profits: %s $%s" %(max_month_var,max_var)) 
print("Greatest Decrease in Profits: %s $%s" %(min_month_var,min_var)) 

fo=open("py_bank_report.txt","w+")

fo.write("total months: %s\n" %(num-2))	
fo.write ("total profit: $%s\n" %(total_sales))
fo.write("Average  Change: $%s\n" %(round(total_var/(num-3),2)))
fo.write("Greatest Increase in Profits: %s $%s\n" %(max_month_var,max_var)) 
fo.write("Greatest Decrease in Profits: %s $%s\n" %(min_month_var,min_var)) 

print("Please check file py_bank_report.txt for more details")

f.close() 
fo.close() 



