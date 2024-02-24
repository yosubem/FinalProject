"""This was written by Emily Yosub"""

def is_id_valid(id, employee_file_path, is_in_file_ok = True):
	"""
	This function checks if the given id is valid
	
	Parameters:
	-----------
	id : Employee id

	employee_file_path : The Employees file

	is_in_file_ok : Is it ok that the id is in file. True by defult for deletion and marking attendance.
	"""
	id_ok = False
	id_len = 9

	if(not id.isdigit()):
		print("Employee id should consist of numbers only")
	elif(not(len(id) == id_len)):
		print("Employee id should have %d numbers" % (id_len))
	elif(is_id_exist(id,employee_file_path)):
		if(not is_in_file_ok):
			print("The employee is already registered, check if you entered the employee id correctly")
		else:
			id_ok = True
	else:
		if(is_in_file_ok):
			print("The id was not found.")
		else:
			id_ok = True
	
	return id_ok

def is_name_valid(name):
	"""
	This function checks if the given name is valid

	Parameters:
	-----------

	name: The employee name
	"""
	name_ok = False

	if(not name.isalpha()):
		print("Names should consist of letters only, please enter again")
	else:
		name_ok = True
	
	return name_ok

def is_phone_valid(phone):
	"""
	This function checks if the given phone is valid

	Parameters:
	-----------
	phone: The employee phone
	"""
	phone_ok = False
	phone_len = 10

	if(not phone.isdigit()):
		print("Phone number should consist of numbers only, please enter again")
	elif(not(len(phone) == phone_len)):
		print("Phone number should have %d numbers, please try again" % (phone_len))
	else:
		phone_ok = True
	
	return phone_ok

def is_age_valid(age):
	"""
	This function checks if the given age is valid

	Parameters:
	-----------

	age: The employee age
	"""
	age_ok = False
	youngest = 15		#The youngest employee can be
	oldest = 80			#The oldest employee can be

	try:
		age = int(age)
	except ValueError:
		print("Age should consist of numbers only, please enter again")
	except Exception as e:
		print(type(e))
		print(e)
	else:
		"""if(not age.isdigit()):
			print("Age should consist of numbers only, please enter again")
		elif((int(age) <  youngest) or (int(age) > oldest)):
			print("The employee should be between %d to %d years old" % (youngest, oldest))
		else:
			age_ok = True"""
		if((age <  youngest) or (age > oldest)):
			print("The employee should be between %d to %d years old" % (youngest, oldest))
		else:
			age_ok = True
		

	return age_ok

def is_id_exist(id, employee_file_path):
	"""
	This function check if the id already exist in the Employees file

	Parameters:
	-----------

	id: Id to check

	employee_file_path: The Employees file
	"""
	exist = False		#A flag to check if the employee already exist
	try:
		with open(employee_file_path, "r") as employee_file:
			#Checking if the employee already exist. If so, prints an error to the user
			#and changes "exist" value to True.
			for line in employee_file:
				if(id == line[0:line.find(",")]):
					exist = True
					break
		
		return exist
	except FileNotFoundError:
		print("No file was found.")

def get_valid_input(input_prompt, validation_func, **kwargs):
	"""
	This function asks for input and checks if it is valid using the validiation function.

	Parameters:
	----------

	input_prompt: What to print to the user when asking for input.

	validation_func: Which function to use when checking input.

	**kwargs: Here are any variables the validation function may need. 
	"""
	is_valid = False

	while(not is_valid):
		user_input = input(input_prompt)
		is_valid = validation_func(user_input, **kwargs)
	
	return user_input





