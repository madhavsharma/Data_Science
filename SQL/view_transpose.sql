create view transpose as select c.term,c.docid,c.count from Frequency c JOIN Frequency p where c.term = p.term group by c.term,c.docid;
