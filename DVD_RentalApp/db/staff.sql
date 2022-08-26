CREATE TABLE IF NOT EXISTS [staff] (
[staff_id] INT,
[first_name] VARCHAR,
[last_name] VARCHAR,
[address_id] INT,
[email] VARCHAR,
[store_id] INT,
[active] BOOL,
[username] VARCHAR,
[password] VARCHAR,
[last_update] VARCHAR,
[picture] VARCHAR NULL
);

INSERT INTO staff VALUES
(1,'Mike','Hillyer',3,'Mike.Hillyer@sakilastaff.com',1,true,'Mike','8cb2237d0679ca88db6464eac60da96345513964','2006-05-16T16:13:11.79328','\x89504e470d0a5a0a'),
(2,'Jon','Stephens',4,'Jon.Stephens@sakilastaff.com',2,true,'Jon','8cb2237d0679ca88db6464eac60da96345513964','2006-05-16T16:13:11.79328',NULL);