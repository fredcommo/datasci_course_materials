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

/* Create a tmp table with Frequency docid containing q words*/
CREATE TEMP TABLE subt AS select Frequency.* from Frequency, q;
/*select * from subt group by term;*/

.output keyword_search.txt
select docid, max(value) from(
select docid, term, count, sum(count * count) as value
from subt
where term = term 
group by term);



