-- CS4400: Introduction to Database Systems (Fall 2022)

-- Phase II: Create Table & Insert Statements [v0] Tuesday, November, 2022 @ 5:00 PM (Local/EDT)

-- Team __56

-- Team Member Name (GT username)rfladell3

-- Team Member Name (GT username)blee444

-- Team Member Name (GT username)pholland7

-- Team Member Name (GT username)spanse9

-- Directions:

-- Please follow all instructions for Phase II as listed on Canvas.

-- Fill in the team number and names and GT usernames for all members above.

-- Create Table statements must be manually written, not taken from an SQL Dump file.

-- This file must run without error for credit.

-- ------------------------------------------------------

-- CREATE TABLE STATEMENTS AND INSERT STATEMENTS BELOW

-- ------------------------------------------------------


DROP DATABASE IF EXISTS phase2;
CREATE DATABASE IF NOT EXISTS phase2;
USE phase2;

DROP TABLE IF EXISTS user;
CREATE TABLE user (
  username char(40) NOT NULL,
  fname char(100),
  lname char(100),
  address varchar(500), 
  birthdate date,
  PRIMARY KEY (username)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS employee;
CREATE TABLE employee (
  username char(40) NOT NULL,
  taxID varchar(11) NOT NULL,
  hired date, 
  experience decimal,
  salary decimal, 
  PRIMARY KEY (username, taxID),
  CONSTRAINT FK1 FOREIGN KEY (username) REFERENCES user (username)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS owner;
CREATE TABLE owner (
  username char(40) NOT NULL,
  PRIMARY KEY (username),
  CONSTRAINT FK2 FOREIGN KEY (username) REFERENCES user (username)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS pilot;
CREATE TABLE pilot (
  username char(40) NOT NULL,
  taxID varchar(11) NOT NULL,
  license_type char(100),
  experience decimal,
  PRIMARY KEY (username, taxID),
  CONSTRAINT FK3 FOREIGN KEY (username, taxID) REFERENCES employee (username, taxID)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS worker;
CREATE TABLE worker (
  username char(40) NOT NULL,
  taxID varchar(11) NOT NULL,
  PRIMARY KEY (username, taxID),
  CONSTRAINT FK4 FOREIGN KEY (username, taxID) REFERENCES employee (username, taxID)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS ingredient;
CREATE TABLE ingredient (
  barcode varchar(40) NOT NULL,
  iname char(100),
  weight integer,
  PRIMARY KEY (barcode)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS location;
CREATE TABLE location (
  label char(40) NOT NULL,
  x_coord decimal,
  y_coord decimal, 
  space decimal,
  UNIQUE KEY (x_coord, y_coord),
  PRIMARY KEY (label)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS service;
CREATE TABLE service (
  label char(40) NOT NULL,
  ID char(40) NOT NULL,
  name char(100),
  PRIMARY KEY (label, ID),
  CONSTRAINT FK5 FOREIGN KEY (label) REFERENCES location (label)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS restaurant;
CREATE TABLE restaurant (
  label char(40) NOT NULL,
  name char(40) NOT NULL,
  spent decimal,
  rating integer,
  PRIMARY KEY (label, name),
  UNIQUE KEY (name),
  CONSTRAINT FK6 FOREIGN KEY (label) REFERENCES location (label)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS fund;
CREATE TABLE fund (
  username char(40) NOT NULL,
  label char(40) NOT NULL,
  name char(40) NOT NULL,
  invested decimal,
  dt_made date,
  PRIMARY KEY (username, label, name),
  CONSTRAINT FK8 FOREIGN KEY (username) REFERENCES owner (username),
  CONSTRAINT FK9 FOREIGN KEY (label, name) REFERENCES restaurant (label, name)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS manage;
CREATE TABLE manage (
  username char(40) NOT NULL,
  worker_id varchar(11) NOT NULL,
  service_label char(40) NOT NULL,
  ID char(40) NOT NULL,
  PRIMARY KEY (username, worker_id, service_label, ID), 
  CONSTRAINT FK15 FOREIGN KEY (username, worker_id) REFERENCES worker (username, taxID),
  CONSTRAINT FK16 FOREIGN KEY (service_label, ID) REFERENCES service (label, ID)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS work_for;
CREATE TABLE work_for (
  username char(40) NOT NULL,
  taxID varchar(11) NOT NULL,
  service_label char(40) NOT NULL,
  ID char(40) NOT NULL,
  PRIMARY KEY (username, taxID, service_label, ID),
  CONSTRAINT FK17 FOREIGN KEY (username, taxID) REFERENCES worker (username, taxID),
  CONSTRAINT FK18 FOREIGN KEY (service_label, ID) REFERENCES service (label, ID)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS drone;
CREATE TABLE drone (
  label char(40) NOT NULL,
  ID char(40) NOT NULL,
  tag decimal NOT NULL,
  fuel decimal, 
  capacity decimal,
  sales decimal,
  hover char(40) NOT NULL,
  control char(40),
  swarm_tag decimal,
  swarm_ID char(40),
  PRIMARY KEY (ID, tag),
  CONSTRAINT FK7 FOREIGN KEY (label, ID) REFERENCES service (label, ID)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS contain;
CREATE TABLE contain (
  barcode varchar(40) NOT NULL,
  ID char(40) NOT NULL,
  tag decimal NOT NULL,
  price decimal, 
  quantity decimal,
  PRIMARY KEY (barcode, ID, tag),
  CONSTRAINT FK10 FOREIGN KEY (barcode) REFERENCES ingredient (barcode),
  CONSTRAINT FK11 FOREIGN KEY (ID, tag) REFERENCES drone (ID, tag)
) ENGINE=InnoDB;

ALTER TABLE drone ADD CONSTRAINT fk12 FOREIGN KEY (hover) REFERENCES location (label);
ALTER TABLE drone ADD CONSTRAINT fk13 FOREIGN KEY (control) REFERENCES pilot (username);
ALTER TABLE drone ADD CONSTRAINT fk14 FOREIGN KEY (swarm_ID, swarm_tag) REFERENCES drone (ID, tag);

insert into user values
("agarcia7", "Alejandro", "Garcia", "710 Living Water Drive", "1966-10-29"),
("awilson5", "Aaron", "Wilson", "220 Peachtree Street", "1963-11-11"),
("bsummers4", "Brie", "Summers", "5105 Dragon Star Circle", "1976-02-09"),
("cjordan5", "Clark", "Jordan", "77 Infinite Stars Road", "1966-06-05"),
("ckann5", "Carrot", "Kann", "64 Knights Square Trail", "1972-09-01"),
("csoares8", "Claire", "Soares", "706 Living Stone Way", "1965-09-03"),
("echarles19", "Ella", "Charles", "22 Peachtree Street", "1974-05-06"),
("eross10", "Erica", "Ross", "22 Peachtree Street", "1975-04-02"),
("fprefontaine6", "Ford", "Prefontaine", "10 Hitch Hikers Lane", "1961-01-28"),
("hstark16", "Harmon", "Stark", "53 Taker Top Lane", "1971-10-27"),
("jstone5", "Jared", "Stone", "101 Five Finger Way", "1961-01-08"),
("lrodriguez5", "Lina", "Rodriquez", "360 Corkskrew Circle", "1975-04-02"),
("mrobot1", "Mister", "Robot", "10 Autonomy Trace", "1988-11-02"),
("mrobot2", "Mister", "Robot", "10 Clone Me Circle", "1988-11-02"),
("rlopez6", "Radish", "Lopez", "8 Queens Route", "1999-09-03"),
("sprince6", "Sarah", "Prince", "22 Peachtree Street", "1968-06-15"),
("tmccall5", "Trey", "McCall", "360 Corkscrew Circle", "1973-03-19");

insert into employee values
("agarcia7", "999-99-9999", "2019-03-17", 24, 41000),
("awilson5", "111-11-1111", "2020-03-15", 9, 46000),
("bsummers4", "000-00-0000", "2018-12-06", 17, 35000),
("ckann5", "640-81-2357", "2019-08-03", 27, 46000),
("csoares8", "888-88-8888", "2019-02-25", 26, 57000),
("echarles19", "777-77-7777", "2021-01-02", 3, 27000),
("eross10","444-44-4444", "2020-04-17", 10, 61000),
("fprefontaine6", "121-21-2121", "2020-04-19", 5, 20000),
("hstark16", "555-55-5555", "2018-07-23", 20, 59000),
("lrodriguez5", "222-22-2222", "2019-04-15", 20, 58000),
("mrobot1", "101-01-0101", "2015-05-27", 8, 38000),
("mrobot2", "010-10-1010", "2015-05-27", 8, 38000),
("rlopez6", "123-58-1321", "2017-02-05", 51, 64000),
("tmccall5", "333-33-3333", "2018-10-17", 29, 33000);

INSERT INTO ingredient values
('bv_4U5L7M', 'balsamic vinegar', 4),
('clc_4T9U25X', 'caviar', 5),
('ap_9T25E36L', 'foie gras', 4),
('pr_3C6A9R', 'prosciutto',	6), 
('ss_2D4E6L', 'saffron', 3), 
('hs_5E7L23M', 'truffles', 3);

insert into pilot values ("agarcia7", "999-99-9999", "610623", 38);
insert into pilot values ("awilson5", "111-11-1111", "314159", 41);
insert into pilot values ("bsummers4", "000-00-0000", "411911", 35);
insert into owner values ("cjordan5");
insert into worker values ("ckann5", "640-81-2357");
insert into pilot values ("csoares8", "888-88-8888", "343563", 7);
insert into worker values ("csoares8", "888-88-8888");
insert into pilot values ("echarles19", "777-77-7777", "236001", 10);
insert into worker values ("echarles19", "777-77-7777");
insert into worker values ("eross10", "444-44-4444");
insert into pilot values ("fprefontaine6", "121-21-2121", "657483", 2);
insert into worker values ("hstark16", "555-55-5555");
insert into owner values ("jstone5");
insert into pilot values ("lrodriguez5", "222-22-2222", "287182", 67);
insert into pilot values ("mrobot1", "101-01-0101", "101010", 18);
insert into worker values ("mrobot2", "010-10-1010");
insert into pilot values ("rlopez6", "123-58-1321", "235711", 58);
insert into owner values ("sprince6");
insert into pilot values ("tmccall5", "333-33-3333", "181633", 10);
insert into worker values ("tmccall5", "333-33-3333");

INSERT INTO location VALUES
("plaza", (-4), (-3), 10),
("buckhead", 7, 10, 8),
("avalon", 2, 15, NULL),
("mercedes", (-8), 5, NULL),
("midtown", 2, 1, 7),
("southside", 1, (-16), 5),
('highpoint', 11, 3, 4),
('airport', 5, (-6), 15);

INSERT INTO restaurant VALUES
("plaza", "Bishoku", 10, 5),
("plaza", "Casi Cielo", 30, 5),
("buckhead", "Ecco", 0, 3),
("buckhead", "Fogo de Chao", 30, 4),
("avalon", "Hearth", 0, 4),
("mercedes", "Il Giallo", 10, 4),
("midtown", "Lure", 20, 5),
("southside", "Micks", 0, 2),
("midtown", "South City Kitchen", 30, 5),
("plaza", "Tre Vele", 10, 4);

INSERT INTO service VALUES
('southside','hf','Herban Feast'),
('southside', 'osf', 'On Safari Foods'),
('avalon', 'rr', 'Ravishing Radish');

INSERT INTO fund VALUES
("jstone5", "buckhead", "Ecco", 20, "2022-10-25"),
("sprince6", "mercedes", "Il Giallo", 10, "2022-03-06"),
("jstone5", "midtown", "Lure", 30, "2022-09-08"),
("jstone5", "midtown", "South City Kitchen", 5, "2022-07-25");

INSERT INTO drone values ( 'avalon', 'rr', 3, 100, 5, 50, 'avalon', 'agarcia7', NULL, NULL);
INSERT INTO drone values ( 'avalon', 'rr', 7, 53, 5, 100, 'avalon', 'agarcia7', NULL, NULL);
INSERT INTO drone values ( 'southside' , 'hf', 16, 17, 5, 40, 'buckhead', 'fprefontaine6', NULL, NULL);
INSERT INTO drone values ( 'avalon', 'rr', 8, 100, 6, 0, 'highpoint', 'agarcia7', NULL, NULL);
INSERT INTO drone values ( 'avalon', 'rr', 11, 90, 6, 0, 'highpoint', NULL, 8, 'rr');
INSERT INTO drone values ( 'southside', 'osf', 1, 100, 9, 0, 'airport', 'awilson5',	NULL, NULL);
INSERT INTO drone values ( 'southside' , 'hf', 8, 100, 8, 0, 'southside', 'bsummers4', null, null);
INSERT INTO drone values ( 'southside' , 'hf', 1, 100, 6, 0, 'southside', 'fprefontaine6', null, null);
INSERT INTO drone values ( 'southside' , 'osf', 2, 75, 7, 0, 'airport', NULL, 1, 'osf');
INSERT INTO drone values ( 'southside' , 'hf', 5, 27, 7, 100, 'buckhead', 'fprefontaine6', null, null);
INSERT INTO drone values ( 'southside' , 'hf', 11, 25, 10, 0, 'buckhead', NULL, 5, 'hf');

INSERT INTO contain values
('clc_4T9U25X', 'rr', 3, 28, 2),
('clc_4T9U25X',	'hf', 5, 30, 1), 
('pr_3C6A9R', 'osf', 1, 20, 5), 
('pr_3C6A9R', 'hf',	8, 18, 4),
('ss_2D4E6L', 'osf', 1, 23, 3),
('ss_2D4E6L', 'hf', 11, 19, 3),
('ss_2D4E6L', 'hf', 1, 27, 6),
('hs_5E7L23M', 'osf', 2, 14, 7),
('hs_5E7L23M', 'rr', 3, 15, 2),
('hs_5E7L23M', 'hf', 5, 17, 4);

Insert INTO manage values ('hstark16', "555-55-5555", 'southside', 'hf' );
Insert INTO manage values ('eross10', "444-44-4444", 'southside', 'osf');
Insert INTO manage values ('echarles19', "777-77-7777", 'avalon', 'rr');

INSERT INTO work_for values
('ckann5', '640-81-2357', 'southside', 'osf'),
('echarles19', '777-77-7777', 'avalon', 'rr'),
('eross10', '444-44-4444', 'southside', 'osf'),
('hstark16', '555-55-5555', 'southside', 'hf'),
('tmccall5', '333-33-3333', 'southside', 'hf');

