from School import *
from Student import *

the_school = School()
the_school.populate_student_array( "students.txt" )
search_val = ""

while ( True ):

	userInput = input( "Enter search command: " )

	if ( userInput == "Q:" or userInput == "Quit:" ):
		break

	elif ( userInput == "S:" or userInput == "Student:" ):
		search_val = input()
		print( search_val )

	elif ( userInput == "T:" or userInput == "Teacher:" ):
		search_val = input()
		print( search_val )

	elif ( userInput == "B:" or userInput == "Bus:" ):
		search_val = input()
		print( search_val )

	elif ( userInput == "A:" or userInput == "Average:" ):
		search_val = input()
		print( search_val )

	elif ( userInput == "I" or userInput == "Info" ):
		search_val = input()
		print( search_val )
