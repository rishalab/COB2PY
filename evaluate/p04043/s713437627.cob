       IDENTIFICATION DIVISION.
       PROGRAM-ID. ABC042-A.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       77 STR PIC X(100).
       77 A PIC 9(2).
       77 B PIC 9(2).
       77 C PIC 9(2).
       77 COUNT5 PIC 9(1) VALUE 0.
       77 COUNT7 PIC 9(1) VALUE 0.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
               ACCEPT STR FROM SYSIN.
               UNSTRING STR DELIMITED " "
                INTO A B C.
               EVALUATE A
                   WHEN 5
                       ADD 1 TO COUNT5
                   WHEN 7
                       ADD 1 TO COUNT7
               END-EVALUATE
               EVALUATE B
                   WHEN 5
                       ADD 1 TO COUNT5
                   WHEN 7
                       ADD 1 TO COUNT7
               END-EVALUATE
               EVALUATE C
                   WHEN 5
                       ADD 1 TO COUNT5
                   WHEN 7
                       ADD 1 TO COUNT7
               END-EVALUATE
               IF COUNT5 = 2 AND COUNT7 = 1 THEN
                   DISPLAY "YES"
               ELSE
                   DISPLAY "NO"
               END-IF
               STOP RUN.
       END PROGRAM ABC042-A.
