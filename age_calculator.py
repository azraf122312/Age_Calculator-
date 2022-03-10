def find_Age(current_date, current_month, current_year,
			birth_date, birth_month, birth_year):

	# if birth date is greater then current birth_date
	# then donot count this month and add 30 to the date so
	# as to substract the date and get the remaining days
	
	month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if (birth_date > current_date):
		current_month = current_month - 1
		current_date = current_date + month[birth_month-1]
		
		
	# if birth month exceeds current month, then
	# donot count this year and add 12 to the
	# month so that we can substract and find out
	# the difference
	if (birth_month > current_month):		
		current_year = current_year - 1;
		current_month = current_month + 12;
		
	# calculate date, month, year
	calculated_date = current_date - birth_date;
	calculated_month = current_month - birth_month;
	calculated_year = current_year - birth_year;
	
	# print present age
	print("Present Age")
	print("Years:", calculated_year, "Months:",
		calculated_month, "Days:", calculated_date)
	
# driver code
current_date = int(input("Please input the current Date: "))
current_month = int(input("Please input the current Month: "))
current_year = int(input("Please input the current Year: "))


# birth dd//mm//yyyy
birth_date = int(input("Please input the Birth Date: "))
birth_month = int(input("Please input the Birth Month: "))
birth_year = int(input("Please input the Birth Year: "))

find_Age(current_date, current_month, current_year,
		birth_date, birth_month, birth_year)
