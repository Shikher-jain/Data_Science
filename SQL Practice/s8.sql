use laptopDB;

select * from laptop;

select gpu_brand,count(*) from laptop
-- where Company = 'HP'
group by gpu_brand having gpu_brand != 'ARM' ;

select Company,count(*) as Total_phones from laptop
-- where Company = 'HP'
group by Company having count(*) > 20
order by Total_phones;