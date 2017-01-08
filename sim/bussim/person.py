import numpy as np
from random import randint
from temp import TimeBuilder as tb
import json

def logFuncStandard(self, date):

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

class Person():

    def __init__(self, style, timeOfReport, logFunc=logFuncStandard):
        self.style = style
        self.timeOfReport = timeOfReport
        self.id = self.getRandomId()
        self.logFunc = logFunc

    def report(self, date):
        log = self.createLog(date)
        return log

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

    def estimateReport(self, style, timeOfReport, date):

        #prob = randint(-3,3)*60 + diff
        #expectedTime = tb(timeAtStopReal).addMinutes(prob).getStr()

        report = {}
        report['time'] = timeOfReport
        report['diff'] = 3

        return report


    def createLog(self, date):
        return self.logFunc(self, date)

