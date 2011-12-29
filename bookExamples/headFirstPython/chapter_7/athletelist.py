class AthleteList(list):
	def __init__(self, name, dob=None, times=[]):
		list.__init__([])
		self.name = name
		self.dob = dob
		self.extend(times)
		
	def top_three_times(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])
		
	def add_time(self, time):
		self.times.append(time)
		
	def add_times(self, new_times):
		self.times.extend(new_times)
