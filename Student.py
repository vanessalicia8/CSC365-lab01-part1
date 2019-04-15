class Student:

	def __init__( self, StLastName, StFirstName, Grade, Classroom, Bus,
	    GPA, TLastName, TFirstName ):
		#constructor

		self.StLastName = StLastName
		self.StFirstName = StFirstName
		self.Grade = Grade
		self.Classroom = Classroom
		self.Bus = Bus
		self.GPA = GPA
		self.TLastName = TLastName
		self.TFirstName = TFirstName

	def __repr__( self ):
		return ( "Student: {!r}, {!r} {!r} {!r} {!r} {!r} {!r}, {!r} " ).format(
			self.StLastName, self.StFirstName, self.Grade, self.Classroom,
			self.Bus, self.GPA, self.TLastName, self.TFirstName )

	def to_String( self ):
		return "Student: " +  self.StLastName + ", " + self.StFirstName + ", " + self.Grade + ", " + self.Classroom + ", " + self.Bus + ", " + self.GPA + ", " + self.TLastName + ", " + self.TFirstName

	def get_member_var( self, c ):
		#takes a character representing the type of member variable to
		#return, returns that value

		member_vars = {'S': self.StLastName, 'T': self.TLastName, 
		    'G': self.Grade, 'B': self.Bus, 'A': self.GPA, 
		    'C': self.Classroom }

		if c in member_vars:
			return member_vars[c]
		else:
			return None



	