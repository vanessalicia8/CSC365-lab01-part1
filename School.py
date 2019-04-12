#need a search function
from Student import *

class School:

	def __init__( self ):

		self.student_array = []
		self.teacher_array = []
         
         
	def populate_teacher_array( self, teacherFile ):
   #takes a file name. Reads in the teachers from the file and puts each
   #teacher into the teacher_array

	    try:
	    	with open( teacherFile ) as file:
	    		while ( True ):
	    			one_line = file.readline()

	    			if ( one_line == '' ):
	    				break
	    			else:
	    				teacher = self.create_teacher( one_line )
	    				self.teacher_array.append( teacher )
	    except:
	    	raise

	def populate_student_array( self, studentFile ):
	#takes a file name. Reads in the students from the file and puts each
	#student into the student_array

	    try:
	    	with open( studentFile ) as file:
	    		while ( True ):
	    			one_line = file.readline()

	    			if ( one_line == '' ):
	    				break
	    			else:
	    				student = self.create_student( one_line )
	    				self.student_array.append( student )
	    except:
	    	raise

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
		GPA = tokens[0:-1]

		new_student = Student( StLastName, StFirstName, Grade, Classroom,
		    Bus, GPA, "empty", "empty" )

		return new_student
         
	def create_teacher( self, lineFromFile ):
		#takes a single line from the teacher file as a string. Creates a
		#Teacher object using the information from the line. Returns the
		#teacher object

		tokens = lineFromFile.split( ',' )
		TLastName = tokens[0]
		TFirstName = tokens[1]
		Classroom = tokens[2]
		Classroom = tokens[0:-1]

		new_teacher = Teacher( TLastName, TFirstName, Classroom )

		return new_teacher

	def search( self, c, aString = None ):
		#takes a character representing the student member variable to search
		#by and a string representing the optional name or number field,
		#returns a list of all the students matching the search, if the
		#search yields no results, an empty line is printed
		
		students = []
		studentCount = 0.0
		allGPA = 0.0

		if(c == 'A'):
			for student in self.student_array:
				if ( student.get_member_var( 'G' ) == aString ):
					studentCount+= 1
					allGPA += float(student.GPA)
			if ( allGPA == 0 ):
				print()
				return
			else:
				print( "\nGrade: " + aString + "\nAverage GPA: " + str(round(allGPA/studentCount, 2)) + "\n" )
				return
		else:
			for student in self.student_array:
				if ( student.get_member_var( c ) == aString ):
					students.append( student )

		for student in students:
			if(c == "S"):
				print( "\nStudent: " + student.StLastName + ", " + student.StFirstName + ", " + student.Grade + ", " + student.Classroom + ", " + student.TLastName + ", " + student.TFirstName + "\n" )
			elif(c == "T"):
				print( "\nStudent: " + student.StLastName + ", " + student.StFirstName + "\n" )
			elif(c == "G"):
				print( "\nStudent: " + student.StLastName + ", " + student.StFirstName + "\n" )
			elif(c == "B"):
				print( "\nStudent: " + student.StLastName + ", " + student.StFirstName  + ", " + student.Grade + ", " + student.Classroom + "\n" )

		if len(students) == 0:
			print( "\n" )
		return


	def search_student_bus( self, aString = None):
		#takes a character representing the student member variable to search
		#by and a string representing the optional name or number field,
		#prints a list of all the students matching the search, if the
		#search yields no results, an empty line is printed
		
		students = []

		for student in self.student_array:
			if ( student.get_member_var( 'S' ) == aString ):
				students.append( student )

		for student in students:
			print( "\nStudent: " + student.StLastName + ", " + student.StFirstName + ", " + student.Bus + "\n" )

		if len(students) == 0:
			print( "\n" )
		return

	def grade_search( self, aString = None, oString = None ):
		#takes a string representing the grade number,
		#prints a list of all the students matching the search, if the
		#search yields no results, an empty line is printed
		
		students = []
		mystudent = None

		for student in self.student_array:
			if ( student.get_member_var( 'G' ) == aString ):
				students.append( student )

		mystudent = students[0]
		if(oString == "H" or oString == "High"):
			for student in students:
				if(student.GPA > mystudent.GPA):
					mystudent = student

			print( "\nStudent: " + mystudent.StLastName + ", " + mystudent.StFirstName + ", " + mystudent.GPA + ", " +\
				mystudent.TLastName + ", " + mystudent.TFirstName + ", " + mystudent.Bus + "\n" )
			
			#print( "\n" + mystudent.to_String() + "\n" )

		elif(oString == "L" or oString == "Low"):
			for student in students:
				if(student.GPA < mystudent.GPA):
					mystudent = student

			print( "\nStudent: " + mystudent.StLastName + ", " + mystudent.StFirstName + ", " + mystudent.GPA + ", " +\
				mystudent.TLastName + ", " + mystudent.TFirstName + ", " + mystudent.Bus + "\n" )
			
			#print( "\n" + mystudent.to_String() + "\n" )

		if len(students) == 0:
			print( "\n" )
		return

	def grade_info( self ):
		#computes the total number of students in each grade
      #prints result
		
		kinder = first = second = third = fourth = fifth = sixth = 0


		for student in self.student_array:
			if ( student.get_member_var( 'G' ) == "0" ):
				kinder += 1
			elif ( student.get_member_var( 'G' ) == "1" ):
				first += 1
			elif ( student.get_member_var( 'G' ) == "2" ):
				second += 1
			elif ( student.get_member_var( 'G' ) == "3" ):
				third += 1
			elif ( student.get_member_var( 'G' ) == "4" ):
				fourth += 1
			elif ( student.get_member_var( 'G' ) == "5" ):
				fifth += 1
			elif ( student.get_member_var( 'G' ) == "6" ):
				sixth += 1

		print( "\nGrade 0: " + str(kinder) )
		print( "\nGrade 1: " + str(first) )
		print( "\nGrade 2: " + str(second) )
		print( "\nGrade 3: " + str(third) )
		print( "\nGrade 4: " + str(fourth) )
		print( "\nGrade 5: " + str(fifth) )
		print( "\nGrade 6: " + str(sixth) + "\n" )
		return



