       IDENTIFICATION DIVISION.
       PROGRAM-ID. EVAL-EX6.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 X PIC 9 VALUE 3.

       PROCEDURE DIVISION.
       EVALUATE X
           WHEN NOT 5
               DISPLAY "X IS NOT 5"
           WHEN 5
               DISPLAY "X IS 5"
           WHEN OTHER
               DISPLAY "X IS SOMETHING ELSE"
       END-EVALUATE.
       STOP RUN.
