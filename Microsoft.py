# Information bank for the company
class Personell:
    company='Microsft'
    class_attribute= "Employee's Personal Information\n"
    def __init__(self,name,age,gender,nationality,desination,department,role,salary,OS,CPU,GPU,RAM):
        self.name=name
        self.age=age
        self.gender=gender
        self.nationality=nationality
        self.email=self.generateEmail()
        self.job=self.Job(desination,department,role,salary)
        self.computer=self.Computer(OS,CPU,GPU,RAM)
    def generateEmail(self):
        return(f'{self.name}@{self.company}.com')
    class Job:
        class_attribute= "Employee's Job Information\n"
        def __init__(self,desination,department,role,salary):
            self.designation=desination
            self.department=department
            self.role=role
            self.salary=salary
    class Computer:
        class_attribute=" Employee's Computer Specs\n"
        def __init__(self,OS,CPU,GPU,RAM):
            self.OS=OS
            self.CPU=CPU
            self.GPU=GPU
            self.RAM=RAM

personell1 = Personell('John',26,'Male','American','Resident','Software','Engineer','$40000','MacOS','M2','GTX1640','64GB')
personell2 = Personell('Peter',24,'Male','Russian','Manager','Software','Development','$70000','Windows 11', 'i9','GTX1670','64GB')
personell3 = Personell('convenant',29,'Female','Aussie','Vice President', 'Software','Engineering','$140000','MacOS','M4','GTX2019','128GB')
personell01 = Personell.Job('Resident','Software','Engineer','$40000')
personell02 = Personell.Job('Manager','Software','Development','$70000')
personell03= Personell.Job('Vice President', 'Software','Engineering','$140000')
personel11001=Personell.Computer('MacOS','M2','GTX1640','64GB')
personel11002=Personell.Computer('Windows 11', 'i9','GTX1670','64GB')
personel11003=Personell.Computer('MacOS','M4','GTX2019','128GB')

print(Personell.class_attribute)
print(f'{personell1.name} {personell1.age} {personell1.gender} {personell1.nationality} {personell1.generateEmail()}')
print(f'{personell2.name} {personell2.age} {personell2.gender} {personell2.nationality} {personell2.generateEmail()}')
print(f'{personell3.name} {personell3.age} {personell3.gender} {personell3.nationality} {personell3.generateEmail()}\n')
print(Personell.Job.class_attribute)
print(f'{personell1.name} {personell01.designation} {personell01.department} {personell01.role} {personell01.salary}')
print(f'{personell2.name} {personell02.designation} {personell02.department} {personell02.role} {personell02.salary}')
print(f'{personell3.name} {personell03.designation} {personell03.department} {personell03.role} {personell03.salary}\n')
print(Personell.Computer.class_attribute)
print(f'{personell1.name} {personel11001.OS} {personel11001.CPU} {personel11001.GPU} {personel11001.RAM}')
print(f'{personell2.name} {personel11002.OS} {personel11002.CPU} {personel11002.GPU} {personel11002.RAM}')
print(f'{personell3.name} {personel11003.OS} {personel11003.CPU} {personel11003.GPU} {personel11003.RAM}')