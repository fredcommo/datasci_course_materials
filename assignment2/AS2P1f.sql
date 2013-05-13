/*Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'. */
.output stdout
.mode column
.headers on
.width 20 20
/*create tables, one for each word, then search for common docids*/
CREATE TABLE table1 AS select * from Frequency where term='transactions';
CREATE TABLE table2 AS select * from Frequency where term='world';
select count(table1.docid) from table1, table2 where table1.docid = table2.docid;

/*delete the tables*/
DROP TABLE 'table1';
DROP TABLE 'table2';

/*A simplest way is to use CREATE TEMP TABLE ... AS SELECT. The tmp tables are automatically deleted when the connexion is closed*/