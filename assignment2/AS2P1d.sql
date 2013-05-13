/*AS2P1d: Write a SQL statement to count the number of documents containing the word “parliament”*/
.output count.txt
.mode column
.headers on
select count(count) from Frequency where term='parliament';

/* Display results in terminal*/
.output stdout
.mode column
.headers on
select * from Frequency where term='parliament';
