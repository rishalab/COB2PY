       IDENTIFICATION                   DIVISION.
       PROGRAM-ID.                      ABC_099_A.
       ENVIRONMENT                      DIVISION.
       DATA                             DIVISION.
       WORKING-STORAGE SECTION.
           01 N PIC 9(4).
       PROCEDURE                        DIVISION.
       MAIN.
           ACCEPT N FROM CONSOLE.
           IF 999 < N THEN
               DISPLAY "ABD" UPON CONSOLE
           ELSE
               DISPLAY "ABC" UPON CONSOLE
           END-IF.
           STOP RUN.
