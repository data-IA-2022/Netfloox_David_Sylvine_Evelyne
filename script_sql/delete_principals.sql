DELETE FROM title_principals tp
where tp.tconst
IN (SELECT tp.tconst
    FROM title_principals tp
    LEFT JOIN title_basics tb 
    ON tp.tconst = tb.tconst 
    WHERE tb.tconst IS NULL);