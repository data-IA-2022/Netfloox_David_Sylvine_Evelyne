/* Compter le nombre de lignes de chaque fichier */
SELECT COUNT(*) FROM "name_basics" ;
SELECT COUNT(*) FROM "title_basics" ;
SELECT COUNT(*) FROM "title_akas" ;
SELECT COUNT(*) FROM "title_crew" ;
SELECT COUNT(*) FROM "title_episode" ;
SELECT COUNT(*) FROM "title_principals" ;
SELECT COUNT(*) FROM "title_ratings" ;

/* compter longueur max pour chaque champ */
/* name_basics */
select nconst, length(nconst) as nconst_length
from public.name_basics
where length(nconst) = (select max(length(nconst)) from public.name_basics) ;

select "primaryName" , length("primaryName" ) as "primaryName_length"
from public.name_basics
where length("primaryName") = (select max(length("primaryName")) from public.name_basics) ;

select "primaryProfession" , length("primaryProfession" ) as "primaryProfession_length"
from public.name_basics
where length("primaryProfession") = (select max(length("primaryProfession")) from public.name_basics) ;

select "knownForTitles" , length("knownForTitles" ) as "knownForTitles_length"
from public.name_basics
where length("knownForTitles") = (select max(length("knownForTitles")) from public.name_basics) ;

/* title_akas*/
select "titleId" , length("titleId" ) as "titleId_length"
from public.title_akas
where length("titleId") = (select max(length("titleId")) from public.title_akas) ;

select "title" , length("title" ) as "title_length"
from public.title_akas
where length("title") = (select max(length("title")) from public.title_akas) ;

select "region" , length("region" ) as "region_length"
from public.title_akas
where length("region") = (select max(length("region")) from public.title_akas) ;

select "language" , length("language" ) as "language_length"
from public.title_akas
where length("language") = (select max(length("language")) from public.title_akas) ;

select "types" , length("types" ) as "types_length"
from public.title_akas
where length("types") = (select max(length("types")) from public.title_akas) ;

select "types" , length("types" ) as "types_length"
from public.title_akas
where length("types") = (select max(length("types")) from public.title_akas) ;

/* title_basics*/
select "tconst" , length("tconst" ) as "tconst_length"
from public.title_basics
where length("tconst") = (select max(length("tconst")) from public.title_basics) ;

select "titleType" , length("titleType" ) as "titleType_length"
from public.title_basics
where length("titleType") = (select max(length("titleType")) from public.title_basics) ;

select "primaryTitle" , length("primaryTitle" ) as "primaryTitle_length"
from public.title_basics
where length("primaryTitle") = (select max(length("primaryTitle")) from public.title_basics) ;

select "originalTitle" , length("originalTitle" ) as "originalTitle_length"
from public.title_basics
where length("originalTitle") = (select max(length("originalTitle")) from public.title_basics) ;

select "genres" , length("genres" ) as "genres_length"
from public.title_basics
where length("genres") = (select max(length("genres")) from public.title_basics) ;

/* title_crew*/
select "tconst" , length("tconst" ) as "tconst_length"
from public.title_crew
where length("tconst") = (select max(length("tconst")) from public.title_crew) ;

select "directors" , length("directors" ) as "directors_length"
from public.title_crew
where length("directors") = (select max(length("directors")) from public.title_crew) ;

select "writers" , length("writers" ) as "writers_length"
from public.title_crew
where length("writers") = (select max(length("writers")) from public.title_crew) ;

/* title_episode*/
select "tconst" , length("tconst" ) as "tconst_length"
from public.title_episode
where length("tconst") = (select max(length("tconst")) from public.title_episode) ;

select "parentTconst" , length("parentTconst" ) as "parentTconst_length"
from public.title_episode
where length("parentTconst") = (select max(length("parentTconst")) from public.title_episode) ;

/* title_principals*/
select "tconst" , length("tconst" ) as "tconst_length"
from public.title_principals
where length("tconst") = (select max(length("tconst")) from public.title_principals) ;

select "nconst" , length("nconst" ) as "nconst_length"
from public.title_principals
where length("nconst") = (select max(length("nconst")) from public.title_principals) ;

select "category" , length("category" ) as "category_length"
from public.title_principals
where length("category") = (select max(length("category")) from public.title_principals) ;

select "job" , length("job" ) as "job_length"
from public.title_principals
where length("job") = (select max(length("job")) from public.title_principals) ;

select "characters" , length("characters" ) as "characters_length"
from public.title_principals
where length("characters") = (select max(length("characters")) from public.title_principals) ;

/* title_ratings*/
select "tconst" , length("tconst" ) as "tconst_length"
from public.title_ratings
where length("tconst") = (select max(length("tconst")) from public.title_ratings) ;