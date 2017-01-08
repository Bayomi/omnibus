class TimeBuilder:

	def __init__(self, timeStr='empty'):
		if timeStr != 'empty':
			self.minutes = self.getMinutesFromStr(timeStr)
			self.hours = self.getHoursFromStr(timeStr)

	"""
	Process the data using the pre_processing.py file parameters.
	@param 
	@return
	"""

	def getHours(self):
		return self.hours

	def getMinutes(self):
		return self.minutes

	def addMinutes(self, minutesToAdd):
		hours = int(self.getHours()) + int(minutesToAdd/60)
		minutes = int(self.getMinutes()) + int(minutesToAdd%60)

		if minutes >= 60:
			minutes = minutes - 60
			hours = hours + 1
			
		if hours>24:
			hours = hours - 24

		hoursStr = self.correctDoubleZeros(hours)
		minutesStr = self.correctDoubleZeros(minutes)
		string = hoursStr + ':' + minutesStr

		return TimeBuilder(string)

	def removeMinutes(self, minutesToRemove):
		hours = int(self.getHours())
		minutes = int(self.getMinutes()) - int(minutesToRemove%60)

		if minutes < 0:
			minutes = minutes + 60
			hours = hours - 1


		hoursStr = self.correctDoubleZeros(hours)
		minutesStr = self.correctDoubleZeros(minutes)
		string = hoursStr + ':' + minutesStr

		return TimeBuilder(string)

	def getMinutesFromStr(self, timeStr):
		time = timeStr.split(':')
		minutes = str(time[1])
		return minutes

	def getHoursFromStr(self, timeStr):
		time = timeStr.split(':')
		hours = str(time[0])
		return hours

	def correctDoubleZeros(self, ref):
		strRef = str(ref)
		length = len(strRef)

		if(length == 1):
			return '0' + strRef

		return strRef

	def toSec(self):
		hours = self.getHours()
		minutes = self.getMinutes()

		seconds = int(hours)*3600 + int(minutes)*60

		return seconds

	def getStr(self):

		hours = self.getHours()
		minutes = self.getMinutes()

		hoursStr = self.correctDoubleZeros(hours)
		minutesStr = self.correctDoubleZeros(minutes)
		string = hoursStr + ':' + minutesStr

		return string
