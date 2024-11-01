       IDENTIFICATION DIVISION.
       PROGRAM-ID. ABC046-A.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       77 STR PIC X(11).
       77 A PIC 9(3).
       77 B PIC 9(3).
       77 C PIC 9(3).

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
               ACCEPT STR FROM SYSIN.
               UNSTRING STR DELIMITED " "
               INTO A B C.
               IF A = B AND B = C THEN
                   DISPLAY 1
               ELSE IF A = B AND B NOT= C THEN
                   DISPLAY 2
               ELSE IF B = C AND C NOT= A THEN
                   DISPLAY 2
               ELSE IF C = A AND A NOT= B THEN
                   DISPLAY 2
               ELSE
                   DISPLAY 3
               END-IF.
               STOP RUN.
       END PROGRAM ABC046-A.
