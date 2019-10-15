--1. List the following details of each employee: employee number, last name, first name, gender, and salary.
select employees.emp_no,last_name,first_name,gender,salary
from employees
inner join salaries
on salaries.emp_no = employees.emp_no


--2. List employees who were hired in 1986.
select * from employees where EXTRACT(year FROM hire_date)=1986

--3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

select dept_manager.dept_no,dept_name,dept_manager.emp_no,first_name,last_name,hire_date,to_date as empl_end_date from dept_manager
inner join employees on 
employees.emp_no = dept_manager.emp_no
inner join departments on
departments.dept_no = dept_manager.dept_no


--4. List the department of each employee with the following information: employee number, last name, first name, and department name.

select employees.emp_no,last_name,first_name,dept_name from employees
inner join dept_emp
on dept_emp.emp_no=employees.emp_no
inner join departments
on departments.dept_no=dept_emp.dept_no

--5. List all employees whose first name is "Hercules" and last names begin with "B."


select * from employees where first_name='Hercules' and last_name like 'B%'

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

select employees.emp_no,last_name,first_name,dept_name from departments
inner join dept_emp on 
dept_emp.dept_no = departments.dept_no
inner join employees on 
employees.emp_no = dept_emp.emp_no
where dept_name='Sales'


-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

select employees.emp_no,last_name,first_name,dept_name from departments
inner join dept_emp on 
dept_emp.dept_no = departments.dept_no
inner join employees on 
employees.emp_no = dept_emp.emp_no
where dept_name='Sales' or dept_name='Development'


--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

select count(last_name) as counter, last_name from employees
group by 2 order by 1 desc

