class Teacher:

	def __init__( self, TLastName, TFirstName, Classroom ):

	    self.TLastName = TLastName
	    self.TFirstName = TFirstName
	    self.Classroom = Classroom
	    self.Grade = None

	def __repr__( self ):

		return ( "Teacher: {!r}, {!r}, {!r} ".format( self.TLastName,
			self.TFirstName, self.Classroom ) )

	def getLastName( self ):
		return self.TLastName

	def getFirstName( self ):
		return self.TFirstName

	def getClassroom( self ):
		return self.Classroom

	def getGrade( self ):
		return self.Grade

	def to_String( self ):
		return ( "Teacher: " + self.TLastName + ", " + 
					self.TFirstName )