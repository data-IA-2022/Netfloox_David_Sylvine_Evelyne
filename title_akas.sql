DELETE FROM title_akas 
where "titleId"
IN (SELECT "titleId"
    FROM title_akas ta
    LEFT JOIN title_basics tb 
    ON ta."titleId" = tb.tconst 
    WHERE tb.tconst IS NULL);