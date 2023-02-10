/* test pour mettre en array */
ALTER TABLE public.name_basics ALTER COLUMN "knownForTitles" TYPE varchar(10)[] USING "knownForTitles"::varchar;