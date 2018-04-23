
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic=dict()
        for e in employees:
            print e
            if e.id not in dic:
                dic[e.id]=e


        return self.getImportance(dic,id)


    def getTotalImportance(self, dic, id):
        sum=0
        if id in dic:
            emp= dic[id]
            sum+=emp.importance
            subs=emp.subordinates
            for s in subs:
                sum+= self.getTotalImportance(dic, s.id)
        return sum 


