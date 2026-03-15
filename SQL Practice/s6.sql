use sqldb1;

create table user_logs(
id int auto_increment primary key,
user_id int,
name varchar(50),
created_on timestamp default current_timestamp
);

-- drop trigger after_user_insert;

DELIMITER $$
CREATE TRIGGER after_user_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_logs(user_id, name)
    VALUES(NEW.id, new.name);
END $$
DELIMITER ;

insert into users (name,email,gender,DOB,salary) values
('Alice1','Alice1@example.com','Male','2001-09-07',55000);

select * from users;
select * from user_logs;
