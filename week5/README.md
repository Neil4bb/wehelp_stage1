# Task 2

-  Create a new database named  website  . 
```sql

CREATE DATABASE website;

```
- Create a new table named  member  , in the  website  database,  designed as below
```sql
USE website;

CREATE TABLE member (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT DEFAULT 0 NOT NULL,
    time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);
```

![task2](task2.png)

---
# Task 3

- INSERT a new row to the member table where name, email and password must be set to  test ,  test@test.com , and  test . INSERT additional  4 rows with arbitrary data. 
```sql
mysql> USE website

mysql> INSERT INTO member (name, email, password)
    -> VALUES ('test', 'test@test.com', 'test');

mysql> INSERT INTO member (name, email, password)
    -> VALUES ('role1', 'role1@test.com', 'role1'),
    -> ('role2', 'role2@test.com', 'role2'),
    -> ('role3', 'role3@test.com', 'role3'),
    -> ('role4', 'role4@test.com', 'role4');
```
- SELECT all rows from the member table. 
```sql
mysql> SELECT * FROM member;
```
- SELECT all rows from the member table, in descending order of time.
```sql
mysql> SELECT * FROM member
    -> ORDER BY time DESC;
```
- SELECT total 3 rows, second to fourth, from the member table, in descending order of time.  Note: it does not mean SELECT rows where  id are 2, 3, or 4. 
```sql
mysql> SELECT * FROM member
    -> ORDER BY time DESC
    -> LIMIT 3 OFFSET 1;
```
- SELECT rows where email equals to  test@test.com . 
```sql
mysql> SELECT * FROM member
    -> WHERE email='test@test.com';
```
- SELECT rows where name includes the  es  keyword.
```sql
mysql> SELECT * FROM member
    -> WHERE name LIKE '%es%';
```
- SELECT rows where email equals to  test@test.com  and  password equals to  test . 
```sql
mysql> SELECT * FROM member
    -> WHERE email='test@test.com'
    -> AND password='test';
```
- UPDATE data in name column to  test2  where email equals  to  test@test.com . 
```sql
mysql> UPDATE member
    -> SET name='test2'
    -> WHERE email='test@test.com';
```
![task3-1](task3_1.png)
![task3-2](task3_2.png)
![task3-3](task3_3.png)
---
# Task 4
- SELECT how many rows from the member table. 
```sql
mysql> SELECT COUNT(*) AS number_of_rows FROM member;
```
- SELECT the sum of follower_count of all the rows from the member table.
```sql
mysql> SELECT SUM(follower_count) FROM member;
``` 
- SELECT the average of follower_count of all the rows from the member table. 
```sql
mysql> SELECT AVG(follower_count) FROM member;
```
- SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
```sql
mysql> SELECT AVG(follower_count) AS avgoffirst2
    -> FROM (
    ->  SELECT follower_count FROM member
    ->  ORDER BY follower_count DESC
    ->  LIMIT 2
    -> ) AS first2;
```
![task4-1](task4_1.png)
![task4-2](task4_2.png)
![task4-3](task4_3.png)
---
# Task 5
- Create a new table named  message  , in the  website  database.  designed as below
```sql
mysql> CREATE TABLE message (
    ->  id INT AUTO_INCREMENT PRIMARY KEY,
    ->  member_id INT NOT NULL,
    ->  content TEXT NOT NULL,
    ->  like_count INT DEFAULT 0 NOT NULL,
    ->  time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    ->  FOREIGN KEY (member_id) REFERENCES member(id)
    -> );
```
- SELECT all messages, including sender names. We have to JOIN the member table to get that.
```sql
mysql> SELECT
    ->  message.id,
    ->  message.member_id,
    ->  member.name AS sender,
    ->  message.content,
    ->  message.like_count,
    ->  message.time
    -> FROM message
    -> JOIN member
    -> ON message.member_id = member.id;
```
- SELECT all messages, including sender names, where sender email equals to test@test.com . We have to JOIN the member table to  filter and get that. 
```sql
mysql> SELECT
    ->  msg.id,
    ->  msg.member_id,
    ->  m.name AS sender,
    ->  msg.content,
    ->  msg.like_count,
    ->  msg.time
    -> FROM message msg
    -> JOIN member m
    -> ON msg.member_id = m.id
    -> WHERE m.email = 'test@test.com';
```
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender email equals to  test@test.com .
```sql
mysql> SELECT AVG(like_count)
    -> FROM message
    -> JOIN member
    -> ON message.member_id = member.id
    -> WHERE member.email = 'test@test.com';
```
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender email.
```sql
mysql> SELECT
    ->  member.email,
    ->  AVG(like_count) AS avg_likes
    -> FROM message
    -> JOIN member
    ->  ON message.member_id = member.id
    -> GROUP BY member.email;
```
![task5-1](task5_1.png)
![task5-2](task5_2.png)
![task5-3](task5_3.png)
![task5-4](task5_4.png)
![task5-5](task5_5.png)