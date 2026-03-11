CREATE DATABASE Company;
USE Company;

CREATE TABLE Candidate(
candidateID int primary key, 
candidateName varchar(20) not null, 
candidateEmail varchar(20) not null,
candidateAddress varchar(20) not null
);

CREATE TABLE Position(
positionCode int primary key,
positionName varchar(10) not null,
positionType varchar(10) not null,
positionDuration date not null,
candidateID int,
orgId int
);

CREATE TABLE Skill(
skillCode int primary key,
skillType varchar(10) not null,
skillLevel varchar(5) not null
);

CREATE TABLE Organization(
orgId int primary key,
orgName varchar(20) not null,
orgURL varchar(30) not null,
orgAddress varchar(20) not null);


CREATE TABLE candidate_skill(
candidateID int not null,
skillCode int
);

CREATE TABLE Position_skill(
positionCode int,
skillCode int
);

ALTER TABLE Position
ADD FOREIGN KEY(candidateID) REFERENCES Candidate(candidateID),
ADD FOREIGN KEY(orgId) REFERENCES Organization(orgId);

ALTER TABLE candidate_skill
ADD FOREIGN KEY(candidateID) REFERENCES Candidate(candidateID),
ADD FOREIGN KEY(skillCode) REFERENCES Skill(skillCode),
ADD PRIMARY KEY (candidateID, skillCode);

ALTER TABLE Position_skill
ADD FOREIGN KEY(skillCode) REFERENCES Skill(skillCode),
ADD FOREIGN KEY(positionCode) REFERENCES Position(positionCode),
ADD PRIMARY KEY (positionCode, skillCode);
