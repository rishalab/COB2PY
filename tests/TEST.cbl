       IDENTIFICATION DIVISION.
       PROGRAM-ID. NegatedConditionExample.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 NUM PIC 9 VALUE 8.

       PROCEDURE DIVISION.
           IF NOT NUM <> 10
               DISPLAY "NUM is not equal to 10."
           ELSE
               DISPLAY "NUM is equal to 10."
           END-IF.
           STOP RUN.
