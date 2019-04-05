from School import *
from Student import *

the_school = School()
the_school.populate_student_array( "students.txt" )
search_val = ""


def prompt():
   command = raw_input("S[tudent]: <lastname> [B[us]]\nT[eacher]: <lastname>\nB[us]: <number>\nG[rade]: <number> [H[igh]|L[ow]]\nA[verage]: <number>\nI[nfo]\nQ[uit]\n")
   return command


def main():
   command = prompt()
   if(command == "Q" or command == "Quit"):
      return
   while (command != "Q" or command != "Quit"):
      if ( command == "Q" or command == "Quit" ):
         break

      elif ( command == "S" or command == "Student" ):
         print( search_val )

      elif ( command == "T" or command == "Teacher" ):
         print( search_val )

      elif ( command == "B" or command == "Bus" ):
         print( search_val )

      elif ( command == "A" or command == "Average" ):
         print( search_val )

      elif ( command == "I" or command == "Info" ):
         print( search_val )

      command = prompt()


if __name__ == "__main__":
   main()


