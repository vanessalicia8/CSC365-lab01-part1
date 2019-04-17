from School import *
from Student import *

def prompt():
   command = input("S[tudent]: <lastname> [B[us]]\nT[eacher]: <lastname>\nC[lassroom]: <number> [T[eacher]]\nB[us]: <number>\nG[rade]: <number> [H[igh]|L[ow]]\nA[verage]: <number>\nI[nfo]\nE[nrollment]\nQ[uit]\n")
   return command

def main():

   the_school = School()
   try:
      the_school.populate_teacher_array( "teachers.txt" )
   except( FileNotFoundError ):
      print( "File was not found.\n" )
      return
   try:
       the_school.populate_student_array( "list.txt" )
   except( FileNotFoundError ):
       print( "File was not found.\n" )
       return

   the_school.add_more_teacher_info()

   search_val = ""

   while ( True ):

      command = prompt()
      values = command.split()

      #Quit
      if ( values[0] == "Q" or values[0] == "Quit" ):
         break
      #Student
      elif ( values[0] == "S" or values[0] == "Student" ):
         if (len(values) == 3):
            if(values[2] == "B" or values[2] == "Bus"):
               the_school.search_student_bus(values[1])
            else:
               print( "\n" + values[2] + " is not a valid command\n" )
         else:
            the_school.search( 'S', values[1] )
      #Teacher
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
            elif ( values[2] == "T" or values[2] == "Teacher" ):
               the_school.teacher_search( "G", values[1] )
            else:
               print( "\n" + values[2] + " is not a valid command\n" )
         else:
            the_school.search( 'G', values[1] )
      #Average
      elif ( values[0] == "A" or values[0] == "Average" ):
         the_school.search( 'A', values[1] )
      #Info
      elif ( values[0] == "I" or values[0] == "Info" ):
         the_school.grade_info()
      #Classroom
      elif ( values[0] == "C" or values[0] == "Classroom" ):
         if ( len( values ) == 3 and ( values[2] == "T" or 
            values[2] == "Teacher" ) ):

            the_school.teacher_search( 'C', values[1] )
         else:
            the_school.search( 'C', values[1] )
      #Enrollment
      elif ( values[0] == "E" or values[0] == "Enrollment" ):
         the_school.print_enrollment()


if __name__ == "__main__":
   main()


