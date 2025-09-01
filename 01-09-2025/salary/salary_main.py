from salary_manager import create_salary, read_all, read_by_salary
from salary_manager import salaries, update, delete_by_salary
create_salary(1000)
create_salary(5000)
create_salary(8000)
create_salary(3000)
result_salaries = read_all()
for salary in result_salaries:
    print(salary)

print(read_by_salary(8000)) #2
print(read_by_salary(4000)) #-1
print(salaries[read_by_salary(8000)]) #8000

update(8000, 8500) 
print(read_all())
delete_by_salary(1000)
print(read_all())
