from Model.Employee import Employee
import arff

class FileOperation:
    def ReadFrom(self, filename, list):
            
        if len(list) != 0:
            list.clear()

        with open(filename, 'r') as f:
            for row in arff.load(f.name):
                employee = Employee(row.id_employee, row.name_and_last_name, row.job_position, row.preferred_working_days, row.preferred_work_shift)
                list.append(employee)

    def SaveTo(self, filename, list):
        temp = []
        
        for employee in list:
            row = []
            row.append(employee.id)
            row.append(employee.nameAndLastName)
            row.append(employee.preferredWorkingDays)
            row.append(employee.preferredWorkShit)
            row.append(employee.jobPosititon)
            temp.append(row)

        with open(filename, 'w') as f:
            arff.dump(f.name, temp, relation="work", names=['id_employee', 'name_and_last_name', 'preferred_working_days','preferred_work_shift', 'job_position'])