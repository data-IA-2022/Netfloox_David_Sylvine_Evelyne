/*  modif les types pour chaque colonne pour chaque table */
ALTER TABLE public.name_basics ALTER COLUMN nconst TYPE varchar(10) USING nconst::varchar;
ALTER TABLE public.name_basics ALTER COLUMN "primaryName" TYPE varchar(105) USING "primaryName"::varchar;
ALTER TABLE public.name_basics ALTER COLUMN "birthYear" TYPE int USING "birthYear"::int;
ALTER TABLE public.name_basics ALTER COLUMN "deathYear" TYPE int USING "deathYear"::int;
ALTER TABLE public.name_basics ALTER COLUMN "primaryProfession" TYPE varchar(66) USING "primaryProfession"::varchar;
ALTER TABLE public.name_basics ALTER COLUMN "knownForTitles" TYPE varchar(64) USING "knownForTitles"::varchar;
ALTER TABLE public.name_basics ALTER COLUMN "knownForTitles2" TYPE varchar(10)[] USING "knownForTitles2"::varchar;

ALTER TABLE public.title_akas ALTER COLUMN "titleId" TYPE varchar(10) USING "titleId"::varchar;
ALTER TABLE public.title_akas ALTER COLUMN title TYPE varchar(831) USING title::varchar;
ALTER TABLE public.title_akas ALTER COLUMN region TYPE varchar(4) USING region::varchar;
ALTER TABLE public.title_akas ALTER COLUMN "language" TYPE varchar(3) USING "language"::varchar;
ALTER TABLE public.title_akas ALTER COLUMN "types" TYPE varchar(20) USING "types"::varchar;
ALTER TABLE public.title_akas ALTER COLUMN "attributes" TYPE varchar(62) USING "attributes"::varchar;
ALTER TABLE public.title_akas ALTER COLUMN "isOriginalTitle" TYPE int USING "isOriginalTitle"::int;

ALTER TABLE public.title_basics ALTER COLUMN tconst TYPE varchar(10) USING tconst::varchar;
ALTER TABLE public.title_basics ALTER COLUMN "titleType" TYPE varchar(12) USING "titleType"::varchar;
ALTER TABLE public.title_basics ALTER COLUMN "primaryTitle" TYPE varchar(419) USING "primaryTitle"::varchar;
ALTER TABLE public.title_basics ALTER COLUMN "originalTitle" TYPE varchar(419) USING "originalTitle"::varchar;
ALTER TABLE public.title_basics ALTER COLUMN "endYear" TYPE int4 USING "endYear"::int4;
ALTER TABLE public.title_basics ALTER COLUMN "startYear" TYPE int4 USING "startYear"::int4;
ALTER TABLE public.title_basics ALTER COLUMN "runtimeMinutes" TYPE int4 USING "runtimeMinutes"::int4;
ALTER TABLE public.title_basics ALTER COLUMN genres TYPE varchar(32) USING genres::varchar;

ALTER TABLE public.title_crew ALTER COLUMN tconst TYPE varchar(10) USING tconst::varchar;
ALTER TABLE public.title_crew ALTER COLUMN directors TYPE varchar(4987) USING directors::varchar;
ALTER TABLE public.title_crew ALTER COLUMN writers TYPE varchar(13434) USING writers::varchar;

ALTER TABLE public.title_episode ALTER COLUMN tconst TYPE varchar(10) USING tconst::varchar;
ALTER TABLE public.title_episode ALTER COLUMN "parentTconst" TYPE varchar(10) USING "parentTconst"::varchar;
ALTER TABLE public.title_episode ALTER COLUMN "seasonNumber" TYPE int USING "seasonNumber"::int;
ALTER TABLE public.title_episode ALTER COLUMN "episodeNumber" TYPE int USING "episodeNumber"::int;

ALTER TABLE public.title_principals ALTER COLUMN tconst TYPE varchar(10) USING tconst::varchar;
ALTER TABLE public.title_principals ALTER COLUMN nconst TYPE varchar(10) USING nconst::varchar;
ALTER TABLE public.title_principals ALTER COLUMN category TYPE varchar(19) USING category::varchar;
ALTER TABLE public.title_principals ALTER COLUMN job TYPE varchar(286) USING job::varchar;
ALTER TABLE public.title_principals ALTER COLUMN "characters" TYPE varchar(1308) USING "characters"::varchar;

ALTER TABLE public.title_ratings ALTER COLUMN tconst TYPE varchar(10) USING tconst::varchar;


