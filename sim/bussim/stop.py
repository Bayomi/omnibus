import numpy as np
from random import randint
from temp import TimeBuilder as tb
from person import Person

"""
Process the data using the pre_processing.py file parameters.
@param {String}
@return {Array} 
"""
def peopleFuncStandard(self, timeAtStopIdeal, timeAtStopReal, date):
	self.people = []
	for i in range(0,randint(0,14)):
		newPerson = Person(1,timeAtStopIdeal,timeAtStopReal)
		self.people.append(newPerson)
	return self.people

class Stop:

	def __init__(self, place, peopleFunc=peopleFuncStandard):
		self.name = place['name']
		self.timeToNext = place['timeToNext']
		self.id = self.getRandomId()
		self.people = []
		self.peopleFunc = peopleFunc
		#self.distanceToNext = place.distance

	"""
	Process the data using the pre_processing.py file parameters.
	@param 
	@return
	"""
	def check(self, parameters, date):
		idealTimes = parameters['idealTimes']
		arrivalTimes = parameters['arrivalTimes']
		ids = parameters['ids']
		startTime = tb(parameters['startTime'])

		diffIdeal = self.find(ids, idealTimes)
		diffReal = self.find(ids, arrivalTimes)

		diff = diffReal - diffIdeal

		timeAtStopIdeal = startTime.addMinutes(diffIdeal).getStr()
		timeAtStopReal = startTime.addMinutes(diffReal).getStr()

		"""
		print timeAtStopIdeal
		print timeAtStopReal
		print ''
		"""

		self.people = self.createPeople(timeAtStopIdeal, timeAtStopReal, date)
		reports = self.getReports(date)

		return reports
		#print timeAtStopIdeal, timeAtStopReal, diff, self.getReports(outfile)

	"""
	Process the data using the pre_processing.py file parameters.
	@param 
	@return
	"""
	def getRandomId(self):

		idRef = ""
		for i in range(0,9):
			idRef = idRef + str(randint(0,9))
		
		return idRef

	"""
	Process the data using the pre_processing.py file parameters.
	@param 
	@return
	"""
	def find(self, ids, arrivalTimes):
		indexRef = ids.index(self.id)
		return self.getCumulativeTime(arrivalTimes, indexRef)

	"""
	Process the data using the pre_processing.py file parameters.
	@param {String}
	@return {Array} 
	"""
	def getCumulativeTime(self, array, index):
		if index == 0:
			return array[0]
		else:
			return array[index] + self.getCumulativeTime(array, index-1)


	"""
	Process the data using the pre_processing.py file parameters.
	@param {String}
	@return {Array} 
	"""
	def createPeople(self, timeAtStopIdeal, timeAtStopReal, date):
		return self.peopleFunc(self, timeAtStopIdeal, timeAtStopReal, date)

	def getPeople(self):
		return len(self.people)

	"""
	Process the data using the pre_processing.py file parameters.
	@param {String}
	@return {Array} 
	"""

	def getReports(self, date):
		reports = []

		for person in self.people:
			reports.append(person.report(date))

		return reports


	"""
	Process the data using the pre_processing.py file parameters.
	@param {String}
	@return {Array} 
	"""
	def predict():
		print 'oi'

	"""
	Process the data using the pre_processing.py file parameters.
	@param {String}
	@return {Array} 
	"""
	def pprint(self):
		print 'olar'