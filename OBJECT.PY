# A basic object oriented file
class Personell:
    company="Assassin's Creed"
    class_attribute='This is a directory for the information of all staff\n'
    def __init__(self,name,age,gender,nationality,designation,department,role,salary,YOE,gun,knife,amour):
        self.name=name
        self.age=age
        self.gender=gender
        self.nationality=nationality
        self.email=self.generateEmail()
        self.job=self.Job(designation,department,role,salary,YOE)
        self.toos=self.Tools(gun,knife,amour)
    def generateEmail(self):
        return (f'{self.name}@{self.company}.com')
    class Job:
        class_attribute='This directory gives us the Job description of each employee\n'
        def __init__(self,designation,department,role,salary,YOE):
            self.designation=designation
            self.department=department
            self.role=role
            self.salary=salary
            self.YOE=YOE
    class Tools:
        class_attribute='This directory tells us what tool each employee uses\n'
        def __init__(self,gun,knife,amour,):
            self.gun=gun
            self.knife=knife
            self.amour=amour

personell_1=Personell('Jonathan Wick',36,'Male','Carribean','Staff','Public Relations','HitMan','$60000',6,'Barretta','Hunting Knife','Vest')
personell_2=Personell('Jason Statham',37,'Male','British','Staff','Human Resources','Transporter','$80000',7,'Bobcat','Dagger','None')
personell_3=Personell('Nikita Anders',29,'Female','Taiwanese','staff','Human Resources','Sniper','$1000000',8,'GOL-Sniper Magnum','Shuriken','Plaid Body Amour')
personell_4=Personell('Denzel Washington',36,'Male','American','Staff','Public Relations','Equalizer','$120000',9,'AMT','Axe','None')
personell_5=Personell('Tom Polo',45,'Male','Nigerian','Staff','Public Relations','Thug','$30000',10,'Awka','Shank','None')

personell_01=Personell.Job('Staff','Public Relations','HitMan','$60000',6)
personell_02=Personell.Job('Staff','Human Resources','Transporter','$80000',7)
personell_03=Personell.Job('staff','Human Resources','Sniper','$1000000',8)
personell_04=Personell.Job('Staff','Public Relations','Equalizer','$120000',9)
personell_05=Personell.Job('Staff','Public Relations','Thug','$30000',10)

personell_001=Personell.Tools('Barretta','Hunting Knife','Vest')
personell_002=Personell.Tools('Bobcat','Dagger','None')
personell_003=Personell.Tools('GOL-Sniper Magnum','Shuriken','Plaid Body Amour')
personell_004=Personell.Tools('AMT','Axe','None')
personell_005=Personell.Tools('Awka','Shank','None')

print(Personell.class_attribute)
print(f'{personell_1.name},{personell_1.age},{personell_1.gender},{personell_1.nationality},{personell_1.generateEmail()}')
print(f'{personell_2.name},{personell_2.age},{personell_2.gender},{personell_2.nationality},{personell_2.generateEmail()}')
print(f'{personell_3.name},{personell_3.age},{personell_3.gender},{personell_3.nationality},{personell_3.generateEmail()}')
print(f'{personell_4.name},{personell_4.age},{personell_4.gender},{personell_4.nationality},{personell_4.generateEmail()}')
print(f'{personell_5.name},{personell_5.age},{personell_5.gender},{personell_5.nationality},{personell_5.generateEmail()}\n')

print(Personell.Job.class_attribute)
print(f'{personell_01.designation},{personell_01.department},{personell_01.role},{personell_01.salary},{personell_01.YOE}')
print(f'{personell_02.designation},{personell_02.department},{personell_02.role},{personell_02.salary},{personell_02.YOE}')
print(f'{personell_03.designation},{personell_03.department},{personell_03.role},{personell_03.salary},{personell_03.YOE}')
print(f'{personell_04.designation},{personell_04.department},{personell_04.role},{personell_04.salary},{personell_04.YOE}')
print(f'{personell_05.designation},{personell_05.department},{personell_05.role},{personell_05.salary},{personell_05.YOE}\n')

print(Personell.Tools.class_attribute)
print(f'{personell_001.gun},{personell_001.knife},{personell_001.amour}')
print(f'{personell_002.gun},{personell_002.knife},{personell_002.amour}')
print(f'{personell_003.gun},{personell_003.knife},{personell_003.amour}')
print(f'{personell_004.gun},{personell_004.knife},{personell_004.amour}')
print(f'{personell_005.gun},{personell_005.knife},{personell_005.amour}')