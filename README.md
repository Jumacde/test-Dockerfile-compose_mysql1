# test-Dockerfile-compose_mysql1
Convert a Docker setup that was only done via CLI into an equivalent Dockerfile and docker-compose.yml.
source: https://www.youtube.com/watch?v=Rb3nhOCxUhM&list=PL714lzee826o4L1sHGQkSoyKFzpSTGUmF&index=2

original docker cli command:
1. create a container by mysql
  sudo docker run --name mysql-test -e MYSQL_ROOT_PASSWORD=pass -d -p 13306:3306 mysql
2. login in mysql
 a. sudo docker exec  -it mysql-test bash
 b. mysql -u root -p
 -- input password --
3. create a database
 a.CREATE DATABASE sampledb2 CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
 b. check the database
  SHOW DATABASES;
4. create a database
 a. CREATE TABLE users2 (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(255) UNIQUE,
create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
 b. check the table
SHOW TABLES;
5. insert data
 a. INSERT INTO users2(name, email) VALUEES
('Alice2', 'alice2@exmaple.com'),
('Bob2', 'bob2@exmaple.com');
 b. check data
SELECT * FORM users2;
6. exit from mysql
exit


