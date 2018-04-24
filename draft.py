
from flask import Flask

class Person:
    school= 'primary school'

    def getSchool(self):
        print self.school

class Tech(Person):
    school='high school'

p=Person()
q=Tech()
p.getSchool()
q.getSchool()