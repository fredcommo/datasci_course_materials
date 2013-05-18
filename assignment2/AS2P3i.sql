/*AS2P3i*/

.mode column
.headers on

/* Create a tmp table containing q*/
CREATE TEMP TABLE q AS select * from(
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
);

/* Merge the 2 tables*/
CREATE TEMP TABLE t1 AS select * from Frequency UNION select * from q;

/*Filter the merged table on q.terms*/
create temp table t2 as select * from t1
where docid in (
select docid from t1
where term in (select term from q)
group by docid);

/*Returns the number of rows, just to double check*/
select (select count() from Frequency) as nrows;
select (select count() from q) as nrows;
select (select count() from t1) as nrows;
select (select count() from t2) as nrows;

/*compute similarities with q*/
/*.output keyword_search.txt*/
select docid, score from(
select t2.docid, t2.term, t2.count, sum(t2.count * q.count) as score
from t2, q
where t2.term = q.term
group by t2.docid)
ORDER by score desc
limit 20;

