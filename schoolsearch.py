from School import *
from Student import *

the_school = School()
the_school.populate_student_array( "students.txt" )
search_val = ""


def prompt():
   command = input("S[tudent]: <lastname> [B[us]]\nT[eacher]: <lastname>\nB[us]: <number>\nG[rade]: <number> [H[igh]|L[ow]]\nA[verage]: <number>\nI[nfo]\nQ[uit]\n")
   return command


def main():

   while ( True ):

      command = prompt()
      values = command.split()

      if ( values[0] == "Q" or values[0] == "Quit" ):
         break
      elif ( values[0] == "S" or values[0] == "Student" ):
         print( the_school.search( 'S', values[1] ) )

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


