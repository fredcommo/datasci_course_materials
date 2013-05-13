-- Xavier's version of AS2P2g
select v from (

select a.row_num, b.col_num, sum(a.value * b.value) as v
from a, b
where a.col_num = b.row_num
group by a.row_num, b.col_num) as t

where t.row_num = 2 and t.col_num = 3;

.mode column
.headers on
select a.row_num, b.col_num, sum(a.value * b.value) as v
from a, b
where a.col_num = b.row_num
group by a.row_num, b.col_num;
