import sqlite3
import Employee
conn = sqlite3.connect('employee.db')

c = conn.cursor()
#c.execute("""create table employees(first text,last text,pay integer)""")

#emp1 = Employee.Employee('Hem','Sagar',2000)
#emp2 = Employee.Employee('Saanvi','kandhati',3000)
emp3 = Employee.Employee('Supriya','Malla',4000)
emp4 = Employee.Employee('Sravan','Babu',2000)
#print(emp1.first)
#print(emp2.last)
#print(emp1.pay)
#c.execute("""insert into employees values(?,?,?)""",(emp2.first,emp2.last,emp2.pay))
def insert(emp4):
    with conn:
        c.execute
#c.execute("""insert into employees values(:f,:l,:p)""",{"f":emp3.first,"l":emp3.last,"p":emp3.pay})
c.execute("""select * from employees""")
print(c.fetchall())

conn.commit()

conn.close()
 
