DELETE FROM corona T1
    USING   corona T2
WHERE   T1.ctid < T2.ctid 
    AND T1.index  = T2.index; 