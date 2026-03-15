use sqldb1;
show tables;

select * from users;
select * from admin_users;
select * from addresses;

create table jointest(
id int auto_increment primary key,
name varchar(50),
email varchar(50),
manager_id int

);

INSERT INTO jointest (name, email, manager_id) VALUES
('Aditi', 'aditi@company.com', NULL),      -- CEO (no manager)
('Rohit', 'rohit@company.com', 1),          -- Manager under Aditi
('Shikher', 'shikher@company.com', 1),      -- Manager under Aditi
('Mohit', 'mohit@company.com', 2),          -- Employee under Rohit
('Karan', 'karan@company.com', 2),          -- Employee under Rohit
('Neha', 'neha@company.com', 3),            -- Employee under Shikher
('Priya', 'priya@company.com', 3);          -- Employee under Shikher


select * from jointest;

select j1.id, j1.name,j1.email,j2.id as manager_id,j2.name as manager_name, j2.email as manager_email from jointest as j1
left join 
jointest as j2
on j2.id = j1.manager_id;
