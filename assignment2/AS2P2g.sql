/*multiply: Express A X B as a SQL query, referring to the class lecture for hints.*/
/*turn in a text document, multiply.txt, which is value of the cell (2,3)*/
.mode column
.headers on
.tables
select * from a where row_num = 1;
select * from b where col_num = 2;

select * from(
select * from a where row_num = 1
union
select * from b where col_num = 2);
/**/

/* Create subtables, one containing the values of a.row = 2, the other containing b.col =3*/
/* Then sum the products a.col = b.row*/
CREATE TEMP TABLE suba AS select * from a where row_num = 2;
CREATE TEMP TABLE subb AS select * from b where col_num = 3;

.output multiply.txt
select sum(suba.value*subb.value) from suba, subb where suba.col_num = subb.row_num;






/* Join columns to rows, group by rows and columns, then filter to get the cell you want.*/
select a.value, b.value from a, b where a.row_num = 2 and b.col_num = 3;

