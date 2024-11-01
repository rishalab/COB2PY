        IDENTIFICATION  DIVISION.
        PROGRAM-ID.      christmas.
        ENVIRONMENT    DIVISION.
        DATA           DIVISION.
        WORKING-STORAGE SECTION.
        77  NUM         PIC 9(2).
        PROCEDURE       DIVISION.
        MAIN.
        ACCEPT  NUM     FROM CONSOLE.
        IF NUM = 25 THEN
            DISPLAY "Christmas"  UPON CONSOLE
        ELSE IF NUM = 24 THEN
            DISPLAY  "Christmas Eve" UPON CONSOLE
        ELSE IF NUM = 23 THEN
            DISPLAY  "Christmas Eve Eve" UPON CONSOLE
        ELSE IF NUM = 22 THEN
            DISPLAY  "Christmas Eve Eve Eve" UPON CONSOLE  
        END-IF 
        END-IF
        END-IF.
        STOP RUN.