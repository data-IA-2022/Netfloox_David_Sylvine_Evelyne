select * from title_akas 
A left join title_basics F ON (A."titleId"=F.tconst) 
Where F.tconst IS NULL Limit 10;