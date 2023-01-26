class Employee:
    no_of_employees = 0

    def __init__(self, name, family_name, salary, department):
        self.__name = name
        self.__family_name = family_name
        self.salary = salary
        self.__department = department
        Employee.no_of_employees += 1

    @staticmethod
    def average_salary(employees):
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.no_of_employees

class FulltimeEmployee(Employee):

    def __init__(self, name, family_name, salary, department):
        super().__init__(name, family_name, salary, department)

    def full_time_benefits(self):
        print("Few benefits as full time employee.")


def main():
    employees = []
    fte1 = FulltimeEmployee("Employee1", "FamilyName1", 120000, "Management")
    fte1.full_time_benefits()
    employees.append(fte1)
    fte2 = FulltimeEmployee("Employee2", "FamilyName2", 180000, "RnD")
    employees.append(fte2)
    emp1 = Employee("Employee3", "FamilyName3", 160000, "Marketing")
    employees.append(emp1)
    emp2 = Employee("Employee4", "FamilyName4", 135000, "HR")
    employees.append(emp2)
    print("Average salary:", FulltimeEmployee.average_salary(employees))

if __name__ == "__main__":
    main()