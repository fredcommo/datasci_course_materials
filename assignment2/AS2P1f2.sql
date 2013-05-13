/*Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'. */
.output two_words.txt
.mode column
.headers on
.width 20 20
/*create temporary tables, one for each word, then search for common docids*/
CREATE TEMP TABLE table1 AS select * from Frequency where term='transactions';
CREATE TEMP TABLE table2 AS select * from Frequency where term='world';
select * from table1, table2 where table1.docid = table2.docid;
select count(table1.docid) from table1, table2 where table1.docid = table2.docid;

