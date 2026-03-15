use sqldb1;
delimiter $$
create procedure AddUsers(
    in p_name varchar(100),
    in p_email varchar(100),
    in p_gender enum('Male','Female','Other'),
    in p_DOB date,
    in p_salary int
)
begin
    insert into users (name,email,gender,DOB,salary)
    values(p_name,p_email,p_gender,p_DOB,p_salary);

    select * from users;
end $$
delimiter ;

call AddUsers('Amit','amit@example.com','Male','2004-06-08',90000);
select * from users; 

show procedure status where Db = 'sqldb1';