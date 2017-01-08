import math
import numpy as np
from bus import Bus

class Manager:

	def __init__():
		print 'oi'

	def route(bus, startTime):
		parameters, timeInfo = bus.route(startTime)
		predictInfo = []
		print parameters
		print timeInfo
		
		for stop in bus.stops:
			predictInfo.append(stop.check(parameters))

		tableOfficial = getTable(timeInfo)
		tablePreview = getTable(predictInfo)

		return tableOfficial, tablePreview

	def getTable(info):
		table = []
		return table


	path = []
	bus110 = Bus(path)

	bus110.pprint()




