"""This was written by Emily Yosub"""
class Employee:

	def __init__(self, id, name, phone, age):
		self.id = id
		self.name = name
		self.phone = phone
		self.age = age

	def __str__(self):
		return "%s,%s,%s,%s\n" % (self.id, self.name, self.phone, self.age)	#The employee information



