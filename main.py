"""This was written by Emily Yosub"""

from ValidationFunctions import *
from AttendanceLog import Attendance_Log
from EmployeesRegistry import Employees_Registry

EMPLOYEE_FILE = "Employees.txt"
ATTENDANCE_FILE = "Attendacce_Log.txt"
attendance_log = Attendance_Log(ATTENDANCE_FILE)		
employee_registry = Employees_Registry(EMPLOYEE_FILE)

#Checking if the employee file exist, if not creats one.
try:
	employee_file = open(EMPLOYEE_FILE, "r")
	employee_file.close()
except FileNotFoundError:
	employee_file = open(EMPLOYEE_FILE, "w")
	employee_file.close()

#Checking if the attendance file exist, if not creats one.
try:
	attendance_file = open(ATTENDANCE_FILE, "r")
	attendance_file.close()
except FileNotFoundError:
	attendance_file = open(ATTENDANCE_FILE, "w")
	attendance_file.close()

#The main menu

program_loop = False


def is_option_valid(digit, lowest, highest):
	"""
	This function checks if the option number that was selected is valid.

	Parameters:
	-----------

	digit: The option number that has been selected.

	lowest: The smallest option number that can be selected.

	highest: The largest option number that can be selected.
	"""
	check_loop = False
	if(not digit.isdigit()):
		print("ERROR: Option must be a digit")
	elif(not((int(digit) >= lowest) and (int(digit) <= highest))):
		print("Please choose a digit  between %d to %d" % (lowest, highest))
	else:
		check_loop = True
	
	return check_loop

#The program loop, to exit it the user will choose the "7.Exit" option in the main menu
while(not program_loop):
	print("1.Add employee")
	print("2.Delete employee")
	print("3.Mark attendence")
	print("4.Print report of a single employee")
	print("5.Print report of all active employees")
	print("6.Print late report")
	print("7.Exit")

	user_input = int(get_valid_input("Please choose one option from the ones above: ", is_option_valid, lowest = 1, highest = 7))
	
	#Based on the user's choice, directing the user to the right "screen"
	go_back = False
	if(user_input == 1):
		while(not go_back):
			print("1.Add employee manually")
			print("2.Add employee(s) from file")
			print("3.Back to main menu")
			add_choice = int(get_valid_input("Please choose one option from the ones above: ", is_option_valid, lowest = 1, highest = 3))
			
			if(add_choice == 1):
				employee_registry.add_employee_manually()
			elif(add_choice == 2):
				new_employee = input("Please enter a file path: ")
				employee_registry.add_employee_from_file(new_employee)
			else:
				go_back = True

	elif(user_input == 2):
		while(not go_back):
			print("1.Delete employee manually")
			print("2.Delete employee(s) from file")
			print("3.Back to main menu")
			delete_choice = int(get_valid_input("Please choose one option from the ones above: ", is_option_valid, lowest = 1, highest = 3))

			if(delete_choice == 1):
				employee_to_delete = get_valid_input("Please enter an id: ", is_id_valid, employee_file_path = EMPLOYEE_FILE)
				employee_registry.delete_employee_manually(employee_to_delete)
			elif(delete_choice == 2):
				employees_to_delete = input("Please enter a file path: ")
				employee_registry.delete_employee_from_file(employees_to_delete)
			else:
				go_back = True
	elif(user_input == 3):
		employee_id = get_valid_input("Please enter your employee id: ", is_id_valid, employee_file_path = EMPLOYEE_FILE)
		name = employee_registry.get_employee_name(employee_id)
		attendance_log.mark_attendance(employee_id, name)
	elif(user_input == 4):
		employee_id = get_valid_input("Please enter an employee id: ", is_id_valid, employee_file_path = EMPLOYEE_FILE)
		attendance_log.print_employee_report(employee_id)
	elif(user_input == 5):
		attendance_log.current_month_attendance()
	elif(user_input == 6):
		attendance_log.late_attendance_report()
	else:
		program_loop = True