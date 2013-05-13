/* (h) similarity matrix: Write a query to compute the similarity matrix DDT. (Hint: The transpose is trivial*/
/*	Just join on columns to columns instead of columns to rows.) The query could take some time to run if you compute the entire result.*/
/*	But notice that you don't need to compute the similarity of both (doc1, doc2) and (doc2, doc1) -- they are the same, since similarity is symmetric.*/
/*	If you wish, you can avoid this wasted work by adding a condition of the form a.docid < b.docid to your query.*/
/*	(But the query still won't return immediately if you try to compute every result.)*/

/* What to turn in: On the assignment website, turn in a text document, similarity_matrix.txt, which has the similarity of the two documents '10080_txt_crude' and '17035_txt_earn'.*/

.mode columns
.headers on
.tables
--.output similarity_matrix.txt

create temp table t1 as select * from Frequency where docid = '10080_txt_crude';
create temp table t2 as select * from Frequency where docid = '17035_txt_earn';

select sum(t1.count * t2.count)
from t1, t2
where t1.term = t2.term;

select value from(
select term, count, sum(count * count) as value
from Frequency
where term = term and docid = '10080_txt_crude' or docid = '17035_txt_earn'
group by term) as t;