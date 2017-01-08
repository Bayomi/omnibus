# Bus

class Bus:

	def __init__(self):
		print "Criar ônibus"
		self.path = ["Rodoferroviária","Parada2","Parada3"] # paradas
		self.nextTime = checkTime(self.path[0])
		self.scheduleNextStop(self.path[1],self.nextTime)

	def checkTime(self,stop):
		print "Analisa trafego e retorna tempo"
		if stop == "Rodoferroviária"
			return timeNow() + 3*60 # + trafego + aleatorio (em seg)
		elif stop == "Parada 2"
			return timeNow() + 4*60 # + trafego + aleatorio (em seg)

	def scheduleNextStop(self,stop,time):
		print "Agendar próxima parada"
		EventManager.scheduleEvent(self.arrivedNextStop(),time)

	def arrivedNextStop(self):
		self.path.rotateLeft() # parada atual vira a última

# Stop

class Stop:

	def __init__(self,personsThroughTheDay):
		print "Criar parada"
		self.persons = []
		self.personsThroughTheDay = personsThroughTheDay
		self.scheduleCreatePersons()

	def createPerson(self, arrival):
		print "Chamado pelo agendamento e cria pessoa"
		self.persons.push(Person(arrival))

	def scheduleCreatePersons(self):
		print "Agendar próximas pessoas a serem criadas"
		for (time in personsThroughTheDay) # gera todas as pessoas
			EventManager.scheduleEvent(self.createPerson(time),time)

	def removePerson(self,person):
		self.persons.pop(person)

# Person

class Person(Stop):

	def __init__(self,arrival):
		print "Criar pessoa"
		self.arrival = arrival
		self.notHereDistribution = [0,5,8,10,15] # tempos que ela avisa que não chegou
		self.scheduleBusNotHere()

	def scheduleBusNotHere(self):
		print "Agendar próximos busNotHere eventos"
		for (time in notHereDistribution)
		EventManager.scheduleEvent(self.busNotHere(),timeNow() + time)

	def busNotHere(self):
		print "Enviar evento busNotHere"

	def busHere(self):
		print "Enviar evento busHere"
		if self.gotIn():
			for (time in notHereDistribution)
				EventManager.unscheduleEvent(self.busNotHere(),timeNow() + time)
			Stop.removePerson(self)

	def gotIn(self):
		return true;
