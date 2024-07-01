CREATE TABLE finances_newbankname (
    kor_co_nm VARCHAR(255)
);
INSERT INTO finances_newbankname (kor_co_nm)
SELECT DISTINCT kor_co_nm 
FROM finances_bankname 
ORDER BY kor_co_nm;

