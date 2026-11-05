from datetime import datetime

class WORKER:

    def __init__(self, name, yearborn, work_experience):
        self.name = name
        self.yearborn = yearborn
        self.work_experience = work_experience

    def CalcAge(self):
        current_year = datetime.now().year
        return current_year - self.yearborn

    def ShowYear(self):
        return self.yearborn

    def SetWork(self, work_experience):
        self.work_experience = work_experience
