#The main menu
print("1.Add employee")
print("2.Delete employee")
print("3.Mark attendence")
print("4.Print report of a single employee")
print("5.Print report of all active employees")
print("6.Print late report")
print("7.Exit")


program_loop = False
check_loop = False

#The program loop, to exit it the user will choose the "7.Exit" option in the main menu
while(not program_loop):
	#A check loop, making sure the user chooses an option that exists
	while(not check_loop):
		user_input = int(input("Please choose one option from the ones above:"))

		if(not user_input.isdigit()):
			print("Please enter a number")
		elif(not(user_input > 0) and (user_input < 8)):
			print("Please choose a number between 1 to 7")
		else:
			check_loop = True
	
	#Based on the user's choice, directing the user to the right "screen"
	if(user_input == 1):

	elif(user_input == 2):

	elif(user_input == 3):

	elif(user_input == 4):

	elif(user_input == 5):

	elif(user_input == 6):

	else:
