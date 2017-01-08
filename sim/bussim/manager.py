import math
import numpy as np
from bus import Bus
from stop import Stop
import json
from temp import TimeBuilder as tb
from random import randint
from person import Person

class Manager:

	def __init__(self, bus):
		self.bus = bus

	"""
	Represents the process of a full cycle in a determined path.
	@param {Object} bus - The bus used as reference for the cycle.
	@param {String} startTime - The time it started the cycle.
	@return {Array} the two table objects
	"""
	def run(self, dateRef):
		#get the times the bus will arrive in each stop and the parameters for the stop prediction
		parameters, timeInfo = self.bus.run(dateRef['startTime'])
		predictInfo = []
		#for each stop, predict what people will report (according to the time of arrival)
		for stop in self.bus.stops:
			info = stop.check(parameters, dateRef['full'])
			for report in info:
				predictInfo.append(report)

		#reports table
		reports = self.createReportsTable(predictInfo)

		#bus times table
		busTimes = self.createBusTimeTable(parameters, dateRef)

	"""
	Process the data using the schedule provide and generate a table object.
	@param {Object} trainValuesFile - Time table information
	@return {Object} the table object
	"""
	def createReportsTable(self, data):
		
		reports = {}
		reports['reports'] = data
		self.jsonify(reports, 'reports.json')


	"""
	Process the data using the schedule provide and generate a table object.
	@param {Object} trainValuesFile - Time table information
	@return {Object} the table object
	"""
	def createBusTimeTable(self, data, dateRef):

		info = {}
		info['idealTimes'] = self.addStartTimeToArray(data['idealTimes'], data['startTime'])
		info['arrivalTimes'] = self.addStartTimeToArray(data['arrivalTimes'], data['startTime'])
		info['order'] = data['order']
		info['ids'] = data ['ids']

		timeRef = {}
		timeRef[data['startTime']] = info

		busTimes = {}
		busTimes[dateRef['full']] = timeRef

		self.jsonify(busTimes, 'times.json')

	"""
	Process the data using the schedule provide and generate a table object.
	@param {Object} trainValuesFile - Time table information
	@return {Object} the table object
	"""
	def addStartTimeToArray(self, array, startTime):
		new = []
		acc = 0
		for el in array:
			acc = acc + el
			el = tb(startTime).addMinutes(acc).getStr()
			new.append(el)

		return new

	"""
	Process the data using the schedule provide and generate a table object.
	@param {Object} trainValuesFile - Time table information
	@return {Object} the table object
	"""
	def jsonify(self, data, fileName):
		with open(fileName, 'w') as outfileJson:
			json.dump(data, outfileJson, indent=4, sort_keys=True, separators=(',', ':'))
		
######## PARAMETERS #########


defaultPath = np.array([{'name': 'Rodoviaria', 'timeToNext':  10},\
						{'name': 'N1 LESTE', 'timeToNext':  7},\
						{'name': 'L2 NORTE 03', 'timeToNext':  6},\
						{'name': 'L2 NORTE 04', 'timeToNext':  5},\
						{'name': 'L2 NORTE 06', 'timeToNext':  3},\
						{'name': 'L2 NORTE 07', 'timeToNext':  5},\
						{'name': 'UnB - Entrada', 'timeToNext':  13},\
						{'name': 'UnB - ICC SUL', 'timeToNext':  11},\
						{'name': 'UnB - ICC NORTE', 'timeToNext':  16},\
						{'name': 'L2 NORTE 07', 'timeToNext':  19},\
						{'name': 'L2 NORTE 06', 'timeToNext':  13},\
						{'name': 'L2 NORTE 03', 'timeToNext':  8},\
						{'name': 'L2 NORTE 02', 'timeToNext':  7}])

def getTime(distance):
	return distance + randint(-3,4)

def runFunc(self, startTime):
	parameters = {}
	parameters['startTime'] = startTime
	order = []
	arrivalTimes = []
	ids = []
	for stop in self.stops:
		order.append(stop.name)
		arrivalTimes.append(getTime(stop.timeToNext))
		ids.append(stop.id)

	parameters['order'] = order
	parameters['arrivalTimes'] = arrivalTimes
	parameters['ids'] = ids
	parameters['idealTimes'] = self.idealTimes

	return parameters, arrivalTimes

def reportFunc(self, date):
	log = {}
	log['id'] = self.id
	log['date'] = date

	report = self.estimateReport(self.style, self.timeOfReport, date)

	log['reportedTimeString'] = report['time']
	log['reportedTimeNum'] = tb(report['time']).toSec()
	#log['diff'] = report['diff']

	if self.style == 1:
		log['message'] = 'late'
		log['isLate'] = True

	if self.style == 2:
		log['message'] = 'arrived'
		log['isLate'] = False

	info = {}
	info[self.id] = log

	print info

	return info

def peopleFunc(self, timeAtStopIdeal, timeAtStopReal, date):
	self.people = []

	#parameters
	ideal = tb(timeAtStopIdeal).toSec()
	real = tb(timeAtStopReal).toSec()
	marginLeft = tb(timeAtStopIdeal).removeMinutes(7).getStr()
	marginRight = tb(timeAtStopIdeal).addMinutes(7).getStr()
	difference = real - ideal
	lam = 10
	
	#poisson
	tp = 8
	tv = min(max(0, 8 + difference/60), 14)
	poissonN = np.random.poisson(lam, 1)[0]
	n_ref = poissonN/(tv+1) + 1
	peopleTimeDivision = [n_ref]*(tv+1)

	while sum(peopleTimeDivision)>poissonN:
		rand = randint(0, tv)
		if peopleTimeDivision[rand]>0:
			peopleTimeDivision[rand] = peopleTimeDivision[rand] - 1

	while len(peopleTimeDivision)<15:
		peopleTimeDivision.append(0)

	print ''
	print 'Horario ideal: ' + timeAtStopIdeal
	print 'Horario real: ' + timeAtStopReal
	print '-'

	if tp>tv:
		for i in range(0, tv):
			if i<=tv:
				for k in range(0, peopleTimeDivision[i]):
					timeOfReport = tb(marginLeft).addMinutes(i).getStr()
					newPerson = Person(2,timeOfReport,reportFunc)
					self.people.append(newPerson)

	if tp<=tv:
		for i in range(0, tv):
			if i<=tp:
				for k in range(0, peopleTimeDivision[i]):
					timeOfReport = tb(marginLeft).addMinutes(i).getStr()
					newPerson = Person(1,timeOfReport,reportFunc)
					self.people.append(newPerson)
			if i>tp:
				for k in range(0, peopleTimeDivision[i]):
					timeOfReport = tb(marginLeft).addMinutes(i).getStr()
					newPerson = Person(2,timeOfReport,reportFunc)
					self.people.append(newPerson)
	print ""
	return self.people


bus110 = Bus(defaultPath, peopleFunc, runFunc)
manager = Manager(bus110)

dateRef = {}
dateRef['startTime'] = '12:00'
dateRef['full'] = '12-08-2016'

manager.run(dateRef)




