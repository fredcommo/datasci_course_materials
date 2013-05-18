/*AS2P3i_2*/

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


/*Filter Frequency on q.terms*/
create temp table t1 as select * from Frequency
where docid in (
select docid from Frequency
where term in (select term from q)
group by docid);

/*Returns the number of rows, just to double check*/
select (select count() from Frequency) as nrows;
select (select count() from q) as nrows;
select (select count() from t1) as nrows;

/*compute similarities with q*/
/*.output keyword_search.txt*/
select docid, score from(
select t1.docid, t1.term, t1.count, sum(t1.count * q.count) as score
from t1, q
where t1.term = q.term
group by t1.docid)
ORDER by score desc
limit 20;

