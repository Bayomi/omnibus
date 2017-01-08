#-----BUS REPORT-----#
"""
Action
@param 
@return 
"""
def run(self, startTime):
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

"""
Action
@param 
@return 
"""
def getTime(self, distance):
	return distance + randint(-1,5)

#-----CREATE PEOPLE-----#

"""
Process the data using the pre_processing.py file parameters.
@param {String}
@return {Array} 
"""
def createPeople(self, timeAtStopIdeal, timeAtStopReal, date):
	self.people = []
	for i in range(0,randint(0,14)):
		newPerson = Person(1,timeAtStopIdeal,timeAtStopReal)
		self.people.append(newPerson)
		return self.people


#-----CREATE REPORT-----#

def createLog(self, date):

    log = {}
    log['id'] = self.id
    log['date'] = date

    diff = tb(self.timeAtStopReal).toSec() - tb(self.timeAtStopIdeal).toSec()
    report = self.estimateReport(self.style, diff, self.timeAtStopReal, date)

    log['reportedTimeString'] = report['time']
    log['reportedTimeNum'] = tb(report['time']).toSec()
    log['diff'] = report['diff']
    log['isLate'] = log['diff']>0

    info = {}
    info[self.id] = log

    return info



