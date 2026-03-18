CREATE DATABASE Company;
USE Company;
--Creating all the three tables
CREATE TABLE Branch(
     branch_id      VARCHAR(8),
     street_address VARCHAR(50) NOT NULL,
     postal_code    VARCHAR(10) NOT NULL,
     city           VARCHAR(50) NOT NULL,
     state_province VARCHAR(50) NOT NULL,
     country        VARCHAR(50) NOT NULL,
     CONSTRAINT b_bid_pk PRIMARY KEY (branch_id)
);

CREATE TABLE Job(
	job_id  		INT(6),
	job_title		VARCHAR(50)NOT NULL,
	min_salary		DECIMAL(8,2) NOT NULL,
	max_salary		DECIMAL(8,2) NOT NULL,
	CONSTRAINT 	j_jid_pk PRIMARY KEY (job_id)
);

CREATE TABLE Staff(
	staff_id 	     INT(6),
	first_name 	VARCHAR(50) NOT NULL,
	last_name 		VARCHAR(50) NOT NULL,
	email 		VARCHAR(50) UNIQUE NOT NULL,
	phone_number 	VARCHAR(15),
	hire_date 		TIMESTAMP NOT NULL,
	salary 		DECIMAL(8,2) NOT NULL,
	job_id 		INT(6) NOT NULL,
     branch_id   	VARCHAR(8),
	CONSTRAINT 	s_sid_pk PRIMARY KEY (staff_id),
	CONSTRAINT 	s_jid_fk FOREIGN KEY (job_id)
	references 	Job(job_id),
     CONSTRAINT  	s_bid_fk FOREIGN KEY (branch_id) 
     references       Branch(branch_id)
);

--Populating all the tables
INSERT INTO Branch (branch_id, street_address, postal_code, city, state_province, country) 
VALUES 
('B100', '6 Osprey Way ', ' E2 7HT', 'London', 'Greater London', 'UK'),
('B200', ' 32 Falcon Road', ' TS1 8GE', 'Swansea', 'Swansea County', 'UK'),
('B300', '26 Trigg Street', ' NW1 4BF', 'Ironbridge', 'Sussex', 'UK'),
('B400', '11 Malcom Close', 'CG1 2SR', 'Cambridge', 'Cambridgeshire', 'UK');

INSERT INTO Job (job_id, job_title, min_salary, max_salary)
VALUES
(301, 'Managing Director', 75000, 125000),
(302, 'Clerical Administrator', 28000, 41000),
(303, 'System Analyst', 45000, 95000),
(304, 'Security Officer', 30000, 55000),
(305, 'Network Operator', 37000, 68000),
(306, 'Data Entry Operator', 24000, 50000),
(307, 'Insurance Rep', 30000, 60000);

INSERT INTO Staff (staff_id, first_name, last_name, email, phone_number, hire_date, salary, 
  branch_id, job_id)
VALUES 
(101, 'Jane', 'Smith', 'js@br.com', '02079111001', '2011-01-21', 98000,'B100', 301),
(102, 'Emma', 'Doe', 'ed@br.com', '02079111002', '2012-02-05', 99000,'B200', 301),
(103, 'Jen', 'Moring', 'jm@br.com', '02079111003', '2014-11-23', 79000, NULL, 303),
(104, 'Mike', 'Gills', 'mg@br.com', '02079111004', '2013-10-06', 51000, 'B200', 304),
(105, 'Nadia', 'Tamsin', 'nt@br.com', '02079111005', '2013-10-08', 62000, 'B300', 305),
(106, 'Mo', 'Backer', 'mb@br.com', '02079111006', '2015-11-24', 41000, 'B400',307),
(107, 'Luke', 'Defo', 'ld@br.com', '02079111007', '2016-05-15', 38000, 'B100', 302),
(108, 'Manu', 'Thomas', 'mt@br.com', '02079111008', '2017-08-12', 33000, NULL, 302),
(109, 'Marc', 'Daniel', 'md@br.com', '02079111009', '2014-01-02', 35000, 'B300', 307),
(110, 'Louise','Tamos', 'lt@br.com', '02079111010', '2017-11-05', 53000, 'B200', 306),
(111, 'Tim', 'Norman', 'tn@br.com', NULL , '2012-03-30', 35000, 'B100', 306);


-- Question 1.1 
SELECT * FROM Staff;

--Question 1.2 
SELECT staff_id, first_name, last_name FROM Staff;

--Question 1.3 
SELECT branch_id FROM Staff
WHERE branch_id IS NOT NULL;

--Question 1.4
SELECT DISTINCT branch_id FROM Staff;

--Question 1.5 
SELECT staff_id, first_name, last_name 
WHERE branch = NULL;

--Question 1.6
SELECT * FROM Staff
WHERE last_name = "Norman";

--Question 1.7
SELECT first_name, last_name, job_id, hire_date
WHERE last_name = "Smith" OR last_name = "Thomas";

--Question 1.8
SELECT last_name, job_id, hire_date FROM Staff
WHERE last_name = "Smith" OR last_name = "Thomas"
ORDER BY hire_date;

-- Question 1.9

SELECT last_name, job_id, hire_date, salary FROM Staff
WHERE branch_id = "B100";

--Question 1.10 
SELECT last_name FROM Staff
WHERE last_name LIKE "_o%";

--Question 1.11
SELECT last_name FROM Staff
WHERE last_name LIKE '%a%' AND last_name LIKE '%e%';

--Question 1.12
SELECT last_name, hire_date FROM Staff
WHERE hire_date >= '2017-01-01' AND hire_date < '2018-01-01';

--Question 1.13
SELECT last_name, salary FROM Staff
WHERE salary > 30000 AND salary < 40000;

--Question 1.14
SELECT last_name AS "Staff", salary AS "Monthly Salary" FROM Staff
WHERE salary BETWEEN 30000 AND 40000;

--Question 1.15
SELECT first_name || ' ' || last_name AS full_name, job_id, hire_date, salary FROM Staff
WHERE branch_id = 'B100' AND salary > 50000;

--Question 1.16
SELECT last_name, job_id, salary FROM employees
WHERE job_id IN (302, 307) AND salary NOT IN (33000, 34000);

--Question 1.17
SELECT first_name ||' '|| last_name AS full_name, job_id, hire_date, salary FROM Staff
WHERE branch_id == "B300" OR salary > 50000;

--Question 1.18
SELECT last_name, job_id, salary FROM Staff
WHERE branch_id = "B200" OR B300 AND salary IN(30000, 40000);

--Question 1.19
SELECT last_name, job_id, hire_date, salary FROM Staff
WHERE branch_id = "B200" AND hire_date < '2016-01-20';

--Question 1.20 
SELECT last_name, job_id, hire_date, salary FROM Staff
WHERE branch_id = "B200" AND hire_date = '2016-01-20' AND salary > 40000;
