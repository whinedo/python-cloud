
CREATE TABLE apirelease(
buildtime date,
version varchar(30) primary key,
links varchar2(30),
methods varchar2(30));


CREATE TABLE users(
    username varchar2(30),
    email varchar2(30),
    password varchar2(30),
    full_name varchar(30),
    id integer primary key autoincrement);

CREATE TABLE tweets(
    id integer primary key autoincrement,
    username varchar2(30),
    body varchar2(30),
    tweet_time date);