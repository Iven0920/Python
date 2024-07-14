# 注释：1.单行注释 -- 注释 2.单行注释 # 注释 3.多行注释 /* 注释/*
-- 注释1
# 注释2
/*
 我
 是
 注释
*/

# SQL语言特点：大小写不敏感， ;结尾
# 查看数据库 show databases
show databases;

# 使用数据库 use 数据库名称
use world;

# 查看当前数据库 select database();
select database();

# 创建数据库 create database test [charset UTF8] []内可选编码格式
create database test charset utf8;
show databases;

# 删除数据库 drop database 数据库名称
drop database test;
show databases;


use world;
# 查看表 show tables;
show tables;

# 创建表 create table 表名称(列名称 列类型,列名称 列类型,......)
-- 列类型: 1.int 2.float 3.varchar(长度) 文本，长度为数字，做最大长度限制（py中的字符串） 4.date 日期类型 5.timesleep  时间戳类型
create table student(
    id int,
    name varchar(10),
    age int
);

# 删除表 drop table 表名称; drop table if exists 表名称;
drop table student;
