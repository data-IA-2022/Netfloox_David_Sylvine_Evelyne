/* test pour mettre en array */
ALTER TABLE title_episode  DROP COLUMN "index";
ALTER TABLE title_akas  DROP COLUMN "index";
ALTER TABLE name_basics  DROP COLUMN "index";
ALTER TABLE title_ratings  DROP COLUMN "index";

ALTER TABLE title_basics  DROP COLUMN "index";
ALTER TABLE title_crew  DROP COLUMN "index";
ALTER TABLE title_principals  DROP COLUMN "index";

/*duplicate column */
ALTER TABLE name_basics  DROP COLUMN "knownForTitles2";

alter table name_basics add column "knownForTitles2" text ;
update name_basics set "knownForTitles2" = "knownForTitles" ;

update name_basics set "knownForTitles2" = '{'||"knownForTitles2"||'}' ;

/* set to array */
ALTER TABLE public.name_basics ALTER COLUMN "knownForTitles2" TYPE varchar(10)[] USING "knownForTitles2"::varchar[];

/* base pour créer foreign key avec array */

ALTER TABLE public.name_basics ADD CONSTRAINT name_basics_fk FOREIGN KEY (EACH ELEMENT OF "knownForTitles2") REFERENCES public.title_basics(tconst);
