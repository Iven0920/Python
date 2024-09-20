create table student(
    id int,
    name varchar(10),
    age int,
    gender varchar(10)
);

INSERT INTO student VALUES(10001, '周杰轮', 31, '男'), (10002, '王力鸿', 33, '男'), (10003, '蔡依琳', 35, '女'), (10004, '林志灵', 36, '女'), (10005, '刘德滑', 33, '男'), (10006, '张大山', 10, '男'), (10007, '刘志龙', 11, '男'), (10008, '王潇潇', 33, '女'), (10009, '张一梅', 20, '女'), (10010, '王一倩', 13, '女'), (10011, '陈一迅', 31, '男'), (10012, '张晓光', 33, '男'), (10013, '李大晓', 15, '男'), (10014, '吕甜甜', 36, '女'), (10015, '曾悦悦', 31, '女'), (10016, '刘佳慧', 21, '女'), (10017, '项羽凡', 23, '男'), (10018, '刘德强', 26, '男'), (10019, '王强强', 11, '男'), (10020, '林志慧', 25, '女');

# select 字段列表 |* from 表 [where 条件判断]
# 从表中，选择某些列进行展示
select id, name from student;
select id, name, age, gender from student;
# * 代表查询所有
select * from student;
select * from student where age > 20;
select * from student where gender = '男';