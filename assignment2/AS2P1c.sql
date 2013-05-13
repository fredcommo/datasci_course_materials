/*Combine queries using UNION (without duplicates, default)*/
.output stdout
.mode column
.headers on
SELECT count(term) FROM(
SELECT term FROM Frequency where docid = '10398_txt_earn' AND count = '1'
UNION
SELECT term FROM Frequency where docid = '925_txt_trade' AND count = '1'
);

/*Combine queries using UNION ALL allows duplicates*/
SELECT count(term) FROM(
SELECT term FROM Frequency where docid = '10398_txt_earn' AND count = '1'
UNION ALL
SELECT term FROM Frequency where docid = '925_txt_trade' AND count = '1'
);

