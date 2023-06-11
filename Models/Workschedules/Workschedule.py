class Workschedule:
        def __init__(self):
                self.WorkingDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                self.Monday    = []
                self.Tuesday   = []
                self.Wednesday = []
                self.Thursday  = []
                self.Friday    = []
                self._employeesOn3rdworkShitOnMonday    = 0
                self._employeesOn3rdworkShitOnTuesday   = 0
                self._employeesOn3rdworkShitOnWednesday = 0
                self._employeesOn3rdworkShitOnThursday  = 0
                self._employeesOn3rdworkShitOnFriday    = 0

        @property
        def employeesOn3rdworkShitOnMonday(self):
                return self._employeesOn3rdworkShitOnMonday

        @employeesOn3rdworkShitOnMonday.setter
        def employeesOn3rdworkShitOnMonday(self, value):
                self._employeesOn3rdworkShitOnMonday = value

        
        @property
        def employeesOn3rdworkShitOnTuesday(self):
                return self._employeesOn3rdworkShitOnTuesday

        @employeesOn3rdworkShitOnTuesday.setter
        def employeesOn3rdworkShitOnTuesday(self, value):
                self._employeesOn3rdworkShitOnTuesday = value

        @property
        def employeesOn3rdworkShitOnWednesday(self):
                return self._employeesOn3rdworkShitOnWednesday

        @employeesOn3rdworkShitOnWednesday.setter
        def employeesOn3rdworkShitOnWednesday(self, value):
                self._employeesOn3rdworkShitOnWednesday = value

        @property
        def employeesOn3rdworkShitOnThursday(self):
                return self._employeesOn3rdworkShitOnThursday

        @employeesOn3rdworkShitOnThursday.setter
        def employeesOn3rdworkShitOnThursday(self, value):
                self._employeesOn3rdworkShitOnThursday = value

        @property
        def employeesOn3rdworkShitOnFriday(self):
                return self._employeesOn3rdworkShitOnFriday

        @employeesOn3rdworkShitOnFriday.setter
        def employeesOn3rdworkShitOnFriday(self, value):
                self._employeesOn3rdworkShitOnFriday = value

        def GetWorkschedule(self):
                schedule = []
                for workingDay in self.WorkingDays:
                        schedule.append("")
                        schedule.append("DAY: " + workingDay)
                        schedule.append("--------------------------------------")
                        if workingDay == 'Monday':
                                for employee in self.Monday:
                                        schedule.append("Id: " + str(employee.id))
                                        schedule.append("Name and last name: " + str(employee.nameAndLastName))
                                        schedule.append("Job position: " + str(employee.jobPosititon))
                                        schedule.append("Work hours: " + str(employee.workShitOnMonday))
                                        schedule.append("")
                        elif workingDay == 'Tuesday':
                                for employee in self.Tuesday:
                                        schedule.append("Id: " + str(employee.id))
                                        schedule.append("Name and last name: " + str(employee.nameAndLastName))
                                        schedule.append("Job position: " + str(employee.jobPosititon))
                                        schedule.append("Work hours: " + str(employee.workShitOnTuesday))
                                        schedule.append("")
                        elif workingDay == 'Wednesday':
                                for employee in self.Wednesday:
                                        schedule.append("Id: " + str(employee.id))
                                        schedule.append("Name and last name: " + str(employee.nameAndLastName))
                                        schedule.append("Job position: " + str(employee.jobPosititon))
                                        schedule.append("Work hours: " + str(employee.workShitOnWednesday))
                                        schedule.append("")
                        elif workingDay == 'Thursday':
                                for employee in self.Thursday:
                                        schedule.append("Id: " + str(employee.id))
                                        schedule.append("Name and last name: " + str(employee.nameAndLastName))
                                        schedule.append("Job position: " + str(employee.jobPosititon))
                                        schedule.append("Work hours: " + str(employee.workShitOnThursday))
                                        schedule.append("")
                        else:
                                for employee in self.Friday:
                                        schedule.append("Id: " + str(employee.id))
                                        schedule.append("Name and last name: " + str(employee.nameAndLastName))
                                        schedule.append("Job position: " + str(employee.jobPosititon))
                                        schedule.append("Work hours: " + str(employee.workShitOnFriday))
                                        schedule.append("")
                return schedule