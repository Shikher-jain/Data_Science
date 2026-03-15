use sqldb1;

select * from users;
select * from users where salary > (select avg(salary) from users);

select * from users where id in (1,3);
select avg(salary) from users;
select * from users where id in (select id from users where salary > (select avg(salary) from users));

select name, salary, (select avg(salary) from users) as avg_salary from users;
-- select gender,name, salary, (select avg(salary) from users) as avg_salary from users group by gender;
SELECT gender, AVG(salary) AS avg_salary,count(*) as count
FROM users
GROUP BY gender;

SELECT gender, AVG(salary) AS avg_salary,count(*) as count
FROM users
GROUP BY gender
HAVING avg(salary) > 50000;
