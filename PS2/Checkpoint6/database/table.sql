-- Verificar se a tabela "Store" existe
DECLARE
    STORE_TABLE_EXISTS NUMBER;
BEGIN
    SELECT
        COUNT(*) INTO STORE_TABLE_EXISTS
    FROM
        USER_TABLES
    WHERE
        TABLE_NAME = 'Store';
    IF STORE_TABLE_EXISTS = 1 THEN
 -- Se a tabela "Store" existe, execute o DROP TABLE
        EXECUTE IMMEDIATE 'DROP TABLE STORE';
    END IF;
END;
/

-- Verificar se a tabela "Item" existe
DECLARE
    ITEM_TABLE_EXISTS NUMBER;
BEGIN
    SELECT
        COUNT(*) INTO ITEM_TABLE_EXISTS
    FROM
        USER_TABLES
    WHERE
        TABLE_NAME = 'ITEM';
    IF ITEM_TABLE_EXISTS = 1 THEN
 -- Se a tabela "Item" existe, execute o DROP TABLE
        EXECUTE IMMEDIATE 'DROP TABLE ITEM';
    END IF;
END;
/

-- Verifique se a sequência "ITEM_SEQ" já existe
DECLARE
    SEQUENCE_EXISTS NUMBER;
BEGIN
    SELECT
        COUNT(*) INTO SEQUENCE_EXISTS
    FROM
        USER_SEQUENCES
    WHERE
        SEQUENCE_NAME = 'ITEM_SEQ';
    IF SEQUENCE_EXISTS = 0 THEN
 -- Se a sequência não existe, crie-a
        EXECUTE IMMEDIATE 'CREATE SEQUENCE ITEM_SEQ
      START WITH 1
      INCREMENT BY 1
      NOMAXVALUE
      NOCYCLE';
    END IF;
END;
/

DECLARE
    SEQUENCE_EXISTS NUMBER;
BEGIN
    SELECT
        COUNT(*) INTO SEQUENCE_EXISTS
    FROM
        USER_SEQUENCES
    WHERE
        SEQUENCE_NAME = 'STORE_SEQ';
    IF SEQUENCE_EXISTS = 0 THEN
 -- Se a sequência não existe, crie-a
        EXECUTE IMMEDIATE 'CREATE SEQUENCE STORE_SEQ
      START WITH 1
      INCREMENT BY 1
      NOMAXVALUE
      NOCYCLE';
    END IF;
END;
/

-- Renomear a tabela "Item" para "ItemOld"

SELECT
    TABLE_NAME
FROM
    USER_TABLES
WHERE
    TABLE_NAME = 'ITEM';

ALTER TABLE ITEM RENAME TO ITEMOLD;

-- Excluir a tabela "Item" existente
DROP TABLE ITEM_CP6;

SELECT
    TABLE_NAME
FROM
    USER_TABLES
WHERE
    TABLE_NAME = 'STORE';

ALTER TABLE STORE RENAME TO STOREOLD;

-- Excluir a tabela "STORE" existente
DROP TABLE STORE;

-- Criar uma sequência para a coluna ID da tabela Store
CREATE SEQUENCE STORE_SEQ
  START WITH 1
  INCREMENT BY 1
  NOMAXVALUE
  NOCYCLE;

-- Criar a tabela Store com a coluna ID autoincrementável
CREATE TABLE "STORE_CP6" (
    ID NUMBER(10) DEFAULT STORE_SEQ.NEXTVAL PRIMARY KEY,
    NAME VARCHAR2(50 CHAR) NOT NULL
);

-- Criar uma sequência para a coluna ID da tabela Item
CREATE SEQUENCE ITEM_SEQ
  START WITH 1
  INCREMENT BY 1
  NOMAXVALUE
  NOCYCLE;

-- Criar a tabela Item com a coluna ID autoincrementável
CREATE TABLE "ITEM_CP6" (
    ID NUMBER(10) DEFAULT ITEM_SEQ.NEXTVAL PRIMARY KEY,
    NAME VARCHAR2(25 CHAR),
    DESCRIPTION VARCHAR2(100 CHAR),
    PRICE NUMBER(10, 2) DEFAULT 0,
    STORE_ID INTEGER,
    FOREIGN KEY (STORE_ID) REFERENCES "STORE_CP6"(ID)
);