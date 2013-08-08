select v from (select a.row_num as r , b.col_num as p, SUM(a.value*b.value) as v from  a JOIN b where a.col_num = b.row_num GROUP BY a.row_num,b.col_num) where r = '2' and p = '3';
