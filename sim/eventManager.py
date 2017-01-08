# EventManager

class EventManager:

	def __init__(self):
		print "Criar EventManager"
		self.queue = []

	def scheduleEvent(self,event,time):
		print "Agendar evento"
		self.queue.insert(event,time)
		self.queue.sort(time)

	def unscheduleEvent(self,event,time):
		print "Desagendar evento"
		self.queue.remove(event,time)