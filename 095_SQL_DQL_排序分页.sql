# 结果排序 对某一列进行排序
# select 列|聚合函数|* from 表 order by ...[asc| desc]默认升序
select * from student where age > 20;
select * from student where age > 20 order by age asc;
select * from student where age > 20 order by age desc;

# 结果分页限制
# select 列|聚合函数|* from 表 limit n[, m]
select * from student limit 5;
# 跳过前10条从第11条开始 取5个
select * from student limit 10, 5;

# 综合使用 执行顺序不可变 select from必写 其他可省略
# select 列|聚合函数|* from 表 where... group by... order by ...[asc| desc] limit n[, m]...
select age, count(*) from student where age > 20 group by age;
select age, count(*) from student where age > 20 group by age 
order by age;
select age, count(*) from student where age > 20 group by age 
order by age limit 3;