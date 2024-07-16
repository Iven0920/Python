# 分组聚合
# select 字段|聚合函数 from 表 [where 条件] group by 列
# 聚合函数：sum(列), avg(列), min(列), max(列), count(列|*)
# select后非聚合函数只能有跟group by一样的对象 聚合函数无限制
select gender, avg(age), sum(age), min(age), max(age), count(*) from student group by gender;