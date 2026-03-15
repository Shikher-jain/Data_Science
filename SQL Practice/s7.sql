use flight_database;

select airline ,count(*) from flights group by airline;

select airline,avg(price),count(price)  from flights group by airline;

SELECT DISTINCT destination FROM flights;
SELECT DISTINCT source FROM flights;
SELECT source FROM flights union all SELECT destination FROM flights;
SELECT DISTINCT source FROM flights union SELECT DISTINCT destination FROM flights;

SELECT source, count(*) FROM (SELECT source FROM flights union all SELECT destination FROM flights) t group by t.source order by count(*) desc;
SELECT destination, count(*) FROM (SELECT destination FROM flights union all SELECT source  FROM flights) t group by t.destination order by count(*) desc;

