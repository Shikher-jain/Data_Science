use sqldb1;
show indexes from manager_RW;
show indexes from users;
show indexes from addresses;
show indexes from admin_users;

create index idx_email on users(email);
create index idx_email_gender on users(email,gender);

select * from admin_users
where gender = 'Female' and salary > 70000;

drop index idx_email on users;

