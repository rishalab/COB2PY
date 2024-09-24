       IDENTIFICATION DIVISION.
       PROGRAM-ID. EVAL-EX1.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 X PIC 9 VALUE 1.

       PROCEDURE DIVISION.
       EVALUATE X
           WHEN 1
               DISPLAY "X IS 1"
           WHEN 2
               DISPLAY "X IS 2"
           WHEN OTHER
               DISPLAY "X IS NEITHER 1 NOR 2"
       END-EVALUATE.
       STOP RUN.
