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
         print( search_val )

      elif ( values[0] == "T" or values[0] == "Teacher" ):
         print( search_val )

      elif ( values[0] == "B" or values[0] == "Bus" ):
         print( search_val )

      elif ( values[0] == "A" or values[0] == "Average" ):
         print( search_val )

      elif ( values[0] == "I" or values[0] == "Info" ):
         print( search_val )


if __name__ == "__main__":
   main()


