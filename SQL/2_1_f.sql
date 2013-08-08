 select docid from  Frequency f where f.term = 'world' intersect select docid from Frequency v where v.term = 'transactions';
