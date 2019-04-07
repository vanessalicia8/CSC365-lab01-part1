from School import *
from Student import *

the_school = School()
the_school.populate_student_array( "students2.txt" )
search_val = ""


def prompt():
   command = input("S[tudent]: <lastname> [B[us]]\nT[eacher]: <lastname>\nB[us]: <number>\nG[rade]: <number> [H[igh]|L[ow]]\nA[verage]: <number>\nI[nfo]\nQ[uit]\n")
   return command

def print_info( studentList, optional = None ):
   #takes a list of students that met the search criteria and prints the
   #requested information

   for student in studentList:
      if ( optional == None ):
         print( student.StLastName, ",", student.StFirstName, ",", 
            student.Grade, ",", student.Classroom, ",", 
            student.TLastName, ",", student.TFirstName )

def handle_options( optionalArg = None ):
   #Takes an optional argument that was provided by the user and returns
   #a character representing that option, for use with other functions 
   c = None

   if ( optionalArg == 'B' or optionalArg == 'Bus' ):
      c = 'B'
   elif ( optionalArg == 'H' or optionalArg == 'High' ):
      c == 'H'
   elif ( optionalArg == 'L' or optionalArg == 'Low' ):
      c == 'L'

   return c

def main():

   while ( True ):

      command = prompt()
      values = command.split()
      numArgs = len( values )

      if ( values[0] == "Q" or values[0] == "Quit" ):
         break
      elif ( values[0] == "S" or values[0] == "Student" ):

         if ( numArgs == 3 ):
            c = handle_options( values[-1] )

         students = the_school.search( 'S', values[1] )
         print_info( students )

      elif ( values[0] == "T" or values[0] == "Teacher" ):
         print( the_school.search( 'T', values[1] ) )

      elif ( values[0] == "B" or values[0] == "Bus" ):
         print( the_school.search( 'B', values[1] ) )

      elif ( values[0] == "A" or values[0] == "Average" ):
         print( the_school.search( 'A', values[1] ) )

      elif ( values[0] == "I" or values[0] == "Info" ):
         print( search_val )


if __name__ == "__main__":
   main()


