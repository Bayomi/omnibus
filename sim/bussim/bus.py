import numpy as np
import pylab
from stop import Stop
from random import randint

"""
Action
@param 
@return 
"""
def runStandard(self, startTime):
	parameters = {}
	parameters['startTime'] = startTime
	order = []
	arrivalTimes = []
	ids = []
	for stop in self.stops:
		order.append(stop.name)
		arrivalTimes.append(self.getTime(stop.timeToNext))
		ids.append(stop.id)

	parameters['order'] = order
	parameters['arrivalTimes'] = arrivalTimes
	parameters['ids'] = ids
	parameters['idealTimes'] = self.idealTimes

	return parameters, arrivalTimes

class Bus:

	def __init__(self, path, func_people, runFunc=runStandard):
		self.path = path
		self.stops, self.idealTimes = self.createStops(path, func_people)
		self.runFunc = runFunc 

	"""
	Action
	@param 
	@return 
	"""
	def run(self, startTime):
		return self.runFunc(self, startTime)

	"""
	Action
	@param 
	@return 
	"""
	def getTime(self, distance):
		return distance + randint(-1,5)

	"""
	Action
	@param 
	@return 
	"""
	def createStops(self, path, func_people):
		stops = []
		idealTimes = []
		for place in path:
			newStop = Stop(place, func_people)
			stops.append(newStop)
			idealTimes.append(place['timeToNext'])


		return stops, idealTimes

	def pprint(self):
		print 'oi'
