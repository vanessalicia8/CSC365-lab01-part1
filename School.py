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

	def search( self, c, aString = None ):
		#takes a character representing the student member variable to search
		#by and a string representing the optional name or number field,
		#returns a list of all the students matching the search, if the
		#search yields no results an empty list is returned
		
		students = []

		for student in self.student_array:
			if ( student.get_member_var( c ) == aString ):
				students.append( student )

		return students