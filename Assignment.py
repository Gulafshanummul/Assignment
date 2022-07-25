class Member():
	def __init__(self,full_name):
		self.full_name = full_name
	def __str__(self):
		return "{}".format(self.full_name)
	def intro(self,full_name):
		self.full_name=full_name
		print('Hi my name is '+self.full_name)

class Attendees(Member):
	def __init__(self,full_name,reason):
		super().__init__(full_name)
		self.occupation = 'student'
		self.reason= reason

class Instructor(Member):
	def __init__(self,full_name,bio,skills=[]):
		super().__init__(full_name)
		self.occupation = 'instructor'
		self.bio = bio
		self.skills = skills
	def add_skill(self,skill):
		self.skills.append(skill)
class Workshop():
	def __init__(self,date,subject,instructors=[],attendees=[]):
		self.date = date
		self.subject = subject
		self.instructors= instructors
		self.attendees = attendees
	def add_participant(self,member):
		if member.occupation == 'Attendees':
			self.attendees.append(member.full_name)
			
		elif member.occupation == 'Instructor':
			self.instructors.append(member.full_name)
	def print_details(self):
		return print("Date: {}, Subject:{}, Instructors:{}, Attendesss:{}".format(self.date,self.subject,self.instructors,self.attendees))
	

workshop = Workshop("25/07/2022", "PythonCon")
gul=Attendees("Gul Afshan", "I am trying to learn python language and need some help")
anjana =Attendees("Anjana", "I am really excited about learning python!")
Neelu = Instructor("Neelu ", "I want to help people learn coding.")
Neelu.add_skill("C")
Neelu.add_skill("C++")
su = Instructor("Suvil", "I have been programming for 5 years in Python and want to spread the love")
su.add_skill("Python")
workshop.add_participant(gul)
workshop.add_participant(anjana)
workshop.add_participant(Neelu)
workshop.add_participant(su)
workshop.print_details()

