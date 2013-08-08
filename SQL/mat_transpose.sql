create view mat_transpose as select c.term as row ,c.docid as col,c.count as val from Frequency c JOIN Frequency p where c.term = p.term group by c.term,c.docid;
