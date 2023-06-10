from DataAccessLayer.FileOperation import FileOperation
from Model.Employee import Employee
import os

class Datebase:
    def LoadExampleDataBase(self, list):
        file = FileOperation()
        path = os.path.join(os.path.dirname(__file__), 'ARFF', 'exampleDatabase.arff')
        file.ReadFrom(path, list)

    def FindMaxId(self, list):
        max = 1
        for employee in list:
            if employee.id > max:
                max = employee.id
        return max
    
    def SaveDataToDataBase(self, length, name, jobPosition, preferredWorkingDays, workshift, list):
        maxId = self.FindMaxId(list) + 1
        i = 0
        for employee in range(length):
            if name and jobPosition and workshift:
                employee = Employee(maxId, str(name[i]), str(jobPosition[i]), preferredWorkingDays, workshift)
                list.append(employee)
                maxId = maxId + 1
                i = i + 1