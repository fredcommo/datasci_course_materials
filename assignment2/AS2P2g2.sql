/* Join columns to rows, group by rows and columns, then filter to get the cell you want.*/
.mode column
.headers on
CREATE TEMP TABLE newTab AS select all * from b Join a using(row_num, col_num);
select * from newTab;