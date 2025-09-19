from models import Employee
from storage import save_all, load_all
from csv_storage import save_all_csv, load_all_csv 

emp1 = Employee(id=1, name="Marko Marković", department="IT", salary=1200.50)
emp2 = Employee(id=2, name="Ana Anić", department="HR", salary=950.00)
emp3 = Employee(id=3, name="Jovan Jović", department="Finance", salary=1500.75)

save_all([emp1, emp2, emp3])
save_all_csv([emp1, emp2, emp3])

employees = load_all()
employees_csv = load_all_csv()
for e in employees:
    print(e)

for e in employees_csv:
    print(e)