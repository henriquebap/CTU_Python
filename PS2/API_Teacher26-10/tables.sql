CREATE TABLE "PF1761"."ARTIST" 
   (	
    "ID" NUMBER(*,0) GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE  NOT NULL ENABLE, 
	"NAME" VARCHAR2(128), 
    "CATEGORY" VARCHAR2(64), 
	 PRIMARY KEY ("ID")
  USING INDEX ENABLE
   ) ;

CREATE TABLE "PF1761"."ALBUM" 
   (	
    "ID" NUMBER(*,0) GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE  NOT NULL ENABLE, 
	"NAME" VARCHAR2(256 CHAR), 
    "SLUG" VARCHAR2(256 CHAR), 
    "LINKS" VARCHAR2(128 CHAR), 
    "RELEASE" NUMBER(*,0), 
    "DESCRIPTION" VARCHAR2(512 CHAR), 
	"ARTIST_ID" NUMBER(*,0), 
	 PRIMARY KEY ("ID")
  USING INDEX  ENABLE, 
	 FOREIGN KEY ("ARTIST_ID")
	  REFERENCES "PF1761"."ARTIST" ("ID") ENABLE
   ) ;


CREATE TABLE "PF1761"."SONG" 
   (	
    "ID" NUMBER(*,0) GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE  NOT NULL ENABLE, 
	"NAME" VARCHAR2(256 CHAR), 
    "TRACK_NUMBER" NUMBER(*,0), 
	"ALBUM_ID" NUMBER(*,0), 
	 PRIMARY KEY ("ID")
  USING INDEX  ENABLE, 
	 FOREIGN KEY ("ALBUM_ID")
	  REFERENCES "PF1761"."ALBUM" ("ID") ENABLE
   ) ;