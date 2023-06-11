from Models.Workschedules.Workschedule import Workschedule

class CSP:
    def __init__(self, employees, maxNumEmployeesOnMonday, maxNumEmployeesOnTuesday, maxNumEmployeesOnWednesday, maxNumEmployeesOnThursday, maxNumEmployeesOnFriday):
        self.employees = employees
        self.workschedule = Workschedule()
        self._saveStepsDays = []
        self._saveStepsID = []
        self._saveStepsWorkshift = []
        self.maxNumEmployeesOnMonday = maxNumEmployeesOnMonday + 1
        self.maxNumEmployeesOnTuesday = maxNumEmployeesOnTuesday + 1
        self.maxNumEmployeesOnWednesday = maxNumEmployeesOnWednesday + 1
        self.maxNumEmployeesOnThursday = maxNumEmployeesOnThursday + 1
        self.maxNumEmployeesOnFriday = maxNumEmployeesOnFriday + 1

    @property
    def saveStepsDays(self):
        return self._saveStepsDays

    @saveStepsDays.setter
    def saveStepsDays(self, value):
            self._saveStepsDays = value

    @property
    def saveStepsWorkshift(self):
        return self._saveStepsWorkshift

    @saveStepsWorkshift.setter
    def saveStepsWorkshift(self, value):
            self._saveStepsWorkshift = value

    @property
    def saveStepsID(self):
        return self._saveStepsID

    @saveStepsID.setter
    def saveStepsID(self, value):
            self._saveStepsID = value            

    def SortByMinimumRemainingValues(self):
        length = len(self.employees)

        for i in range(0, length):
            for j in range(0, length - i - 1):
                if len(str(self.employees[j].preferredWorkShit)) > len(str(self.employees[j + 1].preferredWorkShit)):
                    temp = self.employees[j]
                    self.employees[j] = self.employees[j + 1]
                    self.employees[j + 1] = temp

    def AddEmployee(self, workingDay, employee):
        if workingDay == 'Monday':
            self.workschedule.Monday.append(employee)
        elif workingDay == 'Tuesday':
            self.workschedule.Tuesday.append(employee)
        elif workingDay == 'Wednesday':
            self.workschedule.Wednesday.append(employee)
        elif workingDay == 'Thursday':
            self.workschedule.Thursday.append(employee)
        else:
            self.workschedule.Friday.append(employee)

    def IsOnList(self, workingDay, employee): 
        if workingDay == 'Monday':
            for checkEmployee in self.workschedule.Monday :
                if employee.id == checkEmployee.id:
                    return True
            return False   
        
        elif workingDay == 'Tuesday':
            for checkEmployee in self.workschedule.Tuesday:
                if employee.id == checkEmployee.id:
                    return True
            return False  
        
        elif workingDay == 'Wednesday':
            for checkEmployee in self.workschedule.Wednesday:
                if employee.id == checkEmployee.id:
                    return True
            return False
        
                
        elif workingDay == 'Thursday':
            for checkEmployee in self.workschedule.Thursday:
                if employee.id == checkEmployee.id:
                    return True
            return False
        
        elif workingDay == 'Friday':
            for checkEmployee in self.workschedule.Friday:
                if employee.id == checkEmployee.id:
                    return True
            return False

    def CheckEmployeesOn3rdWorkshift(self, workingDay): 
        if workingDay == 'Monday':
            if self.workschedule.employeesOn3rdworkShitOnMonday < self.maxNumEmployeesOnMonday:
                return True
            else:
                return False
            
        elif workingDay == 'Wednesday':
            if self.workschedule.employeesOn3rdworkShitOnWednesday < self.maxNumEmployeesOnWednesday:
                return True
            else:
                return False
            
        elif workingDay == 'Tuesday':
            if self.workschedule.employeesOn3rdworkShitOnTuesday < self.maxNumEmployeesOnTuesday:
                return True
            else:
                return False
            
        elif workingDay == 'Thursday':
            if self.workschedule.employeesOn3rdworkShitOnThursday < self.maxNumEmployeesOnThursday:
                return True
            else:
                return False
            
        elif workingDay == 'Friday':
            if self.workschedule.employeesOn3rdworkShitOnFriday < self.maxNumEmployeesOnFriday:
                return True
            else:
                return False
            
    def SetEmployeesOn3rdWorkshift(self, workingDay): 
        if workingDay == 'Monday':
            self.workschedule.employeesOn3rdworkShitOnMonday = self.workschedule.employeesOn3rdworkShitOnMonday + 1
        elif workingDay == 'Tuesday':
            self.workschedule.employeesOn3rdworkShitOnTuesday = self.workschedule.employeesOn3rdworkShitOnTuesday + 1
        elif workingDay == 'Wednesday':
            self.workschedule.employeesOn3rdworkShitOnWednesday = self.workschedule.employeesOn3rdworkShitOnWednesday + 1
        elif workingDay == 'Thursday':
            self.workschedule.employeesOn3rdworkShitOnWednesday = self.workschedule.employeesOn3rdworkShitOnWednesday + 1
        elif workingDay == 'Friday':
            self.workschedule.employeesOn3rdworkShitOnWednesday = self.workschedule.employeesOn3rdworkShitOnWednesday + 1

    def SetWorkhours(self, workingDay, employee, workshift): 
        if workingDay == 'Monday':
            if workshift == 3:
                employee.workShitOnMonday = "22:00 - 6:00"
            elif workshift == 2:
                employee.workShitOnMonday = "14:00 - 22:00"
            else:
                employee.workShitOnMonday = "6:00 - 14:00"

        elif workingDay == 'Tuesday':
            if workshift == 3:
                employee.workShitOnTuesday = "22:00 - 6:00"
            elif workshift == 2:
                employee.workShitOnTuesday = "14:00 - 22:00"
            else:
                employee.workShitOnTuesday = "6:00 - 14:00"

        elif workingDay == 'Wednesday':
            if workshift == 3:
                employee.workShitOnWednesday = "22:00 - 6:00"
            elif workshift == 2:
                employee.workShitOnWednesday = "14:00 - 22:00"
            else:
                employee.workShitOnWednesday = "6:00 - 14:00"

        elif workingDay == 'Thursday':
            if workshift == 3:
                employee.workShitOnThursday = "22:00 - 6:00"
            elif workshift == 2:
                employee.workShitOnThursday = "14:00 - 22:00"
            else:
                employee.workShitOnThursday = "6:00 - 14:00"


        elif workingDay == 'Friday':
            if workshift == 3:
                employee.workShitOnFriday = "22:00 - 6:00"
            elif workshift == 2:
                employee.workShitOnFriday = "14:00 - 22:00"
            else:
                employee.workShitOnFriday = "6:00 - 14:00"

    def ChechConstraints(self, employee, workingDay):
        if "3" in str(employee.preferredWorkShit) and self.CheckEmployeesOn3rdWorkshift(workingDay) == True:
            self.SetWorkhours(workingDay, employee, 3)
            self.SetEmployeesOn3rdWorkshift(workingDay)
            self.AddEmployee(workingDay, employee)
            self.saveStepsDays.append(workingDay)
            self.saveStepsID.append(employee.id)
            self.saveStepsWorkshift.append(3)
        elif "2" in str(employee.preferredWorkShit) and self.IsOnList(workingDay, employee) == False:
            self.SetWorkhours(workingDay, employee, 2)
            self.AddEmployee(workingDay, employee)
            self.saveStepsDays.append(workingDay)
            self.saveStepsID.append(employee.id)
            self.saveStepsWorkshift.append(2)
        elif "1" in str(employee.preferredWorkShit) and self.IsOnList(workingDay, employee) == False:
            self.SetWorkhours(workingDay, employee, 1)
            self.AddEmployee(workingDay, employee)
            self.saveStepsDays.append(workingDay)
            self.saveStepsID.append(employee.id)
            self.saveStepsWorkshift.append(1)

    # Minimum Remaining Values
    def GenerateWorkschedule(self):
        if len(self.employees) <= 0:
            return 'There is no data in the database'
        
        self.SortByMinimumRemainingValues()

        steps = 0
        for workingDay in self.workschedule.WorkingDays:
            for employee in self.employees:

                # constraints and adding employee
                if "1" in str(employee.preferredWorkingDays) and workingDay == 'Monday':
                    self.ChechConstraints(employee, workingDay)
                if "2" in str(employee.preferredWorkingDays) and workingDay == 'Tuesday':
                    self.ChechConstraints(employee, workingDay)
                if "3" in str(employee.preferredWorkingDays) and workingDay == 'Wednesday':
                    self.ChechConstraints(employee, workingDay)
                if "4" in str(employee.preferredWorkingDays) and workingDay == 'Thursday':
                    self.ChechConstraints(employee, workingDay)
                if "5" in str(employee.preferredWorkingDays) and workingDay == 'Friday':
                    self.ChechConstraints(employee, workingDay)

                steps = steps + 1
        return steps
    
    def PrintWorkschedule(self):
        return self.workschedule.GetWorkschedule()
