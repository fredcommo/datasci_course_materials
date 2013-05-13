/*Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms.*/
/*Hint: You can use the HAVING clause, or you can use a nested query.*/
/*Another hint: Remember that the count column contains the term frequencies,and you want to consider duplicates.) (docid, term_count)*/

.output stdout
.mode column
.headers on
/*select count(docid) from Frequency where docid = '12848_txt_trade';
select sum(count) from Frequency where docid = '12848_txt_trade';
select distinct docid from Frequency where docid = '12848_txt_trade';
select count(distinct docid) from Frequency where docid = '12848_txt_trade';*/

select count(count) from (select * from Frequency group by docid having sum(count)>300);

