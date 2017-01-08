import numpy as np


class Bus:

	def __init__(self, path):
		self.path = path
		self.stops = self.createStops(path)

	def route(self, startTime):
		parameters = {}
		parameters.startTime = startTime
		order = []
		arrivalTimes = []
		for stop in self.stops:
			order.append(stop.name)
			arrivalTimes.append(self.getTime(stop.distanceToNext))

		parameters.order = order
		parameters.arrivalTimes = arrivalTimes

		return parameters

	def getTime(self, distance):
		time = 0
		return time


	def createStops(self, path):
		stops = []
		for place in path:
			newStop = Stop(place)
			stops.append(newStop)

		return stops

	def pprint(self):
		print 'oi'
