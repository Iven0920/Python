use world;

drop table student;

create table student(
    id int,
    name varchar(10),
    age int
);

# 插入数据 insert into 表[(列1, 列2,.....,列N)] values(值1, 值2,.....)[, (值1, 值2,.....), (值1, 值2,.....)]
insert into student(id) values(1), (2), (3);

# 字符串只支持单引号
insert into student(id, name, age) values(4, 'Iven', 11), (5, 'rosen', 21), (6, 'starry', 41);

# []代表可省略 全部列插入 输入数据顺序保持一样
insert into student values(7, 'bob', 11), (8, 'alen', 21);

# 数据删除 delete from 表名称 (where 条件判断) 不选where则全部删除
delete from student where id = 1;
delete from student where id < 4;
delete from student where id > 6;

delete from student where age = 21;

delete from student ;

# 数据更新 update 表名 set 列=值 [where 条件判断]
update student set name = 'Ivennn' where id = 4;
# 不选where则全部更新
update student set name = 'Ivennn';