#need a search function
from Student import *

class School:

	def __init__( self ):

		self.student_array = []

	def populate_student_array( self, studentFile ):
	#takes a file name. Reads in the students from the file and puts each
	#student into the students_array

	    with open( studentFile ) as file:

	    	while ( True ):

	    		one_line = file.readline()

	    		if ( one_line == '' ):
	    			break
	    		else:
	    			student = self.create_student( one_line )

	    			self.student_array.append( student )

	def create_student( self, lineFromFile ):
		#takes a single line from the student file as a string. Creates a
		#Student object using the information from the line. Returns the 
		#student object

		tokens = lineFromFile.split( ',' )
		StLastName = tokens[0]
		StFirstName = tokens[1]
		Grade = tokens[2]
		Classroom = tokens[3]
		Bus = tokens[4]
		GPA = tokens[5]
		TLastName = tokens[6]
		TFirstName = tokens[7]
		TFirstName = TFirstName[0:]

		new_student = Student( StLastName, StFirstName, Grade, Classroom,
		    Bus, GPA, TLastName, TFirstName )

		return new_student

	# def get_member_val( self, member_val ):
	# 	#

	# def search( self, string, member_var ):
	# 	#
	# 	for student in self.student_array:








	#search functions go here