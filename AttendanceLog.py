"""This was written by Emily Yosub"""
from ValidationFunctions import *
from datetime import datetime
import time

class Attendance_Log():
	def __init__(self, attendance_file):
		self.attendance_report = attendance_file

	def mark_attendance(self, id, name):
		"""
		This function lets an employee to mark their attendance

		Parameters:
		-----------
		
		id: The id of the employee marking his attendance.

		name: The name of the employee marking his attendance.
		"""
		#Registering the employee attendance
		with open(self.attendance_report,"a") as attendance_file:
			#Keeping the currnet time and date
			now = datetime.now()
			#Creating a string to keep the id, date and time
			attendance_info_string = "%s,%s,%s/%s/%s %s:%s:%s\n" % (id, name, now.day, now.month, now.year, now.hour, now.minute, now.second)
			attendance_file.write(attendance_info_string)
		print('\x1b[6;30;42m' + "Attendance was registered" + '\x1b[0m')
	
	def print_employee_report(self, employee_id):
		"""
		This function return all the entries of his attendance.

		Parameters:
		-----------

		employee_id: The id of the employee which report we want to print
		"""
		with open(self.attendance_report, "r") as attendance_file:
			for line in attendance_file:
				if(employee_id == line[0:line.find(",")]):
					print(line[line.find(",") + 1:])

	def current_month_attendance(self):
		"""
		This function prints an attendance report for all active employee in the last month.
		"""
		current_month = datetime.now().month		#Keeps the current month
		current_year = datetime.now().year			#Keeps the current year

		with open(self.attendance_report,"r") as attendance_file:
			for line in attendance_file:
				day_month_seperator = line.find("/")
				month_year_seperator = line.find("/", day_month_seperator + 1)
				month_in_line = int(line[day_month_seperator + 1 : month_year_seperator])	#Finds the month in the line
				year_in_line = int(line[month_year_seperator + 1 : line.find(" ", month_year_seperator)])	#Finds the year in the line
				#print("Month in line : %d" % month_in_line)
				#print("Year in line: %d" % year_in_line)
				#Checks if the attendance is in the right month and the right year,
				#if so prints the line
				if((month_in_line == current_month) and (year_in_line == current_year)):
					print(line)
					#print("In if")
				else:
					print("There are no active employees this month.")

	def late_attendance_report(self):
		"""
		This function prints an attendance report for all employees who were late (came after 9:30).
		"""
		late_time = 570			#9:30 in minutes is 570
		hour_to_minute = 60		#There are 60 minutes in an hour
		with open(self.attendance_report, "r") as attendance_file:
			for line in attendance_file:
				first_colon_index = line.find(":")
				first_space_index = line.find(" ")
				hour_in_line = line[first_space_index + 1:first_colon_index]	#Finds the hour in line
				minute_in_line = line[first_colon_index + 1:first_colon_index + 3]	#Finds the minute in the line
				
				#Calculationg the attendance time in minutes
				attendance_time = (int(hour_in_line) * hour_to_minute) + int(minute_in_line)
				
				#Checks if the employee arrived after 9:30
				if(attendance_time > late_time):
					print(line)