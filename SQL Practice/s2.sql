create view manager_RW as
select j1.id, j1.name,j1.email,j2.id as manager_id,j2.name as manager_name, j2.email as manager_email from jointest as j1
left join 
jointest as j2
on j2.id = j1.manager_id;

drop view manager_RW;
select * from manager_RW;

CREATE OR REPLACE VIEW manager_RW AS
SELECT * FROM jointest;

SELECT * FROM manager_RW;
SELECT * FROM jointest;
