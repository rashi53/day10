Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:/python/Python37-32/day10/1.py =================
Name; nikhil ,salary: 9999
is salary an attribute: True
9999
modified salary 7000
False
True
added attribute manager
is salary an attribute: False
>>> import employee
Name; nikhil ,salary: 9999
is salary an attribute: True
9999
modified salary 7000
False
True
added attribute manager
is salary an attribute: False
>>> help(employee.Employee)
Help on class Employee in module employee:

class Employee(builtins.object)
 |  Employee(name, salary)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name, salary)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  displayCount(self)
 |  
 |  displayEmployee(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  empCount = 1

>>> import employee
>>> 
================= RESTART: C:/python/Python37-32/day10/2.py =================
Employee.__doc__: None
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: (<class '__main__.A'>, <class '__main__.B'>)
Employee.__dict__: {'__module__': '__main__', 'empCount': 0, '__init__': <function Employee.__init__ at 0x03836780>, 'displayCount': <function Employee.displayCount at 0x03A6BDB0>, 'displayEmployee': <function Employee.displayEmployee at 0x03A6BDF8>, '__doc__': None}
>>> 
================= RESTART: C:/python/Python37-32/day10/2.py =================
Employee.__doc__: 
this is documntation string

Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: (<class '__main__.A'>, <class '__main__.B'>)
Employee.__dict__: {'__module__': '__main__', '__doc__': '\nthis is documntation string\n', 'empCount': 0, '__init__': <function Employee.__init__ at 0x02EA6780>, 'displayCount': <function Employee.displayCount at 0x030DBDB0>, 'displayEmployee': <function Employee.displayEmployee at 0x030DBDF8>}
>>> 
================= RESTART: C:/python/Python37-32/day10/3.py =================
43699728 43699728 43699728
Point destroyed
>>> 
================= RESTART: C:/python/Python37-32/day10/4.py =================
output is: 10
content of variabe length tuple is:

output is: 70
content of variabe length tuple is:
Traceback (most recent call last):
  File "C:/python/Python37-32/day10/4.py", line 11, in <module>
    printinfo(70,60,50)
  File "C:/python/Python37-32/day10/4.py", line 6, in printinfo
    print(var_tuple,end=' ')
NameError: name 'var_tuple' is not defined
>>> 
================= RESTART: C:/python/Python37-32/day10/4.py =================
output is: 10
content of variabe length tuple is:

output is: 70
content of variabe length tuple is:
60 50 
output is: 70
content of variabe length tuple is:
60 tea samosa chips cake 50 
>>> 
================= RESTART: C:/python/Python37-32/day10/5.py =================
Traceback (most recent call last):
  File "C:/python/Python37-32/day10/5.py", line 7, in <module>
    test_fun(**tup)
NameError: name 'tup' is not defined
>>> 
================= RESTART: C:/python/Python37-32/day10/5.py =================
args1 programming
Traceback (most recent call last):
  File "C:/python/Python37-32/day10/5.py", line 7, in <module>
    test_fun(*tup1)
  File "C:/python/Python37-32/day10/5.py", line 3, in test_fun
    print("args2",course)
NameError: name 'course' is not defined
>>> 
================= RESTART: C:/python/Python37-32/day10/5.py =================
args1 programming
args2 python
args3 20000
args1 multimedia
args2 animation
args3 30000
>>> 
================= RESTART: C:/python/Python37-32/day10/6.py =================
alex is skilled in ('python', 'html') language 
alex is skilled in 2 language 
parvesh is skilled in ('java', 'c', 'c++') language 
parvesh is skilled in 3 language 
ajay is skilled in () language 
ajay is skilled in 0 language 
>>> 
================= RESTART: C:/python/Python37-32/day10/7.py =================
Inside the function local total: 30
outside the function local total: 30
>>> 
