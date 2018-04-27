'''
comprehension of list
if is optional
[expr(item) for item in iterable if predicate(item)]


a=['test','test2','test3']

b=[len(item) for item in a]


set comprehension
{expr(item) for item in iterable}

dictionary comprehension
{key_expr:value_expr for item in iterable}


generator
yield


def gen123():
    yield 1
    yield 2
    yield 3

g=gen123()
for x in g:
    print x

p=gen123()
print "p",p
for pi in p:
    print pi


generator comprehension
(expr(item) for item in iterable)
this is a single use object

but when calling a generator function
a  new generator object is created.


sum(x*x for x in range(1,100001))

using this expression can help us save memory
sum(x*x for x in range(1,100001) if is_prime(x))

any(is_prime(x) for x in range(1,39))
all(is_prime(x) for x in range(1,39))

monday=[12,23,23]
sunday=[2,3,4]
temperatures=chain(monday,sunday)
chain combine the two lists without duplicating the data
'''

class AirCraft:
    def num_seats(self):
        rows, row_seats=self.seating_plan()
        return len(rows)*len(row_seats)

class AirBus(AirCraft):
    def seating_plan(self):
        return range(1,23),"ABCDE"

class Boeing(AirCraft):
    def seating_plan(self):
        return range(1,56),"ABCDEFG"

a= AirBus()
print a.num_seats()

b=Boeing()
print b.num_seats()

aircraft=AirCraft()
print aircraft.num_seats()


































