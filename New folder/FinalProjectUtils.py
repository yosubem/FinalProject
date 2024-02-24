import re


#This function checks if the given id is valid
def is_id_valid(id):
	id_ok = False
	id_len = 9

	if(not id.isdigit()):
		print("Employee id should consist of numbers only.")
	elif(not(len(id) == id_len)):
		print("Employee id should have %d numbers." % (id_len))
	elif(is_id_exist(id)):
		print("The employee is already registered, check if you entered the employee id correctly.")
	else:
		id_ok = True
	
	return id_ok

#This function checks if the given name is valid
def is_name_valid(name):
	name_ok = False

	if(not name.isalpha()):
		print("Names should consist of letters only, please enter again")
	else:
		name_ok = True
	
	return name_ok

#This function checks if the given phone is valid	
def is_phone_valid(phone):
	phone_ok = False
	phone_len = 10

	if(not phone.isdigit()):
		print("Phone number should consist of numbers only, please enter again")
	elif(not(len(phone) == phone_len)):
		print("Phone number should have %d numbers, please try again" % (phone_len))
	else:
		phone_ok = True
	
	return phone_ok

#This function checks if the given age is valid
def is_age_valid(age):
	age_ok = False
	youngest = 15		#The youngest employee can be
	oldest = 80			#The oldest employee can be

	if(not age.isdigit()):
		print("Age should consist of numbers only, please enter again")
	elif((int(age) <  youngest) or (int(age) > oldest)):
		print("The employee should be between %d to %d years old" % (youngest, oldest))
	else:
		age_ok = True

	return age_ok

#This function adds an employee
def add_employee(info_string, employee_id):
		#exist = False		#A flag to check if the employee already exist
	"""with open("Employee.txt", "r+") as employees_file:
	
		#Checking if the employee already exist. If so, prints an error to the user
		#and  changes "exist" value to True.
		for line in employees_file:
			if(employee_id == line[0:line.find(",")]):
				print("The employee is already registered, check if you entered the employee id correctly.")
				exist = True
				break"""
		
		#If the it is a new employee, add it to the end of the file 
		#if(not exist):
	with open("Employee.txt" "r+") as employees_file:
		employees_file.write(info_string)

#This function checks if the id already exist in the employee file
def is_id_exist(id):
	exist = False		#A flag to check if the employee already exist
	with open("Employee.txt", "r") as employees_file:
		
		#Checking if the employee already exist. If so, prints an error to the user
		#and  changes "exist" value to True.
		for line in employees_file:
			if(id == line[0:line.find(",")]):
				#print("The employee is already registered, check if you entered the employee id correctly.")
				exist = True
				break

	return exist

#This function is letting the user adding a single employee manually
def add_employee_manually():
	id_ok = False
	name_ok = False
	phone_ok = False
	age_ok = False

	while(not id_ok):
		employee_id = input("Please enter an employee's id: ")
		id_ok = is_id_valid(employee_id)		#Calls a helper function to check if the id is valid

		"""if(not employee_id.isdigit()):
			print("Employee id should consist of numbers only, please try again")
		elif(not(len(employee_id) == id_len)):
			print("Employee id should have %d numbers, please try again" % (id_len))
		else:
			id_ok = True"""

	while(not name_ok):
		employee_name = input("And now enter the employee's name: ")
		name_ok = is_name_valid(employee_name)	#Calls a helper function to check if the name is valid
		"""if(not employee_name.isalpha()):
			print("Names should consist of letters only, please enter again")
		else:
			name_ok = True"""
			
	while(not phone_ok):
		phone = input("Their phone number: ")
		phone_ok = is_phone_valid(phone)		#Calls a helper function to check if the phone number is valid
		"""if(not phone.isdigit()):
			print("Phone number should consist of numbers only, please enter again")
		elif(not(len(phone) == phone_len)):
			print("Phone number should have %d numbers, please try again" % (phone_len))
		else:
			phone_ok = True"""
		
	while(not age_ok):
		age = input("How old are they? ")
		age_ok = is_age_valid(age)		#Calls a helper function to check if the age is valid
		"""if(not age.isdigit()):
			print("Age should consist of numbers only, please enter again")
		elif((int(age) <  youngest) or (int(age) > oldest)):
			print("The employee should be between %d to %d years old" % (youngest, oldest))
		else:
			age_ok = True"""
		


	#Adding the employee to the empolyee file
	#with open("Employee.txt", "r+") as employees_file:
	info_string = "%s,%s,%s,%s\n" % (employee_id, employee_name, phone, age)		#The employee information
	add_employee(info_string, employee_id)
	"""exist = False		#A flag to check if the employee is already exist
	
	#Checking if the employee already exist. If so, prints an error to the user
	#and  changes "exist" value to True.
	for line in employees_file:
		if(employee_id == line[0:line.find(",")]):
			print("The employee is already registered, check if you entered the employee id correctly.")
			exist = True
			break
		
		#If the it is a new employee, add it to the end of the file 
		if(not exist):
			employees_file.write(info_string)"""
			

add_employee_manually()

#This function gets a file with new employees and adds them to the employee file, only if they don't already exist
def add_employee_from_file(new_employees):
	with open("new_employees.txt", "r") as to_read_file:		#Opening the given file

		for line in to_read_file:
			employee_info_list = line.split(",")			#Spliting each line into a list. Each cell holds a info piece
			employee_id = employee_info_list[0]
			if(is_id_valid(employee_id)):
				employee_name = employee_info_list[1]
				if(is_name_valid(employee_name)):
					phone = employee_info_list[2]
					if(is_phone_valid(phone)):
						age = employee_info_list[3]
						if(is_age_valid(age)):
							info_string = "%s,%s,%s,%s\n" % (employee_id, employee_name, phone, age)
							add_employee(info_string, employee_id)


file = open("new_employees.txt", "w")
file.close()
add_employee_from_file(file)


