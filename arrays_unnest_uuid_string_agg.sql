/* Création et décomposition des arrays pour les colonnes directors et writers dans la table title_crew */
ALTER TABLE public.title_crew ALTER COLUMN directors TYPE varchar(4989) USING directors::varchar;
ALTER TABLE public.title_crew ALTER COLUMN writers TYPE varchar(13436) USING writers::varchar;

UPDATE public.title_crew SET directors = (CASE WHEN direCtors IS NOT NULL THEN concat('{', directors, '}') END);
UPDATE public.title_crew SET writers = (CASE WHEN direCtors IS NOT NULL THEN concat('{', writers, '}') END);

ALTER TABLE public.title_crew ALTER COLUMN directors TYPE varchar(4989) ARRAY USING directors::varchar ARRAY;
ALTER TABLE public.title_crew ALTER COLUMN writers TYPE varchar(4989) ARRAY USING writers::varchar ARRAY;

CREATE TABLE new_title_crew AS (SELECT tconst, unnest(directors) AS directors, writers FROM public.title_crew);
CREATE TABLE new2_title_crew AS (SELECT tconst, directors, unnest(writers) AS writers FROM public.new_title_crew);
ALTER TABLE new2_title_crew RENAME TO title_crew;
/* Le code suivant aurait été plus efficace, mais il ne fonctionne pas avec cette version de posgres */ 
UPDATE public.title_crew SET directors = (CASE WHEN directors IS NOT NULL THEN unnest(directors) END);
UPDATE public.title_crew SET directors = (CASE WHEN writers IS NOT NULL THEN unnest(writers) END);


/* Génération des UUID */
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v1();
ALTER TABLE title_crew ADD COLUMN id UUID DEFAULT (uuid_generate_v1());


/* Décomposition des arrays pour la colonne knownForTitles dans la table name_basics */
CREATE TABLE final_name_basics AS (SELECT nconst, primaryName, birthYear, deathYear, primaryProfession, unnest(knownForTitles2) AS knownForTitles FROM public.name_basics);
ALTER TABLE final_name_basics ADD COLUMN id UUID DEFAULT (uuid_generate_v1());

/* Table créant des nconsts aggrégés par tconst unique */
CREATE TABLE grouped_name_basics AS (SELECT "knownForTitles", STRING_AGG(nconst,',') AS nconst FROM final_name_basics GROUP BY "knownForTitles");

/* Vérification du nombre de tconsts une fois l'aggrégation faite */
SELECT COUNT(DISTINCT tconst) FROM grouped_name_basics;
SELECT COUNT(*) FROM grouped_name_basics;

/* Left Join de title_basics avec la table grouped_name_basics créée au-dessus */
SELECT "primaryTitle", tconst, genres, nconst FROM title_basics A LEFT JOIN grouped_name_basics B ON (A.tconst=B."knownForTitles") WHERE "titleType"='movie';


/* Table créant des acteurs et actrices (nconsts) aggrégés par tconst unique */
CREATE VIEW actors_sel AS (SELECT * FROM title_principals WHERE category = 'actor' OR category = 'actress');
CREATE TABLE tconst_actors AS (SELECT tconst, STRING_AGG(nconst,',') AS actors FROM actors_sel GROUP BY tconst);
/* Vérification du nombre de tconsts une fois l'aggrégation faite */
SELECT COUNT(DISTINCT tconst) FROM tconst_actors;
SELECT COUNT(*) FROM tconst_actors;


/* Table final_table_basics avec la date exprimée en décennie */
CREATE TABLE final_title_basics AS (SELECT tconst, "titleType", "primaryTitle", "originalTitle", "isAdult", "startYear"/10 AS decade, "runtimeMinutes", genres FROM title_basics WHERE "titleType"='movie');
