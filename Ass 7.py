ASSIGNMENT NO: 7
Problem statement: Write a PL/SQL Stored Procedure and Stored Function for different applications.

create table student(roll_no number,name varchar(20),class varchar(20),marks number);
Table created.
SQL> insert into student values(101,'jadhav saurabh','SE comp',1600);
1 row created.
SQL> ed
Wrote file afiedt.buf
66
q
  1* insert into student values(102,'jadhav amar','TE comp',990);
  2  /
SQL> insert into student values(102,'amar chavan','TE comp',880);
1 row created.
SQL> insert into student values(103,'sonali gaikwad','SE comp',556);

1 row created.
SQL> insert into student values(104,'ruturaj saha','TE comp',789);
1 row created.
SQL> select * from student;
   ROLL_NO NAME         CLASS              MARKS
---------- -------------------- -------------------- ----------
       101 jadhav saurabh    SE comp            1600
       102 amar chavan        TE comp             880
       103 sonali gaikwad    SE comp             556
       104 ruturaj saha     TE comp             789


SQL> create table result2(roll number,name varchar(20),class varchar(20),grade varchar(20));

Table created.

WITH PROCEDURE:

SQL> ed
Wrote file afiedt.buf
24
q
  1  declare
  2  roll_no1 number;
  3  marks1 varchar(20);
  4  name1 varchar(20);
  5  class1 varchar(20);
  6  grade varchar(20);
  7  procedure prc_grade(marks in number,grade out varchar) as
  8  begin
  9  if(marks<=1500 and marks>=990 ) then
 10  grade:='distinction';
 11  else
 12  if(marks<=989 and marks>=900) then
 13  grade:='first class';
 14  else
 15  if(marks<=899 and marks>=825) then
 16  grade:='second class';
 17  end if;
 18  end if;
 19  end if;
 20  end;
 21  begin
 22  roll_no1:='&roll_no1';
 23  marks1:='&marks1';
 24  select roll_no,name,class,marks into roll_no1,name1,class1,marks1 from student where roll_no=roll_no1 and marks=marks1;
 25  prc_grade(marks1,grade);
 26  insert into result2 values(roll_no1,name1,class1,grade);
 27* end;
 28  /
Enter value for roll_no1: 102
old  22: roll_no1:='&roll_no1';
new  22: roll_no1:='102';
Enter value for marks1: 880
old  23: marks1:='&marks1';
new  23: marks1:='880';

PL/SQL procedure successfully completed.

SQL> select * from result2;

      ROLL NAME         CLASS             GRADE
---------- -------------------- -------------------- --------------------
       101 jadhav saurabh    SE comp
       102 amar chavan        TE comp          second class

WITH FUCTION:

SQL> ed
Wrote file afiedt.buf
707
q
  1  declare
  2  roll_no1 number;
  3  marks1 varchar(20);
  4  name1 varchar(20);
  5  class1 varchar(20);
  6  grade varchar(20);
  7  d varchar(20);
  8  function prc_grade(marks in number,grade out varchar) return varchar as
  9  begin
 10  if(marks<=1500 and marks>=990 ) then
 11  grade:='distinction';
 12  return grade;
 13  else
 14  if(marks<=989 and marks>=900) then
 15  grade:='first class';
 16  return grade;
 17  else
 18  if(marks<=899 and marks>=825) then
 19  grade:='second class';
 20  return grade;
 21  end if;
 22  end if;
 23  end if;
 24  end;
 25  begin
 26  roll_no1:='&roll_no1';
 27  marks1:='&marks1';
 28  select roll_no,name,class,marks into roll_no1,name1,class1,marks1 from student where roll_no=roll_no1 and marks=marks1;
 29  d:=prc_grade(marks1,grade);
 30  insert into result2 values(roll_no1,name1,class1,d);
 31* end;
 32  /
Enter value for roll_no1: 102
old  26: roll_no1:='&roll_no1';
new  26: roll_no1:='102';
Enter value for marks1: 880
old  27: marks1:='&marks1';
new  27: marks1:='880';

PL/SQL procedure successfully completed.

SQL> select * from result2;

      ROLL NAME         CLASS             GRADE
---------- -------------------- -------------------- --------------------
       101 jadhav saurabh    SE comp
       102 amar chavan        TE comp          second class
       102 amar chavan        TE comp          second class

