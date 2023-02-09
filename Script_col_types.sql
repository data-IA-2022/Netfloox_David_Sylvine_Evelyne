/*  modif les types pour chaque colonne pour chaque table */
SELECT COUNT(*) FROM "name_basics" ;

ALTER TABLE public.name_basics ALTER COLUMN nconst TYPE varchar(10) USING nconst::varchar;
ALTER TABLE public.name_basics ALTER COLUMN "primaryName" TYPE varchar(150) USING "primaryName"::varchar;
ALTER TABLE public.name_basics ALTER COLUMN "birthYear" TYPE int USING "birthYear"::int;
ALTER TABLE public.name_basics ALTER COLUMN "deathYear" TYPE int USING "deathYear"::int;
ALTER TABLE public.name_basics ALTER COLUMN "primaryProfession" TYPE varchar(150) USING "primaryProfession"::varchar;
ALTER TABLE public.name_basics ALTER COLUMN "knownForTitles" TYPE varchar(150) USING "knownForTitles"::varchar;

ALTER TABLE public.title_basics ALTER COLUMN genres TYPE varchar(50) USING genres::varchar;

ALTER TABLE public.title_akas ALTER COLUMN "titleId" TYPE varchar(9) USING "titleId"::varchar;
ALTER TABLE public.title_akas ALTER COLUMN title TYPE varchar(200) USING title::varchar;
ALTER TABLE public.title_akas ALTER COLUMN region TYPE varchar(4) USING region::varchar;
ALTER TABLE public.title_akas ALTER COLUMN "language" TYPE varchar(5) USING "language"::varchar;
ALTER TABLE public.title_akas ALTER COLUMN "types" TYPE varchar(50) USING region::varchar;
ALTER TABLE public.title_akas ALTER COLUMN "attributes" TYPE varchar(50) USING region::varchar;

ALTER TABLE public.title_basics ALTER COLUMN tconst TYPE varchar(9) USING tconst::varchar;
ALTER TABLE public.title_basics ALTER COLUMN "titleType" TYPE varchar(15) USING "titleType"::varchar;
ALTER TABLE public.title_basics ALTER COLUMN "primaryTitle" TYPE varchar(200) USING "primaryTitle"::varchar;
ALTER TABLE public.title_basics ALTER COLUMN "originalTitle" TYPE varchar(200) USING "originalTitle"::varchar;
ALTER TABLE public.title_basics ALTER COLUMN "endYear" TYPE int4 USING "endYear"::int4;
ALTER TABLE public.title_basics ALTER COLUMN "startYear" TYPE int4 USING "startYear"::int4;
ALTER TABLE public.title_basics ALTER COLUMN "runtimeMinutes" TYPE int4 USING "runtimeMinutes"::int4;

ALTER TABLE public.title_crew ALTER COLUMN tconst TYPE varchar(9) USING tconst::varchar;
ALTER TABLE public.title_crew ALTER COLUMN directors TYPE varchar(100) USING directors::varchar;
ALTER TABLE public.title_crew ALTER COLUMN writers TYPE varchar(200) USING writers::varchar;

ALTER TABLE public.title_episode ALTER COLUMN tconst TYPE varchar(9) USING tconst::varchar;
ALTER TABLE public.title_episode ALTER COLUMN "parentTconst" TYPE varchar(50) USING "parentTconst"::varchar;
ALTER TABLE public.title_episode ALTER COLUMN "seasonNumber" TYPE varchar(5) USING "seasonNumber"::varchar;
ALTER TABLE public.title_episode ALTER COLUMN "episodeNumber" TYPE varchar(5) USING "episodeNumber"::varchar;

ALTER TABLE public.title_principals ALTER COLUMN tconst TYPE varchar(9) USING tconst::varchar;
ALTER TABLE public.title_principals ALTER COLUMN nconst TYPE varchar(50) USING nconst::varchar;
ALTER TABLE public.title_principals ALTER COLUMN category TYPE varchar(20) USING category::varchar;
ALTER TABLE public.title_principals ALTER COLUMN job TYPE varchar(100) USING job::varchar;
ALTER TABLE public.title_principals ALTER COLUMN "characters" TYPE varchar(150) USING "characters"::varchar;

ALTER TABLE public.title_ratings ALTER COLUMN tconst TYPE varchar(9) USING tconst::varchar;



