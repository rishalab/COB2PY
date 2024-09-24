       IDENTIFICATION DIVISION.
       PROGRAM-ID. EVAL-EX7.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 X PIC 9 VALUE 2.

       PROCEDURE DIVISION.
       EVALUATE X
           WHEN 1
               DISPLAY "X IS 1"
           WHEN 2
               DISPLAY "X IS 2"
           WHEN 3
               DISPLAY "X IS 3"
           WHEN OTHER
               DISPLAY "X IS SOMETHING ELSE"
       END-EVALUATE.
       STOP RUN.
