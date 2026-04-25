bill = None

while bill is None:
	try:
		my_number = input('Please enter bill to split: ')
		Initial_bill = float(my_number)
		if Initial_bill <= 0:
			print('The number must be greater than 0.')
		else:
			bill = Initial_bill
	except ValueError:
		print('Invalid input. Bill must be a number')
	

tip_percentage = None
while tip_percentage is None:
	try:
		original_tip = float(input("please enter tip percentage: "))
		if original_tip <= 0:
			print('Tip percentage must be greater than 0')
		else:
			tip_percentage = original_tip
	except ValueError:
		print('Invalid input. Please enter a numerical value.')
	   

people = None
while people is None:
	try:
		num_people = float(input("Please enter the number of people paying"))
		if num_people <=0:
			print("Please enter valid number greater than 0")
		else:
			people = num_people
	except ValueError:
		  print("Invalid input; Please enter a numerical value")
    
percentage_tip = tip_percentage / 100
bill_and_tip =  bill * percentage_tip
per_person_bill = bill_and_tip / people
print(f"Your individual contribution is: {per_person_bill:.2f}")
