"""Add employee manually:
	*The user can choose to add new employee to the Employees file. 
		Make sure all data is supplied.
	*Give an error messege to the user if something is wrong
"""

def add_employee_manually(self, employee_id, employee_name, phone, age):
    

    id_ok = False
    name_ok = False
    phone_ok = False
    age_ok = False

    id_len = 9          #The length of the id

    phone_num_len = 10  #The length of the phone number

    youngest_age = 15     #The younget employee can be
    oldest_age = 120    #The oldest employee can be


    while(not id_ok):
        employee_id = input("Please enter an employee's id: ")
        if(not employee_id == id_len):
            print("Employee id should be %d numbers, please enter it correctly." % (id_len))
        else:
            id_ok = True
    
    while(not name_ok):
        employee_name = input("And now enter the employee's name: ")
        if(not employee_name.isalpha()):
            print("Name should consist of only letters, please enter it correctly.")
        else:
            name_ok = True
    
    while(not phone_ok):
        phone = input("Their phone number: ")
        if(not phone.isdigit()):
            print("Phone number should consist of only numbers, please enter it correctly.")
        elif(not phone == phone_num_len):
            print("The phone number should have %d numbers, please enter it correctly." % (phone_num_len))
        else:
            phone_ok = True

    while(not age_ok):
        age = input("How old are they? ")
        if(not age.isdigit):
            print("Age should consist of only numbers, please enter it correctly.")
        elif(not youngest_age < age < oldest_age):
            print("The employee should be %d to %d old to work, plese enter it again." % (youngest_age, oldest_age))
        else:
            age_ok = True
	

