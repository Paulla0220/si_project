class Employee:
    def __init__(self, idEmpoyee, nameAndLastName, jobPosititon, preferredWorkingDays, preferredWorkShit):
        self.id = idEmpoyee
        self.nameAndLastName = nameAndLastName
        self.jobPosititon = jobPosititon
        self.preferredWorkingDays = preferredWorkingDays
        self.preferredWorkShit = preferredWorkShit 
        self._workShitOnMonday = None
        self._workShitOnTuesday = None
        self._workShitOnWednesday = None
        self._workShitOnThursday = None
        self._workShitOnFriday = None

    @property
    def workShitOnMonday(self):
        return self._workShitOnMonday

    @workShitOnMonday.setter
    def workShitOnMonday(self, value):
        self._workShitOnMonday = value

    @property
    def workShitOnTuesday(self):
        return self._workShitOnTuesday

    @workShitOnTuesday.setter
    def workShitOnTuesday(self, value):
        self._workShitOnTuesday = value
    
    
    @property
    def workShitOnWednesday(self):
        return self._workShitOnWednesday

    @workShitOnWednesday.setter
    def workShitOnWednesday(self, value):
        self._workShitOnWednesday = value

    @property
    def workShitOnThursday(self):
        return self._workShitOnThursday

    @workShitOnThursday.setter
    def workShitOnThursday(self, value):
        self._workShitOnThursday = value

    
    @property
    def workShitOnFriday(self):
        return self._workShitOnFriday

    @workShitOnFriday.setter
    def workShitOnFriday(self, value):
        self._workShitOnFriday = value