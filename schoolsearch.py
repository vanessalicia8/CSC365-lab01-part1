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
<<<<<<< HEAD
      #Quit
=======
      numArgs = len( values )

>>>>>>> 4af2b517e3da6a9a38ce5449cb178bb319ea6cbf
      if ( values[0] == "Q" or values[0] == "Quit" ):
         break
      #Student
      elif ( values[0] == "S" or values[0] == "Student" ):
<<<<<<< HEAD
         if (len(values) == 3):
            if(values[2] == "B" or values[2] == "Bus"):
               the_school.search_student_bus(values[1])
            else:
               print "\n" + values[2] + " is not a valid command\n"
         else:
            the_school.search( 'S', values[1] )
      #Teacher
=======

         if ( numArgs == 3 ):
            c = handle_options( values[-1] )

         students = the_school.search( 'S', values[1] )
         print_info( students )

>>>>>>> 4af2b517e3da6a9a38ce5449cb178bb319ea6cbf
      elif ( values[0] == "T" or values[0] == "Teacher" ):
         the_school.search( 'T', values[1] )
      #Bus
      elif ( values[0] == "B" or values[0] == "Bus" ):
         the_school.search( 'B', values[1] )
      #Grade
      elif ( values[0] == "G" or values[0] == "Grade" ):
         if (len(values) == 3):
            if(values[2] == "H" or values[2] == "L" or values[2] == "High" or values[2] == "Low"):
               the_school.grade_search( values[1], values[2] )
            else:
               print "\n" + values[2] + " is not a valid command\n"
         else:
            the_school.search( 'G', values[1] )
      #Average
      elif ( values[0] == "A" or values[0] == "Average" ):
         the_school.search( 'A', values[1] )
      #Info
      elif ( values[0] == "I" or values[0] == "Info" ):
         the_school.grade_info()


if __name__ == "__main__":
   main()


