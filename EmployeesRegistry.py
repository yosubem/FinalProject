"""This was written by Emily Yosub"""
import os
from ValidationFunctions import *
from Employee import Employee


class Employees_Registry():
	def __init__(self, employees_file):
		self.employees_file = employees_file

	def get_employee_name(self, id):
		"""
		This function gets an id and finds the name attached to it.

		Parameters:
		-----------

		id: The id of the employee whom we need their name.
		"""
		#Searching for the id given and when found copy the name of the employee
		with open(self.employees_file, "r") as employee_file:
			for line in employee_file:
				first_comma_index = line.find(",")
				#print("Id: " +  line[0:first_comma_index])
				if(line[0:first_comma_index] == id):
					employee_name = line[first_comma_index + 1 :line.find(",", first_comma_index + 1)]
					#print("Name: " + employee_name)
					#print("In get name if")
					return employee_name

	#region Add Functions
	def add_employee(self, new_employee):
		"""
		This function adds an employee.

		Parameters:
		-----------

		new_employee: The employees to add.
		"""
		with open(self.employees_file, "a") as employees_file:
			employees_file.write("%s" % new_employee)

	def add_employee_manually(self):
		"""
		This function lets the user add an employee manually.
		"""

		employee_id = get_valid_input("Please enter an employee's id: ", is_id_valid, employee_file_path = self.employees_file, is_in_file_ok = False)
		
		employee_name = get_valid_input("And now enter the employee's name: ", is_name_valid)

		phone = get_valid_input("Their phone number: ", is_phone_valid)			

		age = get_valid_input("How old are they? ", is_age_valid)
			
		new_employee = Employee(employee_id, employee_name, phone, age)
		self.add_employee(new_employee)	#Adding the employee to the empolyee file
		print('\x1b[6;30;42m' + "Employee was added." + '\x1b[0m')

	def add_employee_from_file(self, new_employees):
		"""
		This function gets a file with new employee(s) and adds them to the employee file, only if they don't already exists.

		Parameters:
		-----------

		new_employees: The file from which we take the new employees.
		"""
		try:
			with open(new_employees, "r") as to_read_file:		#Opening the given file
				for line in to_read_file:
					employee_info_list = line.split(",")			#Spliting each line into a list. Each cell holds a info piece
					employee_id = employee_info_list[0]
					if(is_id_valid(employee_id, self.employees_file, is_in_file_ok=False)):
						employee_name = employee_info_list[1]
						if(is_name_valid(employee_name)):
							phone = employee_info_list[2]
							if(is_phone_valid(phone)):
								age = employee_info_list[3]
								if(is_age_valid(age)):
									age = int(age)
									new_employee = Employee(employee_id, employee_name, phone, age)
									self.add_employee("%s" % new_employee)
									print('\x1b[6;30;42m' + "Employees were added." + '\x1b[0m')
		except FileNotFoundError:
			print('\x1b[6;30;42m' + "There is no file by that name." + '\x1b[0m')
		except Exception as e:
			print(type(e))
			print(e)
		

	#endregion

	#region Delete Functions
	def delete_employee(self, id_list):
		"""
		This function deletes an employee
		
		Parameters:
		-----------

		id_list: A list of employee(s) to delete.
		"""
		#Becuse python doesn't have a delete function, I had to copy each line that
		#does not contain the given id(cheking if it exists in the id_list), 
		# to a new file. Then delete the current "Employee" file and change the name 
		# of the new one to "Employee".
		with open(self.employees_file,"r") as employee_file, open("new_employee.txt","w") as new_employee_file:
			for line in employee_file:
				if(not(line[0:line.find(",")] in id_list)):
					new_employee_file.write(line)

		
		os.remove(self.employees_file)
		os.rename("new_employee.txt", self.employees_file)

	def delete_employee_manually(self, employee_to_delete):
		"""
		This function lets the user delete an employee manually.

		Parameters:
		-----------

		employee_to_delete: The id of the employee to delete.
		"""
		#id = get_valid_input("Please enter an employee's id: ", is_id_valid, employee_file_path = self.employees_file, to_delete = True)
		self.delete_employee(employee_to_delete)
		print('\x1b[6;30;42m' + "Employe was removed." + '\x1b[0m')

	def delete_employee_from_file(self,employees_to_delete):
		"""
		This function gets a file with employee(s) to delete and deletes them from the employee file.

		Parameters:
		-----------
		
		employees_to_delete: The file from which we take the ids of the employees we need to delete.
		"""
		id_list = []
		try:
			with open(employees_to_delete, "r") as to_delete:
				for line in to_delete:
					employee_id = line.split(",", 1)		#Getting the id from each line
					#print(employee_id)
					id_list.append(employee_id[0])
			self.delete_employee(id_list)
			print('\x1b[6;30;42m' + "Employees were removed." + '\x1b[0m')

		except FileNotFoundError:
			print('\x1b[6;30;42m' + "There is no file by that name." + '\x1b[0m')

		
	#endregion